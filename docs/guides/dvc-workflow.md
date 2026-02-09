# 📦 Data Version Control (DVC) Workflow

This project uses **DVC (Data Version Control)** to manage large datasets that cannot be stored in Git.
Git tracks the *code* and *DVC metadata files* (`.dvc`), while DVC tracks the actual *heavy data files*.

---

## 🚀 1. Setup & Installation

### Prerequisites
1.  **Git** installed and initialized.
2.  **Docker** installed and running.
3.  **DVC** installed on your host machine (not inside Docker).

```bash
# Install DVC (Windows/Mac/Linux)
pip install dvc

# Initialize DVC in the project root (Run only once)
dvc init
git commit -m "Initialize DVC"

```

---

## 🔄 2. The Ingestion Workflow

### Step A: Clean Slate (Optional)

If you want to start fresh or suspect corrupted data:

```bash
rm -rf data/bronze  # Delete old data

```

### Step B: Run the Ingestion Pipeline

Use Docker to safely download the raw data (e.g., BiciMAD CSVs/ZIPs).

```bash
docker-compose up --build

```

*Wait until the container logs: `🏁 Ingestion Finished.*`

### Step C: Track Data with DVC

Once data is in `data/bronze`, **DO NOT** use `git add`. Use DVC.

```bash
# 1. Stop tracking the folder in Git (if previously tracked)
git rm -r --cached data/bronze
git commit -m "Stop tracking raw data in Git"

# 2. Add the folder to DVC
dvc add data/bronze

```

**What this does:**

* Creates `data/bronze.dvc` (The "Receipt").
* Updates `data/.gitignore` (Tells Git to ignore the heavy files).
* Calculates hashes for version control.

### Step D: Save the State to Git

Commit the DVC metadata files to Git so the team can see the changes.

```bash
git add data/bronze.dvc data/.gitignore
git commit -m "feat: Update raw data (tracked by DVC)"
git push origin feature/ingest-bicimad

```

---

## 🛑 Common Commands & Troubleshooting

| Goal | Command |
| --- | --- |
| **Check Status** | `dvc status` |
| **Pull Data** (if remote configured) | `dvc pull` |
| **Reproduce Pipeline** | `dvc repro` |
| **Stop Tracking** | `dvc remove data/bronze.dvc` |

### ⚠️ Important Rules

1. **NEVER** `git add` large files (ZIP, CSV, Parquet) directly.
2. **ALWAYS** use `dvc add` for data directories.
3. **ALWAYS** commit the `.dvc` file to Git immediately after adding data.
