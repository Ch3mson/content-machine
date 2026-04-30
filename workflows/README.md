# Workflows

Use this directory as the action index for agents.

| Workflow | File | Trigger | Output |
| --- | --- | --- | --- |
| Workflow A | `workflow-a-new-account.md` | New account or account onboarding | Orchestrates A0-A4. |
| Workflow A0 | `workflow-a0-account-intake-reference-map.md` | Account intake or reference organization | `account-brief.md` and `extractions/reference-map.md`. |
| Workflow A1 | `workflow-a1-writing-principle-extraction.md` | Baseline writing extraction | Indexed `writing.md` and `writing/` folder. |
| Workflow A2 | `workflow-a2-design-principle-extraction.md` | Design extraction | `design.md` and `image.md`. |
| Workflow A3 | `workflow-a3-writing-design-quality-gate.md` | Test writing/design quality | Approved sample PNG and revision notes. |
| Workflow A4 | `workflow-a4-angle-extraction-to-presets.md` | Extract repeatable angles | Validated `presets.md` additions. |
| Workflow B | `workflow-b-new-post.md` | New slideshow for an existing account | User-approved full copy, then post folder with flow, sourced images, script, and processed slides. |
| Workflow C | `workflow-c-image-processing.md` | Process/render slideshow images | Final `processed/slide_N.png` files. |

Routing lives in `../AGENTS.md`. If a user tags a workflow, start the matching
file immediately.
