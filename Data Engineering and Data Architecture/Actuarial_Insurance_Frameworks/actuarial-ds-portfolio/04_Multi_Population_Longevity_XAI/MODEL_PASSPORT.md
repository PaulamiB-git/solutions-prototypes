# Model Passport: Hierarchical LSTM Mortality Framework
**Version:** 1.0.0 (Pre-print Edition)  
**Status:** Validated & Audited  
**Owner:** Davide Rindori  
**Paper:** [arXiv:2605.06438](https://arxiv.org/abs/2605.06438)

## 1. Model Identity
- **Model Type:** Hybrid Neural-Actuarial (Hierarchical LSTM + Mean-Bias Correction).
- **Primary Use:** Longevity risk assessment, SCR calculation (SST/Solvency II), and Longevity Swap pricing.
- **Target Population:** High-longevity frontier cluster (CHE, SWE, NOR, DEUTW, NLD, JPN).

## 2. Methodology Snapshot
- **Architecture:** Stacked LSTM (32, 16 units) with fixed 20% Dropout and Bayesian Uncertainty (MC Dropout).
- **Stationarity Strategy:** First Differences ($\Delta K_t$) to neutralize linear drift.
- **Anchor Mechanism:** Mean-Bias Correction (MBC) to align neural variations with long-term actuarial trends.

## 3. Governance & Validation Verdicts
### A. Biological Consistency
- **Monotonicity Test:** PASS (Confirmed Gompertzian compliance for all six nations, ages 40-90).
- **Monotonicity FAIL (Youth):** None. All countries pass the monotonicity audit.

### B. Statistical Robustness
- **Out-of-Sample Performance:** +17.40% RMSE improvement over Li-Lee in Sweden.
- **Residual Analysis:** Lexis Map confirmed zero cohort-effect leakage.
- **XAI Audit:** SHAP analysis revealed a structured cross-country influence hierarchy for Swiss mortality, with Norway's regional proximity signal and distributed European dynamics as key drivers.

## 4. Risk & Capital Metrics (2050 Forecast)
- **Switzerland (CHE) SCR (ES 99.0%):** +1.153 years.
- **Japan (JPN) SCR (ES 99.0%):** +1.153 years.
- **Observation:** Risk convergence identified at the longevity frontier.

### Reverse Stress Test (SST Compliance)
- **Critical Shock Threshold ($\delta^*$):** 23.3% (Switzerland).
- **Interpretation:** A permanent, uniform reduction in mortality rates of 23.3% would exhaust the ES 99.0% solvency buffer.
- **Linearity Verification:** PASS (CV < 5% across 5%-20% shock range).
- **10% Shock Calibration:** Consumes 42.8% of the SCR buffer (+0.494 years out of +1.153 years).

## 5. Model Robustness & Sensitivity (Clean Run Audit)
- **Lookback Optimization**: Sensitivity analysis (Fig 19) revealed that RMSE decreases as the lookback window increases (5y: 7.09, 10y: 7.01, 15y: 6.85). 
- **Design Decision**: A 10-year lookback was selected as the standard. While a 15-year window offers marginal precision gains (+2.3% over 10y), it significantly reduces the available training sample size. The 10y window provides the optimal balance between capturing deep temporal dependencies and maintaining statistical volume for the 6-country cluster.
- **Inertia Analysis**: The model effectively filters short-term noise by leveraging a concentrated mid-horizon memory profile (peak at t-4), as confirmed by gradient-based temporal saliency analysis.