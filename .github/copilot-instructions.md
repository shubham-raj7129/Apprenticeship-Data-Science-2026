# Copilot Instructions for this Repository

This file documents the standing workflow rules for this repository. Any AI assistant (or human) making changes here should follow them.

## Repository visibility

- This repo must remain **private**. It contains personal coursework alongside course-provided materials (syllabi, rubrics, assignment PDFs) that are not to be published publicly.
- Never commit `.venv/` or `.env` — both are git-ignored and must stay that way. `.env` holds local secrets/tokens.

## Branching and PR workflow

- **Never commit or push directly to `main`.** Even as the sole contributor, all changes go through a feature branch and a pull request.
- Workflow for every change:
  1. Create a feature branch (e.g. `docs/...`, `feat/...`, `fix/...`).
  2. Commit the change(s) with a clear message.
  3. Push the branch.
  4. Open a pull request into `main`.
- When opening a PR:
  - Request a review from **Copilot** (`copilot-pull-request-reviewer[bot]`).
  - Set the **assignee** to the PR author (the repo owner).
- **Whenever new commits are pushed to an already-open PR, re-request a Copilot review** on that PR afterward.
- Merge only after review feedback has been addressed.
