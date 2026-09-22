# Project 05: Actuarial-Informed Neural Networks
## *Constrained Deep Learning for Multi-Population Mortality Forecasting*

### Project Objective
To develop an alternative internal model for multi-population longevity forecasting that embeds actuarial domain knowledge directly into the neural network training process. This model serves as a **challenger** to both the Li-Lee benchmark and the unconstrained LSTM framework (Project 04), while satisfying the governance, robustness, and explainability requirements expected by regulators (FINMA/EIOPA) for internal model validation.

---

### Research Question
*Can physics-informed actuarial constraints embedded in the training loss improve neural mortality forecasting — particularly for near-linear populations where unconstrained LSTMs show no advantage — while preserving the model's ability to capture non-linear regime shifts?*

---

### The 5 Pillars of Research

#### 1. Constrained Loss Function (AINN Architecture)
Embed actuarial domain knowledge as soft constraints in the training loss:
$$\mathcal{L} = \mathcal{L}_{MSE} + \lambda_1 \mathcal{L}_{coherence} + \lambda_2 \mathcal{L}_{monotonicity}$$

- **Coherence penalty**: penalise divergence of country-specific factors from zero (Li-Lee assumption as a regulariser, not a hard constraint).
- **Monotonicity penalty**: penalise positive $\Delta K_t$ (temporal mortality worsening as a surrogate for Gompertzian compliance).
- **Stationarity penalty**: tested and excluded — inconsistent with data (4/6 countries violate stationarity).
- **Key finding**: constraints are neutral on RMSE (-0.009%) but serve as a governance instrument for regulatory defensibility.

#### 2. Credibility-Weighted Blending & MBC as Bayesian Shrinkage
- MBC formalised as a regularisation technique: the bias vector $\mathcal{B}$ introduces bias to reduce variance (integration drift).
- Connected to credibility theory: MBC weight $Z=1$ gives full credibility to neural signal, anchored to Li-Lee drift prior.
- Framed as Bayesian shrinkage toward the Li-Lee drift prior.

#### 3. Robustness & Validation (Regulatory Grade)
- **Multi-seed robustness**: 5-seed ensemble (CV = 1.06%, PASS).
- **Rolling-window validation**: 3 expanding windows (CV = 5.78%, PASS).
- **Residual-calibrated process noise**: walk-forward one-step-ahead residuals replace historical σ, eliminating double-counting (53-60% σ reduction).

#### 4. True Model-Based Stress Testing
- Mortality shock translated into the $\Delta K_t$ domain and injected into the sliding window.
- Recursive forecast re-executed with MC Dropout.
- **Result**: maximum amplification ratio 1.02× — STABLE. No explosive feedback.

#### 5. Regulatory Governance & Auditability
- Full Model Passport with validation verdicts (v2.0.0).
- Biological consistency audit (Gompertz monotonicity: STRUCTURALLY COMPLIANT).
- SHAP influence mapping for cross-country explainability.
- Reverse stress test and SCR calibration (SST/Solvency II).

---

### Positioning: Challenger Model Framework

| Criterion | Li-Lee (Benchmark) | Project 04 (LSTM+MBC) | Project 05 (AINN Ensemble) |
|:---|:---|:---|:---|
| Non-linear dynamics | ✗ | ✓ | ✓ |
| Coherence guarantee | ✓ (by construction) | ✗ (implicit) | ✓ (soft constraint) |
| Monotonicity | Not enforced | Post-hoc audit | Training-embedded |
| Sex-specific | ✗ (Total only) | ✗ (Total only) | ✓ (Joint M/F) |
| Uncertainty framework | Parametric (RWD) | Dual (MCD + process) | Dual (MCD + residual σ) |
| Model robustness | N/A | Single seed | 5-seed ensemble |
| Stress test | Level-shift | Level-shift | Model-based (ΔK_t injection) |

---

### Execution Phases
- [x] **Phase A**: Data reproduction and Li-Lee baseline (NB01-02).
- [x] **Phase B**: Constrained loss design, Optuna 6D joint optimisation, λ-sweep ablation (NB03).
- [x] **Phase C**: 5-seed ensemble training with model persistence (NB03).
- [x] **Phase D**: Residual-calibrated process noise, ensemble MC Dropout forecasting, MBC, life expectancy reconstruction (NB04).
- [x] **Phase E**: XAI (temporal saliency, SHAP), Gompertz audit, rolling-window validation (NB05).
- [x] **Phase F**: SCR (VaR/ES), reverse stress test, model-based stress test (NB06).
- [x] **Phase G**: Documentation consolidation (Model Passport v2.0, Research Notes, README).
- [x] **Phase H**: Constraint intensity experiment — governance-accuracy trade-off analysis (NB07).
- [ ] **Phase I**: Paper drafting and arXiv submission.
