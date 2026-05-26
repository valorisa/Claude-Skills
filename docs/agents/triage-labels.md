# Triage Labels

| Canonical role | GitHub label | Description |
|----------------|--------------|-------------|
| needs-triage | `needs-triage` | Maintainer needs to evaluate |
| needs-info | `needs-info` | Waiting on reporter response |
| ready-for-agent | `ready-for-agent` | Fully specified, AFK agent can pick up |
| ready-for-human | `ready-for-human` | Needs human implementation |
| wontfix | `wontfix` | This will not be worked on |

## Usage

The `triage` skill (if adopted) will apply these labels as it moves issues through the state machine.

Skills like `create-github-issues` can apply `ready-for-agent` to issues that are fully specified.
