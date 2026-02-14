
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


## Week 2: Data Ingestion & Version Control (Feb 2026)

**Goal:** Implement scalable data ingestion and establish Data Version Control (DVC).

### 📅 2026-02-09

* **Containerization (Docker):**
    * Created `Dockerfile` (Python 3.9 Slim) and `docker-compose.yml` to isolate the ingestion environment.
    * Implemented volume mapping to save downloaded data directly to the host machine.


* **Data Ingestion (BiciMAD):**
    * Developed `src/ingestion/ingest_bicimad.py` to automate downloading historical data.
    * Implemented a **smart scraper** that detects available years (2017–2023) and downloads ZIP files automatically.
    * Successfully ingested **~4GB** of raw data into `data/bronze`.


* **Data Version Control (DVC):**
    * Initialized DVC to handle large binary files (preventing Git bloat).
    * Configured **Hybrid Versioning Strategy**:
    * **Git:** Tracks code, DVC metadata (`.dvc`), and documentation.
    * **DVC:** Tracks the actual `data/bronze` directory.

Here is the updated section for your `dev_log.md`. You can copy and paste this block directly at the bottom of your file, under the **Week 2** section.

I have summarized the Docker fixes, the successful API connection, and the specific data endpoints we verified today.

---

### 📅 2026-02-14

* **Infrastructure Refactor (Docker):**
* Refactored `docker-compose.yml` to correctly map local volumes (`src/`, `notebooks/`).
* Enabled "Hot-Reloading": Changes in local code are now immediately reflected in the container without rebuilding.


* **API Integration (EMT MobilityLabs):**
* **Authentication:** Fixed header protocols (`accessToken`) and successfully established connection.
* **Bus Data:** Verified `v2/transport/busemtmad/stops/{id}/arrives/` endpoint. Successfully extracted Real-Time GPS, incident status, and arrival estimates.
* **BiciMAD Data:** Verified `v1/transport/bicimad/stations/` endpoint. Confirmed access to real-time bike availability (`dock_bikes`) for intermodal analysis.
* **Topology:** Investigated `lines/info` endpoint. Confirmed it provides Line Metadata (Head/Tail/Length) but requires calculating frequency from real-time data.


* **Data Strategy:**
* Defined the **"Weather vs. Mobility"** correlation model.
* Selected specific features for the future ingestion pipeline: Precipitation (Weather), `dock_bikes` (BiciMAD), and `estimateArrive` (EMT).

