# Multi-stage deploy demo

This repository demonstrates the canonical GitHub Actions pattern for one PR, one build, and a single promotion pipeline that advances the same artifact through the environment chain: dev -> qa -> stg -> prd.

## Flow

1. A pull request is opened and merged into `main`.
2. The `promote` workflow runs once from `main`.
3. The same artifact is validated and then approved at each GitHub environment gate.
4. A stage-specific environment branch is updated to the exact commit SHA after the prior environment has passed its gate.

## Required GitHub setup

- Create a branch protection rule for `main` requiring PRs and status checks.
- Create GitHub environments named `dev`, `qa`, `stg`, and `prd`.
- Turn on environment protection rules with required reviewers for each environment.
- Ensure the repository has permissions for `contents: write` and `deployments: write`.

## Files in this repo

- `.github/workflows/promote.yml` contains the promotion pipeline.
- `scripts/promotion.py` defines the allowed environment stages and ordering.
- `tests/test_promotion.py` validates the stage flow.

## Local validation

```bash
python -m unittest discover -s tests -v
```
