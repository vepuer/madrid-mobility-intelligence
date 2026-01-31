# madrid-mobility-intelligence
End-to-end Data Engineering &amp; ML project analyzing Madrid mobility (BiciMAD, EMT) vs. Weather (AEMET). Features: Medallion Architecture, Docker, and Predictive Modeling.
# Madrid Mobility Intelligence 🚲🌦️

**End-to-end MLOps project analyzing the relationship between weather and urban mobility in Madrid.**

## 🎯 Objective
This project correlates usage data from **BiciMAD** (public electric bikes) and **EMT** (buses) with meteorological data from **AEMET** to predict demand and analyze mobility patterns under different weather conditions.

## 💾 Data Sources (Input Data)
We use the following public datasets:

| Source | Type | Description | Link |
|--------|------|-------------|------|
| **BiciMAD** | Historical | Usage data (stations, trip duration, timestamp). | [Open Data Madrid](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=54e76af6a185a910VgnVCM200000f921e388RCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default&idValorado=54e76af6a185a910VgnVCM200000f921e388RCRD&action=addValoracion&puntuacion=4) |
| **EMT** | API | Real-time bus status and station info. | [MobilityLabs](https://mobilitylabs.emtmadrid.es/) |
| **AEMET** | API | Historical and forecast weather data (rain, temp). | [AEMET OpenData](https://opendata.aemet.es/) |

## 🏗️ Architecture
We follow a **Medallion Architecture** (Bronze $\to$ Silver $\to$ Gold) to ensure data quality.
* See [Architecture Guide](docs/setup_and_architecture.md) for full technical details.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Infrastructure:** Docker, Git
* **Data Engineering:** Pandas, Requests (APIs)
* **ML:** Scikit-Learn (Planned for Q2)