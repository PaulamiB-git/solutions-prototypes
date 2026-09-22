# Methodology: Extreme Precipitation & Flood Risk Analysis
## Climate Risk Assessment for the Zurich Region (1980-2023)

## 1. Executive Summary
This project implements an **Extreme Value Theory (EVT)** framework to estimate the return periods of catastrophic precipitation events in Zurich. While standard actuarial models focus on average claims, climate risk management requires modeling the "tail" of the distribution—events that occur once every 50 or 100 years (Tail Risk).

## 2. Data Strategy & Engineering

### 2.1 Data Source
Data is sourced from the **ERA5 Reanalysis** dataset produced by the **ECMWF** (European Centre for Medium-Range Weather Forecasts) and accessed via the Copernicus Climate Data Store (CDS).

### 2.2 Challenges in Data Granularity
Initial exploratory analysis using daily snapshots (sampled at 12:00 UTC) revealed a significant underestimation of extreme events. In the context of flood risk, an instantaneous measurement is insufficient as it fails to capture the cumulative volume of water delivered by a storm system over 24 hours.

### 2.3 Batch Processing & API Optimization
To ensure scientific rigor, the project transitioned to **hourly resolution data**. To overcome the "Cost Limit" restrictions of the CDS-Beta API, a **sequential batch processing system** was implemented:
* **Granularity:** Hourly (24 observations per day).
* **Time Range:** 1980 – 2023 (44 years).
* **Engineering Solution:** A Python-based automation script requested data in 1-year chunks to bypass payload constraints and handle potential API timeouts.
* **Volume:** ~385,000 hourly observations for the Zurich metropolitan area.

## 3. Physical & Actuarial Pre-processing

### 3.1 Daily Accumulation (Hydrological Consistency)
Precipitation is a flux variable. To align with hydrological and insurance risk standards, we performed a temporal aggregation:
$$P_{daily} = \sum_{h=1}^{24} P_{hourly}$$
This step is critical: only by summing all 24 hourly steps can we identify the true **Annual Maximum Series (AMS)**, which serves as the fundamental input for the EVT models.

### 3.2 Unit Normalization
ERA5 precipitation is provided in meters (m). For the analysis, values were converted to **millimeters (mm)**, the standard unit for rainfall intensity in meteorological reporting and insurance NatCat modeling.

## 4. Statistical Framework: Extreme Value Theory (EVT)

To model the probability of "Black Swan" events, we utilize the **Generalized Extreme Value (GEV)** distribution.

### 4.1 The Block Maxima Approach
Following the Fisher-Tippett-Gnedenko theorem, we extract the maximum daily accumulation for each year. These values are fitted to a **Gumbel distribution** (GEV Type I), assuming a shape parameter $\xi = 0$.

### 4.2 Return Period Estimation
The model calculates the **Return Level** $z_T$ for a given return period $T$ (e.g., 100 years) using the inverse of the Cumulative Distribution Function (CDF):
$$P(X \leq z_T) = 1 - \frac{1}{T}$$

## 5. Model Validation & Final Results

### 5.1 Statistical Robustness (Goodness-of-Fit)
The model's validity was confirmed through formal testing:
* **Kolmogorov-Smirnov Test:** P-value of **0.992**, confirming the Gumbel distribution is an excellent fit for Zurich's precipitation extremes.
* **Q-Q Plot Analysis:** The alignment between empirical and theoretical quantiles validates the model's reliability, with a slight conservative margin in the upper tail.

### 5.2 The "Value of Data" Insight
A comparison between different data granularities revealed that:
* **Daily Snapshots** (Naive approach) underestimated the maximum rainfall record by **~43%** (37 mm vs 64.6 mm).
* This proves that high-resolution data engineering is non-negotiable for accurate Catastrophe Modeling.

### 5.3 Zurich Return Levels (1980-2023)
The Gumbel model yielded the following estimated return levels:

| Return Period | Estimated Daily Rainfall (mm) |
|---------------|-------------------------------|
| 2 Years       | 40.2 mm                       |
| 10 Years      | 55.8 mm                       |
| 50 Years      | 69.4 mm                       |
| 100 Years     | **75.2 mm** |

The maximum recorded event (64.6 mm in July 1996) corresponds to an empirical return period of approximately 30-40 years. The 100-year estimate provides the necessary safety margin for solvency requirements.

## 6. Actuarial Implications for Swiss Re
From a NatCat perspective, this analysis provides fundamental inputs for:
* **PML (Probable Maximum Loss) Estimation:** Quantifying the "1-in-100" event to define capital reserves.
* **Pricing Accuracy:** Mitigating premium leakage by capturing true cumulative rainfall intensity.
* **Climate Resilience:** Assessing the frequency of tail events in the context of increasing volatility.

---
**Project:** Actuarial Data Science Portfolio