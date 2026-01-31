# Git & Project Workflow Cheat Sheet

## 1. Initial Setup (First Time Only)
These are the commands used to initialize the project `madrid-mobility-intelligence`.

### A. Cloning the Repository
Connects your local computer to the GitHub cloud repo.
```bash
# Go to your documents folder
cd ~/Documents

# Clone the repository
git clone [https://github.com/vepuer/madrid-mobility-intelligence.git](https://github.com/vepuer/madrid-mobility-intelligence.git)

# Enter the project folder
cd madrid-mobility-intelligence
```

### B. Creating Directory Structure & Tracking

We use `mkdir -p` to create folders. Since Git **ignores empty folders**, we must create a `.gitkeep` file inside them to ensure they are uploaded to GitHub.

```bash
# 1. Create directory structure
mkdir -p data/bronze data/silver data/gold
mkdir -p src/ingestion src/processing src/utils
mkdir -p docs/guides notebooks models tests

# 2. Add .gitkeep files (Required for Git to track empty folders)
touch data/bronze/.gitkeep data/silver/.gitkeep data/gold/.gitkeep
touch src/ingestion/.gitkeep src/processing/.gitkeep src/utils/.gitkeep
touch notebooks/.gitkeep models/.gitkeep tests/.gitkeep
```

### C. Security Configuration (.gitignore)

To prevent stealing of passwords, we configure Git to ignore the `.env` file.

1. Open `.gitignore`
2. Add the following line at the bottom:

```text
.env
```

## 2. Branching Strategy (Git Flow)

We follow a strict branching model to keep the code safe.

| Branch | Description |
| --- | --- |
| **`main`** | Production-ready code. **Never work directly here.** |
| **`develop`** | Integration branch. Combine your features here. |
| **`feature/...`** | Specific task workspace (e.g., `feature/data-ingestion`). |

### How to use branches:

```bash
# 1. Create and switch to the develop branch (First time only)
git checkout -b develop
git push -u origin develop

# 2. Start a new task (Create a feature branch from develop)
git checkout develop
git checkout -b feature/my-new-task

# 3. Check which branch you are on
git branch
```

## 3. Commit Message Conventions

We use **Conventional Commits** (`type: message`) to keep history clean.

* **`feat: ...`**  New feature (e.g., "feat: add AEMET connector")
* **`fix: ...`**  Bug fix (e.g., "fix: crash on missing .env")
* **`docs: ...`**  Documentation (e.g., "docs: update architecture guide")
* **`chore: ...`**  Maintenance (e.g., "chore: move folders")
* **`refactor: ...`**  Code cleanup (no logic change)

## 4. Daily Workflow

How to save your work every day using the branching strategy:

```bash
git status              # 1. Check what changed
git add .               # 2. Stage all changes
git commit -m "feat: description of work" # 3. Save snapshot
git push origin feature/my-new-task       # 4. Upload to GitHub
```

## 5. Useful Commands

* **`git pull`**: Download changes from the cloud.
* **`git log --oneline --graph`**: Show history of commits visually.
* **`git checkout -`**: Switch back to the previous branch.
