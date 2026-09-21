# Project 04: Neural Multi-Population Mortality
## *Beyond Linear Coherence with LSTM and Explainable AI (XAI)*

📄 **Paper**: [arXiv:2605.06438](https://arxiv.org/abs/2605.06438)

This repository contains the complete research pipeline for forecasting mortality rates across a high-longevity 6-country cluster (**Switzerland, Sweden, Norway, West Germany, Netherlands, and Japan**). The project challenges classical actuarial models (Lee-Carter, Li-Lee, CBD) by introducing a **Hierarchical LSTM** architecture capable of capturing non-linear trends and persistent structural shifts.

## 🎯 Research Objectives
- **Neural Innovation**: Implementing a Bayesian-optimized LSTM with **Monte Carlo Dropout (MCD)** for stochastic longevity forecasting.
- **Actuarial Benchmarking**: Direct comparison against **Li-Lee (2005)** and **CBD (2006)** models using a novel **Mean-Bias Correction (MBC)** anchor.
- **Explainability (XAI)**: Decompressing the "Black Box" via Temporal Saliency and **SHAP (SHapley Additive exPlanations)** for cross-country influence mapping.
- **Regulatory & Financial Utility**: Quantifying capital requirements (**SCR**) and pricing **Longevity Swaps** to meet **SST/Solvency II** standards.

## 🚀 Key Innovations & Results

### 1. Hybrid Benchmarking: The MBC Advantage
To resolve the integration drift typical of recursive neural networks, we implemented a **Mean-Bias Correction (MBC)**. This hybrid framework outperformed the Li-Lee "Gold Standard" in 67% of the cluster, achieving a **+17.40% RMSE improvement in Sweden** and **+12.57% in West Germany**, proving that neural-actuarial hybrids are superior for frontier populations with non-linear dynamics.

### 2. Stochastic Fan Charts (2020-2050)
Utilizing MC Dropout, the model generates 1,000 stochastic trajectories. Unlike the rigid linearity of Lee-Carter, the LSTM captures non-linear curvatures and cyclical "stalls" in mortality improvement, identifying a shared biological frontier.
![Stochastic Projection](reports/figures/fig09_kt_stochastic_forecast.png)

### 3. Longevity Convergence & Frontier Dynamics
The results confirm a **Catch-up Effect**: countries exhibit steeper improvement slopes converging toward a projected life expectancy ($e_0$) median of **~84.8 years** (CHE/JPN/SWE) by 2050.
![Convergence Map](reports/figures/fig13_final_convergence_map.png)

### 4. Regulatory Capital & Tail Risk (SCR)
The model provides a robust framework for calculating the **Solvency Capital Requirement (SCR)** under a dual uncertainty framework combining model uncertainty (MC Dropout) with process uncertainty calibrated on the Li-Lee benchmark. For Switzerland (SST), the model yields an ES 99.0\% SCR of **+1.153 years**, satisfying the requirements for internal model validation.
![Tail Risk Analysis](reports/figures/fig15_longevity_tail_risk.png)

### 5. Reverse Stress Test (SST)
Following the FINMA reverse stress test methodology, we invert the standard scenario analysis: instead of applying an arbitrary shock, we compute the critical mortality reduction $\delta^*$ that would exhaust the SCR buffer. For Switzerland, $\delta^* \approx 23.3\%$, meaning a permanent uniform reduction in mortality rates of this magnitude would fully consume the ES 99.0% solvency buffer. A standard 10% shock consumes only 42.8% of the buffer.

### 6. Financial Utility: Longevity Swap Pricing
By transforming mortality rates into discounted cash flows, the model prices a 30-year **Longevity Swap** (Cohort 65). The analysis reveals the distribution of Net Present Value (NPV), providing a superior basis for risk transfer compared to traditional deterministic models.
![Swap Pricing](reports/figures/fig17_longevity_swap_pricing.png)

### 7. XAI: SHAP Influence Mapping
Utilizing Game Theory-based **SHAP values**, the model provides a "Right to Explanation". Results for Switzerland reveal a structured influence hierarchy where **Norway's** regional proximity signal and **Switzerland's** own autoregressive dynamics jointly drive local mortality projections, with distributed contributions from the remaining European cluster.
![SHAP Influence Mapping](reports/figures/fig18_shap_influence_mapping.png)

### 8. Methodological Robustness: Window Sensitivity
To justify the choice of a 10-year lookback window, a sensitivity analysis was performed. Results confirm that while 15 years offer marginal gains, the 10-year window provides the optimal balance between capturing deep temporal dependencies (as shown by the non-zero importance at t-10 validating the full window depth) and maintaining statistical sample volume.
![Sensitivity Analysis](reports/figures/fig19_lookback_sensitivity.png)

## 🛠 Project Structure
- `data/`: Processed mortality assets, stationarity reports, and final actuarial summaries.
- `models/`: Serialized LSTM "Champion" models (.keras) and standardized scalers (.pkl).
- `notebooks/`: 
    - `01_data_extraction_and_eda.ipynb`: Data ingestion and professional EDA.
    - `02_actuarial_benchmarking.ipynb`: Implementation of LC, Li-Lee, and CBD.
    - `03_lstm_hierarchical_forecasting.ipynb`: Bayesian Tuning and Anti-Leakage Training.
    - `04_forecasting_xai_and_results.ipynb`: Recursive MCD projection and Life Table integration.
    - `05_actuarial_stress_testing_validation.ipynb`: Monotonicity, Lexis Maps, SHAP analysis, Reverse Stress Test, and **Lookback Sensitivity**.
    - `06_ablation_studies.ipynb`: Ablation studies quantifying the contribution of each design choice.
- `reports/figures/`: High-resolution visualizations (Viridis/Helvetica/300 DPI).
- `RESEARCH_NOTES.md`: Detailed methodological journal and mathematical proofs.
- `MODEL_PASSPORT.md`: Model governance report for regulatory and internal audit purposes.
- `requirements.txt`: Pinned Python dependencies for full reproducibility.

## 📊 Standards & Methodology
- **Cluster**: CHE, SWE, NOR, DEUTW, NLD, JPN (1956-2020).
- **Source**: Human Mortality Database (HMD).
- **Validation**: Out-of-sample testing (2012-2020), **Biological Monotonicity Audit**, and **Lookback Sensitivity Analysis**.
- **Governance**: Comprehensive [MODEL_PASSPORT.md] included for regulatory auditability and L&H Risk management.
- **XAI**: Concentrated mid-horizon temporal memory (peak at t-4) and SHAP-based feature importance mapping.
- **Financials**: 2% Risk-free rate; SST (Expected Shortfall) and Solvency II (VaR) standards.
- **Design**: Viridis color palette for perceptual uniformity; Helvetica typography for academic legibility.