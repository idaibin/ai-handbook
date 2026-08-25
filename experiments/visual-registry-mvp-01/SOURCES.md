# Source Audit

Checked on: 2026-08-25

## Decision

The listed repositories are references, not an import dataset. This experiment contains no copied third-party prompt, image, artist list, or provider-version parameter.

| Repository | Fixed commit | Stars snapshot | License | MVP decision |
| --- | --- | ---: | --- | --- |
| `willwulfken/MidJourney-Styles-and-Keywords-Reference` | `1e54e7f` | 12,289 | No declared license | Taxonomy reference only; no content copied. |
| `f/prompts.chat` | `db92786` | 167,861 | MIT code / CC0 prompt data | Reference separation of code, data, variables, and distribution. |
| `CaylaLuo/awesome-midjourney-prompts` | `0db48f7` | 1 | No declared license | Excluded from MVP. The “high-star” premise is not supported. |
| `YouMind-OpenLab/awesome-gemini-3-prompts` | `602c9fd` | 514 | CC BY 4.0 | Reference argument placeholders and source metadata; no community prompts copied. |
| `AIwork4me/awesome-gemini-visual-gems` | `dde992e` | 50 | MIT | Reference style/use-case and workflow/design-rule separation. |
| `Amery2010/midjourney-prompt-generator` | `ff69f7f` | 188 | MIT | UI interaction reference only; website is out of this MVP. |

## Extracted patterns

- Durable taxonomy dimensions: style, palette, material, texture, lighting, camera, composition, atmosphere, constraints.
- Prompt/application separation: semantic data is distinct from provider syntax and distribution UI.
- Variable injection is a compiler input, not stored inside the durable contract.
- Each public example must keep source identity and rights status.
- A gallery is a read-only projection and must not become the registry authority.

## Explicit exclusions

- Artist-name emulation as a registry dimension.
- Model-version flags in a Visual Contract.
- Community prompt ingestion.
- Third-party example images.
- Generic prompt marketplace or social features.
