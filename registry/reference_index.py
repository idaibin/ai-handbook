"""Handbook-owned metadata contract; no retrieval, execution or network access."""
import hashlib
import re
from datetime import date
from pathlib import PurePosixPath

VERSION = 'handbook-reference-index/1'
OWNER = 'idaibin/ai-handbook'
KINDS = {'method', 'interaction-pattern', 'prompt-case', 'audit-case', 'design-candidate'}
STATUSES = {'reference', 'candidate', 'historical'}
EVIDENCE = {'source-read', 'local-experiment', 'not-verified'}


def validate_reference_index(document, source_root=None):
    """Validate metadata only unless producer explicitly supplies source_root."""
    def require(condition, message):
        if not condition:
            raise ValueError('references: ' + message)

    def obj(value, keys, label):
        require(isinstance(value, dict) and set(value) == set(keys.split()), label + ': unexpected/missing fields')

    def text(value):
        return isinstance(value, str) and bool(value.strip())

    def strings(value, label, nonempty=False):
        require(isinstance(value, list) and all(text(v) for v in value), label + ': expected strings')
        require(len(value) == len(set(value)), label + ': duplicate values')
        require(not nonempty or bool(value), label + ': empty')

    obj(document, 'schema_version owner basis entries', 'index')
    require(document['schema_version'] == VERSION and document['owner'] == OWNER, 'unsupported contract/owner')
    basis = document['basis']
    obj(basis, 'repository revision', 'basis')
    require(basis['repository'] == OWNER, 'wrong repository')
    require(isinstance(basis['revision'], str) and re.fullmatch('[0-9a-f]{40}', basis['revision']), 'fixed revision required')
    require(isinstance(document['entries'], list), 'entries must be a list')
    ids = set()
    for row in document['entries']:
        obj(row, 'id kind title summary topics stages applies_to excludes source status evidence rights freshness', 'entry')
        require(text(row['id']) and row['id'] not in ids, 'unique nonempty id required')
        ids.add(row['id'])
        require(text(row['kind']) and text(row['status']) and row['kind'] in KINDS and row['status'] in STATUSES, 'unknown kind/status')
        require(text(row['title']) and text(row['summary']), 'title/summary required')
        for key in ('topics', 'stages', 'applies_to', 'excludes'):
            strings(row[key], key, key == 'topics')
        require(not set(row['applies_to']) & set(row['excludes']), 'contradictory constraints')
        source = row['source']
        obj(source, 'repository path revision sha256', 'source')
        require(source['repository'] == basis['repository'] and source['revision'] == basis['revision'], 'source/basis mismatch')
        path = source['path']
        require(text(path) and not any(ord(c) < 32 or ord(c) == 127 for c in path) and '\\' not in path and not path.startswith('/') and all(p not in ('', '.', '..') for p in path.split('/')), 'unsafe source path')
        require(not PurePosixPath(path).is_absolute(), 'absolute source path')
        require(isinstance(source['sha256'], str) and re.fullmatch('[0-9a-f]{64}', source['sha256']), 'source sha256 required')
        obj(row['evidence'], 'level limitations', 'evidence')
        require(text(row['evidence']['level']) and row['evidence']['level'] in EVIDENCE, 'unknown evidence level')
        strings(row['evidence']['limitations'], 'limitations', True)
        obj(row['rights'], 'status allowed_use', 'rights')
        rights = row['rights']
        require(text(rights['status']) and rights['status'] in {'unknown', 'reference-only', 'licensed'}, 'unknown rights status')
        strings(rights['allowed_use'], 'allowed_use', True)
        require(set(rights['allowed_use']) <= {'reference', 'adapt', 'copy'}, 'unknown allowed use')
        require(rights['status'] == 'licensed' or rights['allowed_use'] == ['reference'], 'unresolved rights cannot allow copying/adaptation')
        obj(row['freshness'], 'checked_at recheck_when', 'freshness')
        checked = row['freshness']['checked_at']
        require(isinstance(checked, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}', checked), 'checked_at must be ISO date')
        date.fromisoformat(checked)
        strings(row['freshness']['recheck_when'], 'recheck_when', True)
        if source_root is not None:
            root = source_root.resolve()
            target = (root / path).resolve()
            require(target.is_relative_to(root) and target.is_file(), 'source unavailable: ' + path)
            require(hashlib.sha256(target.read_bytes()).hexdigest() == source['sha256'], 'source stale: ' + path)
    return {'schema_version': VERSION, 'entry_count': len(ids), 'source_bytes_checked': source_root is not None,
            'authorizes_execution': False}
