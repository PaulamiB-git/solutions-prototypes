# Project 05: Actuarial-Informed Neural Networks
## *Constrained Deep Learning for Multi-Population Mortality Forecasting*

This project develops an alternative internal model for multi-population longevity forecasting that embeds actuarial domain knowledge directly into the neural network training process. It serves as a **challenger model** to both the Li-Lee benchmark and the unconstrained LSTM framework ([Project 04](../04_Multi_Population_Longevity_XAI)), satisfying the governance, robustness, and explainability requirements expected by regulators (FINMA/EIOPA) for internal model validation.

## Research Question
*Can physics-informed actuarial constraints embedded in the training loss improve neural mortality forecasting — particularly for near-linear populations where unconstrained LSTMs show no advantage — while preserving the model's ability to capture non-linear regime shifts?*

## Key Innovations

### 1. Constrained Loss Function (AINN)
Actuarial constraints embedded as differentiable penalties during training:
- **Coherence**: soft penalty on divergence of country-specific factors (Li-Lee assumption as regulariser).
- **Monotonicity**: temporal mortality improvement enforced during training (mortality should improve over time in developed countries).
- **Stationarity**: tested and excluded — inconsistent with data (4/6 countries violate stationarity).

### 2. Joint Male/Female Training
A single model trained on Male and Female mortality jointly, with a binary sex indicator as input feature. This doubles the effective sample size (90 training samples vs 45) and produces coherent sex-specific forecasts.

### 3. Joint Bayesian Optimisation via Optuna (6D)
Architecture (units, learning rate), temporal context (lookback window), and actuarial constraints (λ values) are optimised simultaneously in a single 100-trial joint search using Optuna's TPE sampler. This is methodologically superior to sequential tuning and reveals that the optimal constraint weight is architecture-dependent.

**Champion**: LSTM (48-32 units), lookback=15, lr=0.001, λ_coherence=0.001, λ_monotonicity=0.001.
**RMSE**: 6.1725 (overall), 5.72 (Male), 6.59 (Female). Multi-seed CV: 1.06% (PASS).
**Runtime**: 48 minutes on Apple M1 Pro.

### 4. 5-Seed Ensemble with Residual-Calibrated Process Noise
Instead of relying on a single model, 5 independently trained models (one per seed) are averaged for forecasting. Process noise σ is calibrated on the model's walk-forward residuals — not on historical Li-Lee variability — to avoid double-counting the uncertainty the LSTM already captures. This reduces 95% CI width by ~55% and produces SCR estimates in the +1.3–2.6 year range, consistent with the dual uncertainty framework.

### 5. Regulatory-Grade Robustness
- Multi-seed robustness (CV = 1.06%, PASS). Seed 77 replaces original Seed 123 (premature convergence outlier).
- Lookback sensitivity analysis.
- Rolling-window validation (CV = 5.78%, PASS).
- Gompertz monotonicity audit (structurally compliant).
- Temporal saliency and SHAP influence mapping.

### 6. Stress Test & SCR
- **SCR (ES 99.0%)**: +1.907 years (CHE Male), +1.516 years (CHE Female).
- **Reverse stress test**: δ* = 23.0% (CHE Male), 25.2% (CHE Female) — critical shock threshold under SST.
- **Model-based stress test**: STABLE (amplification ratio 1.02×, no explosive feedback).

## Project Structure
- `data/`: Mortality data assets (HMD, same cluster as Project 04).
- `models/`: Serialized AINN ensemble models (5 seeds) and scalers.
- `notebooks/`:
    - `01_data_and_baseline.ipynb`: Data loading, EDA, log-mortality matrices. ✓
    - `02_actuarial_benchmarking.ipynb`: Li-Lee sex-specific, stationarity analysis. ✓
    - `03_training_ablation_lambda.ipynb`: Joint Bayesian Optimisation (Optuna 6D), 5-seed ensemble training, ablation studies. ✓
    - `04_stochastic_forecasting.ipynb`: Residual-calibrated process noise, 5-seed ensemble MC Dropout, MBC, observation-anchored e₀ with Gompertz isotonic correction. Includes cross-project comparison (P04 vs P05) and multi-step constraint effect analysis. ✓
    - `05_xai_validation.ipynb`: Temporal saliency, SHAP, Gompertz audit, rolling-window. ✓
    - `06_stress_test_scr.ipynb`: SCR (VaR/ES), reverse stress test, model-based stress test. ✓
    - `07_constraint_intensity_experiment.ipynb`: Governance-accuracy trade-off analysis across 5 λ levels. ✓
    - `08_ainn_vs_lilee_benchmark.ipynb`: Quantitative benchmark — AINN ensemble vs Li-Lee RWD (e₀, CI, SCR). ✓
    - `09_backtest_10yr_hindcast.ipynb`: Out-of-sample 10-year backtest (train 1956-2010, validate 2011-2020). ✓
- `src/`: Modular source code (custom losses, reproducibility, styling).
- `reports/figures/`: High-resolution visualizations.
- `latex/`: Paper source files.
- `RESEARCH_NOTES.md`: Methodological journal.
- `ROADMAP.md`: Research plan and execution phases.
- `MODEL_PASSPORT.md`: Governance report for regulatory audit.
- `requirements.txt`: Pinned dependencies.

## Standards & Methodology
- **Cluster**: CHE, SWE, NOR, DEUTW, NLD, JPN (1956-2020).
- **Source**: Human Mortality Database (HMD).
- **Benchmarks**: Li-Lee (2005), Project 04 LSTM+MBC.
- **Validation**: Rolling-window, multi-seed, biological monotonicity audit.
- **Governance**: Model Passport, SHAP, Lexis Maps, Reverse Stress Test.
- **Financials**: SST (Expected Shortfall) and Solvency II (VaR) standards.
- **Design**: Viridis colour palette; Helvetica typography.

## Status
Pipeline complete (Notebooks 01-09). Ensemble with residual-calibrated process noise integrated into main pipeline. Next: paper drafting.
