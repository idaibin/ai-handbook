import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from registry.validate import RegistryError, validate


ROOT = Path(__file__).resolve().parents[1]


class RegistryValidationTest(unittest.TestCase):
    def copy_contract(self, destination: Path) -> None:
        shutil.copytree(ROOT / "registry", destination / "registry")
        target_workflows = destination / "workflows" / "ai-engineering-system"
        target_workflows.parent.mkdir(parents=True)
        shutil.copytree(ROOT / "workflows" / "ai-engineering-system", target_workflows)
        target_experiments = destination / "experiments" / "story-studio-60s-pilot"
        target_experiments.parent.mkdir(parents=True)
        shutil.copytree(ROOT / "experiments" / "story-studio-60s-pilot", target_experiments)

    def test_current_contract_closes(self) -> None:
        result = validate(ROOT)
        self.assertTrue(result["verified"])
        self.assertEqual(result["route_count"], 4)
        self.assertTrue(result["pilot_experiment"]["contract_validated"])
        self.assertEqual(result["pilot_experiment"]["stage_count"], 10)

    def test_unknown_project_route_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_contract(root)
            path = root / "registry" / "projects.yaml"
            value = yaml.safe_load(path.read_text())
            value["projects"][0]["route"] = {"primary": "missing-route"}
            path.write_text(yaml.safe_dump(value, sort_keys=False))
            with self.assertRaises(RegistryError):
                validate(root)

    def test_content_media_boundary_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_contract(root)
            path = root / "registry" / "routes.yaml"
            value = yaml.safe_load(path.read_text())
            media = next(row for row in value["routes"] if row["id"] == "media-production-system")
            media["outputs"].remove("video")
            path.write_text(yaml.safe_dump(value, sort_keys=False))
            with self.assertRaises(RegistryError):
                validate(root)

    def test_missing_pilot_mandatory_gate_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_contract(root)
            path = root / "experiments" / "story-studio-60s-pilot" / "task-plan.yaml"
            value = yaml.safe_load(path.read_text())
            # Remove gate from stage 0
            value["stages"][0]["gates"] = []
            path.write_text(yaml.safe_dump(value, sort_keys=False))
            with self.assertRaises(RegistryError):
                validate(root)

    def test_pilot_route_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_contract(root)
            path = root / "experiments" / "story-studio-60s-pilot" / "task-plan.yaml"
            value = yaml.safe_load(path.read_text())
            value["route"] = "wrong-route"
            path.write_text(yaml.safe_dump(value, sort_keys=False))
            with self.assertRaises(RegistryError):
                validate(root)

    def test_pilot_claimed_execution_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_contract(root)
            path = root / "experiments" / "story-studio-60s-pilot" / "task-plan.yaml"
            value = yaml.safe_load(path.read_text())
            value["claimed_execution"] = True
            path.write_text(yaml.safe_dump(value, sort_keys=False))
            with self.assertRaises(RegistryError):
                validate(root)

    def test_pilot_self_approval_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_contract(root)
            path = root / "experiments" / "story-studio-60s-pilot" / "task-plan.yaml"
            value = yaml.safe_load(path.read_text())
            value["stages"][4]["review_owner"] = value["stages"][4]["owner"]
            path.write_text(yaml.safe_dump(value, sort_keys=False))
            with self.assertRaises(RegistryError):
                validate(root)

    def test_pilot_missing_master_hash_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.copy_contract(root)
            path = root / "experiments" / "story-studio-60s-pilot" / "task-plan.yaml"
            value = yaml.safe_load(path.read_text())
            render = next(stage for stage in value["stages"] if stage["id"] == "09-master-render-and-playback")
            render["outputs"].remove("master_sha256")
            path.write_text(yaml.safe_dump(value, sort_keys=False))
            with self.assertRaises(RegistryError):
                validate(root)


if __name__ == "__main__":
    unittest.main()
