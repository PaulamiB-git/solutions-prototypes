# Actuarial Data Science Portfolio

---

This repository collects five research projects at the intersection of Actuarial Science, Machine Learning, and Quantitative Risk Management. I build quantitative risk models for Life, P&C, and Climate, bridging actuarial theory with modern ML. Each project addresses a distinct domain — P&C Pricing, NatCat Climate Risk, Single-Population Longevity, Multi-Population Longevity, and Constrained Neural Forecasting — with a consistent emphasis on statistical rigour, model governance, and regulatory applicability under Swiss Solvency Test (SST) and Solvency II frameworks.

---

## Project Index

### 5 · [Actuarial-Informed Neural Networks](./05_Actuarial_Informed_Neural_Networks)

**Domain:** Multi-Population Longevity · Constrained Deep Learning · Credibility Theory · Regulatory Validation

A challenger internal model that embeds actuarial domain knowledge directly into the neural network training process. Produces sex-specific (M/F) longevity projections for a 6-country cluster, with full regulatory compliance (SCR, stress tests, XAI).

- **Constrained Loss (AINN):** Differentiable penalties for Li-Lee coherence and temporal monotonicity — enforced during training.
- **Joint Male/Female Training:** Single model with sex indicator, doubling the effective sample size and producing coherent M/F projections.
- **Optuna 6D Joint Optimisation:** Architecture, lookback, and constraints optimised simultaneously (100 trials). Champion: LSTM (48-32), lb=15, RMSE=6.17.
- **5-Seed Ensemble with Residual-Calibrated σ:** Process noise calibrated on walk-forward model residuals (not historical variability) to avoid double-counting. 5 independently trained models averaged for robustness. CI reduced by ~55%.
- **Stochastic Forecasting (2020–2050):** Observation-anchored projections with dual uncertainty (MC Dropout + residual-calibrated process noise). CHE Male: 80.3→82.1, CHE Female: 83.6→85.4.
- **Regulatory Capital:** SCR (ES 99.0%) = +1.907 years (CHE Male), +1.516 years (CHE Female). Reverse stress test: δ* = 23.0% (Male), 25.2% (Female).
- **Model Stability:** Model-based stress test confirms STABLE behaviour (amplification ratio 1.02×).
- **Documentation:** Includes [Model Passport](./05_Actuarial_Informed_Neural_Networks/MODEL_PASSPORT.md) and [Research Notes](./05_Actuarial_Informed_Neural_Networks/RESEARCH_NOTES.md).

---

### 4 · [Neural Multi-Population Mortality: Beyond Linear Coherence](./04_Multi_Population_Longevity_XAI)

**Domain:** Global Longevity Risk · Hierarchical LSTM · Dual Uncertainty · XAI (SHAP) · Model Governance

A complete research pipeline for forecasting mortality across a high-longevity 6-country cluster (CHE, SWE, NOR, DEUTW, NLD, JPN). The project challenges classical actuarial models — Lee-Carter, Li-Lee (2005), and CBD (2006) — by introducing a Bayesian-optimised Hierarchical LSTM with a dual uncertainty framework that jointly captures epistemic and process risk.

