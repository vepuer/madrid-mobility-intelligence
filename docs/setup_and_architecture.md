# Project Setup and Architecture Guide

## 1. Repository Initialization
This project is hosted on GitHub under the name `madrid-mobility-intelligence`.

**License:** MIT License.
* **Reason:** We chose this license to demonstrate that this is an open-source project, allowing others to view and learn from the code, which aligns with professional software engineering standards.

**Git Workflow used for setup:**
1.  Created repository on GitHub with `.gitignore` (Python) and `README.md`.
2.  Cloned to local machine:
    ```bash
    git clone [https://github.com/vepuer/madrid-mobility-intelligence.git](https://github.com/vepuer/madrid-mobility-intelligence.git)
    ```

## 2. Directory Structure (Medallion Architecture)
The project follows a strict folder hierarchy to separate raw data, processed data, and source code.

```text
madrid-mobility-intelligence/
├── .github/                   <-- GitHub Actions (CI/CD)
├── data/
│   ├── bronze/                <-- Raw Data (JSON/CSV/ZIP) - Immutable
│   ├── silver/                <-- Cleaned Data (Parquet/CSV) - Deduplicated
│   └── gold/                  <-- Aggregated Data - Ready for ML/Dashboard
├── docs/                      <-- Project Documentation
│   ├── architecture.md        <-- Project Memory & Data Flow
│   ├── dev_log.md             <-- Development Diary (Changelog)
│   └── guides/                <-- Technical Manuals (Git, Docker)
├── models/                    <-- Trained ML Models (.pkl)
├── notebooks/                 <-- Jupyter Notebooks for experiments
├── src/                       <-- Source Code
│   ├── ingestion/             <-- Scripts: Internet -> Bronze
│   ├── processing/            <-- Scripts: Bronze -> Silver -> Gold
│   └── utils/                 <-- Shared helper functions
├── tests/                     <-- Unit Tests
├── .env                       <-- API Keys (IGNORED by Git)
├── .gitignore                 <-- Files to exclude from Git
├── docker-compose.yml         <-- Container orchestration
├── Dockerfile                 <-- Container definition
├── README.md                  <-- Main Project Presentation
└── requirements.txt           <-- Python Dependencies

```

## 3. Data Flow Strategy

* **Bronze Layer:** Raw inputs from BiciMAD (historical JSON/CSV) and EMT/AEMET (Real-time APIs). We treat this data as immutable (read-only).
* **Silver Layer:** Data is cleaned. We cast data types (e.g., string to datetime), handle null values, and remove duplicates.
* **Gold Layer:** Business-level aggregates. Features are engineered here for the ML model (e.g., "Rain intensity vs Bus delays" or "Bike usage by neighborhood").

```

