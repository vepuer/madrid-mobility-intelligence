# Contributing to Madrid Mobility Intelligence

Thank you for your interest in this project! This document outlines the standards for contributing.

## 1. Branching Strategy (Git Flow)
We follow a strict branching model to ensure stability:

* **`main`**: Production-ready code. **Never push directly here.**
* **`develop`**: The integration branch. All features merge here first.
* **`feature/<name>`**: Workspace for new capabilities (e.g., `feature/data-pipeline`).
* **`fix/<name>`**: Workspace for bug fixes (e.g., `fix/csv-parser`).

## 2. Commit Messages (Conventional Commits)
We use the [Conventional Commits](https://www.conventionalcommits.org/) specification to keep our history readable.

**Format:** `<type>: <description>`

**Allowed Types:**
* **`feat`**: A new feature (e.g., `feat: add emt api client`)
* **`fix`**: A bug fix (e.g., `fix: handle null values in weather data`)
* **`docs`**: Documentation only changes (e.g., `docs: update readme`)
* **`chore`**: Maintenance tasks (e.g., `chore: update .gitignore`)
* **`refactor`**: Code change that neither fixes a bug nor adds a feature

## 3. Pull Requests (PR)
* PRs should be targeted to `develop`, not `main`.
* Ensure your code passes all unit tests before submitting.
* Describe your changes clearly in the PR description.