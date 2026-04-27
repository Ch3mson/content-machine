# Workflows

Use this directory as the action index for agents.

| Workflow | File | Trigger | Output |
| --- | --- | --- | --- |
| Workflow A | `workflow-a-new-account.md` | New account or account onboarding | Account source-of-truth files. |
| Workflow B | `workflow-b-new-post.md` | New slideshow for an existing account | Post folder with flow, sourced images, script, and processed slides. |
| Workflow C | `workflow-c-image-processing.md` | Process/render slideshow images | Final `processed/slide_N.png` files. |

Routing lives in `../AGENTS.md`. If a user tags a workflow, start the matching
file immediately.
