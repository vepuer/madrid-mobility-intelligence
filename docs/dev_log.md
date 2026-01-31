
# Development Log (Changelog)

## Week 1: Project Setup & Architecture (Jan 2026)
**Goal:** Initialize repository, define architecture, and secure data access.

### 📅 2026-01-31
* **Repository Initialization:**
    * Created `madrid-mobility-intelligence` on GitHub (Public, MIT License).
    * Cloned to local environment.
* **Architecture Design:**
    * Defined **Medallion Architecture** (Bronze/Silver/Gold) for data layers.
    * Created folder structure: `data/`, `src/`, `notebooks/`, `docs/`.
* **Security:**
    * Created `.env` file for credentials.
    * Configured `.gitignore` to prevent secret leakage.
* **Documentation:**
    * Created `setup_and_architecture.md` with file tree and data flow.
    * Created `git_cheat_sheet.md` for internal reference.
* **Data Access:**
    * Registered app on **EMT MobilityLabs** (Status: *Pending Review*).
    * Identified AEMET and BiciMAD data sources.
* **Workflow & Standards:**
    * Established **Git Flow** strategy (Main $\to$ Develop $\to$ Feature).
    * Created `CONTRIBUTING.md` with guidelines for commits and PRs.
    * Performed initial commit to `main` and initialized `develop` branch.

### 🚧 Current Blockers
* Waiting for EMT MobilityLabs API keys approval.