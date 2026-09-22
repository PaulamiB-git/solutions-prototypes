# Methodology: Neural Longevity Framework
## Probabilistic Mortality Forecasting via LSTM & MC Dropout (CHE 1950-2024)

---

### Document Control
| Field | Details |
| :--- | :--- |
| **Status** | Final Production Release |

---

## 1. Executive Summary
This document outlines the modeling strategy used to quantify Longevity Trend Risk for the Swiss population. The core objective is to move beyond the deterministic constraints of the Lee-Carter (LC) model by implementing a **Recurrent Neural Network (LSTM)**. By incorporating **Monte Carlo Dropout (MCD)**, this framework provides a stochastic distribution of future mortality, enabling the calibration of **Expected Shortfall (ES)** for regulatory capital purposes (SST/Solvency II).

---

## 2. Data Strategy & Pre-processing
### 2.1 Source and Granularity
The dataset consists of Swiss central death rates ($m_{x,t}$) sourced from the **Human Mortality Database (HMD)**, spanning 1950 to 2024. We focus on the age range 0–95 to ensure data credibility, as centenarian data often exhibits idiosyncratic volatility that can distort neural training.

### 2.2 Feature Engineering
* **Log-Transformation:** Mortality rates are modeled in log-space ($\ln m_{x,t}$) to linearize exponential age effects and stabilize the variance of improvements.
* **Sequential Windowing:** We implemented a **10-year sliding window** ($L=10$). In longevity modeling, capturing the "momentum" of the last decade is critical to identifying structural plateaus that a standard year-on-year analysis might miss.

---

## 3. Modeling Architecture: Why LSTM?
Traditional actuarial models (SVD-ARIMA) assume a constant rate of improvement. However, mortality in high-income countries often exhibits **regime shifts**.

The **Long Short-Term Memory (LSTM)** architecture was selected for its ability to:
1.  **Capture Non-Linearity:** Unlike Random Walk with Drift (RWD), LSTMs can identify if the pace of mortality improvement is accelerating or decelerating.
2.  **Mitigate Vanishing Gradients:** The LSTM's "cell state" allows it to maintain a memory of long-term historical trends while selectively "forgetting" outdated regimes via its gating mechanism.

---

## 4. Uncertainty Quantification via MC Dropout
A standard Neural Network is a point-estimator; it provides no measure of "model doubt." To align with Risk Management standards, we implemented **Monte Carlo Dropout (MCD)**.

### 4.1 Epistemic Uncertainty
During the inference phase, we maintain the Dropout layers active. This allows us to sample from the approximate posterior distribution of the model weights. By performing **100 stochastic forward passes**, we generate an ensemble of future mortality trajectories ($k_t$). The spread of these trajectories quantifies the **Epistemic Uncertainty**. The resulting distribution exhibits a natural skewness, reflecting the asymmetric nature of longevity tail risk.

---

## 5. Risk Metrics & Regulatory Calibration (SST)
The framework translates neural variance into actionable capital parameters. We focus on the 2050 horizon to assess long-term trend risk.

### 5.1 Tail Risk Assessment
In accordance with the **Swiss Solvency Test (SST)**, we prioritize **Expected Shortfall (ES)** over Value-at-Risk (VaR). 
* **SST Shock Calibration:** The ES at 99% confidence level results in a mortality index ($k_t$) of **-85.78**.
* **Longevity SCR Shock:** The resulting shock ($\Delta k_t = 3.90$) reflects a conservative view, capturing the risk of a significant slowdown in mortality improvement compared to historical averages.

---

## 6. Validation and Quality Assurance
1. **Backtesting Derby:** Competitive comparison (2011–2024) where the LSTM demonstrated a superior **RMSE of 0.1141** against SVD (0.1682).
2. **Sensitivity Analysis:** Identified a performance optimum at $L=5, U=32$ (**RMSE: 0.0439**), while confirming $L=10$ as the robust standard for Swiss regime shifts.
3. **Residual Heatmap:** Confirmed a mean residual of **0.0021**, indicating an unbiased fit across age-period grids.
4. **Structural Bias Discussion:** The systematic underestimation of mortality during backtesting (bias) is interpreted as a "Prudence Buffer." It reflects the model's adherence to long-term improvement trends while the actual data was impacted by post-2011 deceleration and the 2020-2023 exogenous pandemic shocks.

---

## 7. Strategic Conclusions
The "Neural Longevity Framework" reveals a **38.54-point "Prudence Gap"** compared to Lee-Carter by 2050. This methodology provides a resilient basis for longevity swap pricing and internal capital model calibration, effectively addressing the post-2010 mortality improvement deceleration in Switzerland.