- **Hybrid Benchmarking (MBC):** A Mean-Bias Correction anchor resolves the integration drift inherent in recursive neural forecasting. The LSTM+MBC framework outperforms Li-Lee in 67% of the cluster, achieving **+17.40% RMSE improvement in Sweden** and **+12.57% in West Germany**.
- **Dual Uncertainty Framework:** Combines MC Dropout (model/epistemic uncertainty) with Li-Lee calibrated process noise (aleatoric/process uncertainty) within the same 1,000 stochastic trajectories. This produces realistic confidence intervals of **±0.9 years** (95% CI) for life expectancy projections — a material upgrade from epistemic-only estimates.
- **Stochastic Projections (2020–2050):** Projected median life expectancy converges toward ~84.8 years for CHE, JPN, and SWE, with West Germany exhibiting the steepest catch-up trajectory (+3.45 years).
- **Regulatory Capital:** Under the dual uncertainty framework, SCR calibration yields **+1.153 years** (ES 99.0%, SST) and **+1.116 years** (VaR 99.5%, Solvency II) for Switzerland, with an actuarial Risk Margin of **±0.879 years**. West Germany carries the highest tail risk (+1.320 years ES) due to catch-up volatility.
- **Reverse Stress Test (SST):** Following FINMA methodology, the critical mortality reduction that exhausts the ES 99.0% solvency buffer is quantified at **δ* = 23.3%** for Switzerland. A standard 10% shock consumes 42.8% of the buffer.
- **Ablation Studies:** Systematic decomposition of design choices confirms that First Differences contribute **+48.6%** and MBC contributes **+18.6%** to out-of-sample accuracy, validating the hybrid architecture.
- **Longevity Swap Pricing:** Stochastic mortality trajectories are translated into discounted cash flows for a 30-year Longevity Swap (Cohort 65).
- **Explainability (XAI):** SHAP influence mapping decomposes the "Black Box", revealing that Norway's regional proximity signal and Switzerland's autoregressive dynamics jointly drive local mortality projections.
- **Documentation:** Includes a comprehensive [Model Passport](./04_Multi_Population_Longevity_XAI/MODEL_PASSPORT.md), detailed [Research Notes](./04_Multi_Population_Longevity_XAI/RESEARCH_NOTES.md), and a [Roadmap](./04_Multi_Population_Longevity_XAI/ROADMAP.md). Paper available on [arXiv:2605.06438](https://arxiv.org/abs/2605.06438).

---

### 3 · [Stochastic Longevity Forecasting: A Neural Approach to SST](./03_Stochastic_Mortality_Modeling)

**Domain:** Life & Health Reinsurance · Deep Learning · Swiss Solvency Test (SST)

An LSTM-based framework for Swiss mortality (HMD, 1950–2024) that quantifies Longevity Trend Risk through probabilistic inference. The model transitions beyond the deterministic constraints of Lee-Carter by incorporating Monte Carlo Dropout for epistemic uncertainty quantification.

- **Model Selection:** Out-of-sample backtesting (2011–2024) confirms LSTM superiority over SVD-based benchmarks (RMSE 0.1141 vs. 0.1682), with effective adaptation to the post-2010 mortality improvement plateau.
- **Prudence Gap:** A **38.54-point divergence** between LSTM median and Lee-Carter trend by 2050 quantifies the Model Risk of relying on linear drift assumptions in a decelerating regime.
- **SST Calibration:** Expected Shortfall (ES 99%) yields a **Longevity SCR Shock of 3.90**, calibrated for FINMA regulatory capital requirements.
- **Documentation:** [LaTeX source](./03_Stochastic_Mortality_Modeling/latex/).

---

### 2 · [Zurich Extreme Precipitation Analysis (EVT)](./02_Climate_Risk_EVT)

**Domain:** Climate Risk · Extreme Value Theory · Big Data Engineering

An Extreme Value Theory framework applied to 44 years of ERA5 hourly reanalysis data (ECMWF / Copernicus CDS) for the Zurich metropolitan area. The project quantifies tail risk for catastrophic precipitation events, providing inputs for PML estimation and solvency assessments.

- **Data Engineering:** A resilient Python pipeline processes **~385,000 hourly observations** (1980–2023), overcoming CDS API payload constraints through sequential batch processing.
- **Granularity Insight:** Transitioning from daily snapshots to hourly accumulation reveals a **43% underestimation** of historical extreme events (37 mm vs. 64.6 mm), demonstrating that high-resolution data engineering is non-negotiable for accurate Catastrophe Modelling.
- **Statistical Modelling:** Gumbel distribution (GEV Type I) fitted to the Annual Maximum Series, validated by a Kolmogorov-Smirnov p-value of **0.992**.
- **100-Year Return Level:** Estimated at **75.2 mm** daily rainfall, providing the necessary safety margin for NatCat reserving and capital adequacy.

---

### 1 · [Motor Pricing & Actuarial Interpretability](./01_Motor_Pricing_Interpretability)

**Domain:** P&C Pricing · Gradient Boosting (XGBoost) · Explainable AI (XAI)

A frequency-severity pricing study on the French MTPL dataset (~670,000 policies), benchmarking GLM, XGBoost, and CANN (Combined Actuarial Neural Network) architectures.

- **Champion Model:** XGBoost achieves a Poisson Deviance of **0.5646**, a **4.67% improvement** over the GLM benchmark (0.5923).
- **Explainability (SHAP):** TreeSHAP decomposes non-linear risk factor interactions — notably the sharp acceleration of young-driver risk above a vehicle power threshold — ensuring regulatory auditability under Solvency II.
- **Neural Baseline (CANN):** A hybrid GLM-Neural architecture demonstrates strong convergence, establishing a foundation for future deep learning pricing iterations.
- **Documentation:** Includes a detailed [Technical White Paper](./01_Motor_Pricing_Interpretability/METHODOLOGY.md) covering mathematical foundations, model governance, and Shapley value theory.

---

## Skills & Tools

| Category | Detail |
| :--- | :--- |
| **Actuarial** | Stochastic Longevity Modelling (Single & Multi-Population), SCR Calibration (VaR / ES), EVT, GLM, Frequency-Severity Pricing, Longevity Swap Valuation |
| **Machine Learning** | LSTM (Hierarchical, MC Dropout), Actuarial-Informed Neural Networks (PINN-style), XGBoost, CANN, Bayesian Hyperparameter Optimisation, SHAP / XAI |
| **Engineering** | Python (TensorFlow/Keras, Scikit-learn, Pandas, xarray, SciPy), Git, LaTeX, SQL |
| **Regulatory** | Swiss Solvency Test (SST), Solvency II, Model Risk Management, Internal Model Governance, Reverse Stress Testing |

---


