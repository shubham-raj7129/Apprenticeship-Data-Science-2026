# Data Science 2026 — Apprenticeship Coursework

Personal coursework repository for the Data Science apprenticeship program (Purdue Global), covering machine learning, deep learning, and foundational data science coursework. This is a **private** repo kept for personal archival/reference — contents include course materials (syllabi, rubrics, readings) alongside my own assignments, discussion posts, and notebooks.

> **Note:** This repository contains course-provided materials (PDFs, rubrics, syllabi) that are the property of Purdue Global / course instructors, included here for personal reference only. It is kept private for that reason — please do not redistribute course materials from this repo.

## Structure

| Folder | Description |
| --- | --- |
| [`Orientation/`](./Orientation) | Program orientation materials (syllabus, Dropbox basics, time management resources). |
| [`IN 501/`](./IN%20501) | IN501 coursework — assignments, seminar slides/PDFs, and assignment rubrics, organized by unit. |
| [`IN404_MachineLearning/`](./IN404_MachineLearning) | IN404 (Machine Learning) coursework — per-unit folders (`Unit 1`–`Unit 4`+), plus shared `Docs/` and `Rubrics/`. Subfolder names vary by unit (e.g., `Discussion/`, `Seminar/`, and either `Assignment/` or `Assignments/`); see each unit for its exact layout. |
| [`IN 403 - Deep Learning/`](./IN%20403%20-%20Deep%20Learning) | IN403 (Deep Learning) coursework — per-unit folders (`Unit 1`–`Unit 10`) with notebooks (`.ipynb`), presentations, and lab datasets. Most units use `Assignment/` and `Discussion/` subfolders, but a few units (e.g., `Unit 2`, `Unit 3`) keep assignment/discussion material as files directly in the unit root instead. |
| [`data/`](./data) | Shared datasets used across notebooks (e.g., MNIST). |
| `requirements_backup.txt` / `requirements_no_tf.txt` | Snapshots of the Python environment's installed packages (with and without TensorFlow) for reproducing the local `.venv`. |

Unit folders generally include some combination of the following, but exact names and whether content lives in a subfolder or directly at the unit root **vary by unit** — browse each unit to confirm its layout:

- `Overview.txt` / `Reading.txt` — unit overview and reading notes.
- `Assignment/` or `Assignments/` (or assignment files at the unit root) — assignment notebooks/write-ups and related datasets.
- `Discussion/` (or discussion files at the unit root) — discussion board posts and responses.
- `Seminar/` — seminar slides, recording notes, or related PDFs.

## Environment Setup

This project uses Python 3.14 via a local virtual environment (not tracked in git).

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_backup.txt   # or requirements_no_tf.txt to skip TensorFlow
```

## Notes

- `.venv/` and `.env` are git-ignored — the environment is rebuilt locally from the requirements files above, and `.env` holds local secrets/tokens that are never committed.
- Large binary course materials (PDFs, PPTX, images) are kept for personal reference alongside code; notebooks (`.ipynb`) contain the actual analysis/model work for each assignment.
