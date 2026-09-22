# Project 02: Climate Risk Assessment - Extreme Value Theory (EVT)

This project applies Extreme Value Theory (EVT) to 44 years of ERA5 climate reanalysis data to assess flood risk and "Black Swan" precipitation events in the Zurich metropolitan area.

## Project Highlights
* Data Engineering: Developed a resilient Python pipeline to download and process ~385,000 hourly observations from the Copernicus CDS API, overcoming API payload constraints through sequential batch processing.
* Risk Assessment Insight: Demonstrated that transitioning from daily snapshots to hourly accumulation reveals a 43% underestimation of historical extreme events (37 mm vs 64.6 mm).
* Statistical Modeling: Fitted a Gumbel distribution (GEV Type I) to the Annual Maximum Series (AMS) to quantify tail risk.
* Actuarial Application: Estimated the 100-year return level at 75.2 mm, providing a statistically sound safety margin for Probable Maximum Loss (PML) calculations and solvency requirements.

## Project Structure
* data/: Processed summaries and final return level tables (raw .nc files are ignored via .gitignore).
* notebooks/: 01_Extreme_Value_Analysis.ipynb — The complete analytical workflow, from data loading to statistical validation.
* scripts/: download_zurich_hourly.py — The data acquisition engine.
* reports/figures/: Statistical visualizations including Return Level plots and Q-Q diagnostics.
* METHODOLOGY.md: Detailed technical white paper on the physical and statistical foundations of the project.
* requirements.txt: List of Python dependencies for environment reproducibility.

## How to Run

1. Setup Environment: It is recommended to use a virtual environment. Install all dependencies using: pip install -r requirements.txt
2. Data Acquisition: Run the acquisition script (requires a Copernicus CDS API key configured on your system): python scripts/download_zurich_hourly.py
3. Analysis: Open and run the Jupyter notebook to view the full statistical modeling and validation: jupyter notebook notebooks/01_Extreme_Value_Analysis.ipynb

---
Role: Actuarial Data Science Portfolio