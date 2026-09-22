# Solutions & Prototypes

A working portfolio of end-to-end **data engineering**, **actuarial modelling**, and **applied ML** projects across the insurance and healthcare domains — from cloud lakehouse pipelines to regulatory-grade longevity models.

---

## What's Inside

| Project | Domain | Core Stack |
|---|---|---|
| [Actuarial_Insurance_Frameworks](./Actuarial_Insurance_Frameworks) | Actuarial science & quantitative risk | Python, TensorFlow/Keras, XGBoost, Optuna, SHAP |
| [Snowflake-ELT-Pipeline-with-dbt-and-Airflow](./Snowflake-ELT-Pipeline-with-dbt-and-Airflow) | Modern data stack ELT | Snowflake, dbt, Airflow (Astronomer/Cosmos) |
| [Azure-data-engineering-project](./Azure-data-engineering-project) | Multi-source cloud pipeline | ADF, Databricks, ADLS Gen2, Synapse, MongoDB, MySQL |
| [Databricks-end-to-end-data-pipeline...](./Databricks-end-to-end-data-pipeline-with-medallion-architecture-project) | Lakehouse & dimensional modelling | Databricks, Delta Lake, Unity Catalog, Structured Streaming |
| [Microsoft-Azure-Medallion-Data-pipeline](./Microsoft-Azure-Medallion-Data-pipeline) | On-prem → cloud migration | SQL Server, ADF, Databricks, Synapse, Key Vault, Power BI |
| [Insurance-claim-prediction](./Insurance-claim-prediction) | Insurance risk scoring | scikit-learn, Streamlit |
| [Medical-Insurance-Cost-Prediction](./Medical-Insurance-Cost-Prediction) | Health cost modelling | pandas, scikit-learn, Tableau |
| [Disease-Risk-Analysis-with-Machine-Learning](./Disease-Risk-Analysis-with-Machine-Learning) | Clinical risk classification | scikit-learn, KMeans, DBSCAN |
| [Healthcare_Frameworks](./Healthcare_Frameworks) | Clinical ML (11 notebooks) | PyTorch, PySpark MLlib, scikit-learn |

---

## Highlights

### Actuarial & Quantitative Risk

Five research-grade projects bridging actuarial theory with modern ML, built for regulatory applicability under **Swiss Solvency Test (SST)** and **Solvency II**:

- **Motor Pricing & Interpretability** — Frequency-severity study on ~670,000 French MTPL policies. XGBoost achieves a Poisson deviance of 0.5646, a **4.67% improvement over the GLM benchmark**, with TreeSHAP decomposition for regulatory auditability.
- **Climate Risk (EVT)** — Extreme Value Theory on 44 years of ERA5 reanalysis data (~385,000 hourly observations). Moving from daily to hourly granularity revealed a **43% underestimation** of historical extremes; 100-year return level estimated at 75.2 mm.
- **Stochastic Mortality Modelling** — LSTM framework with MC Dropout for Swiss mortality (HMD, 1950–2024). Outperforms SVD benchmarks (RMSE 0.1141 vs. 0.1682) and quantifies a **38.54-point prudence gap** against Lee-Carter linear drift.
- **Multi-Population Longevity + XAI** — Hierarchical LSTM across a 6-country high-longevity cluster, beating Li-Lee in 67% of the cluster (**+17.40% RMSE in Sweden**). Paper on [arXiv:2605.06438](https://arxiv.org/abs/2605.06438).
- **Actuarial-Informed Neural Networks** — Constrained loss embedding Li-Lee coherence and monotonicity penalties directly in training, with 6D Optuna optimisation and a 5-seed ensemble that **reduces confidence intervals by ~55%**.

Each project ships with a Model Passport, research notes, and SCR calibration under VaR/ES.

### Data Engineering

- **Medallion architecture, three ways** — Bronze/Silver/Gold implementations across Azure Databricks (retail), ADF + Synapse (e-commerce), and an on-prem SQL Server migration — covering incremental loading, idempotent processing, Spark Structured Streaming, CDC, and **SCD Type 1 & Type 2** dimensional modelling.
- **Production patterns, not toy pipelines** — Unity Catalog governance, Lakeflow data-quality expectations, Azure Key Vault + AAD service principals and RBAC, and deliberately multi-source ingestion (relational + NoSQL) to mirror real enterprise topology.
- **Modern data stack ELT** — Snowflake + dbt + Airflow pipeline with staging/marts separation, reusable macros, and both generic and singular dbt tests, containerised and orchestrated via Astronomer.

### Applied ML — Insurance & Healthcare

- **Insurance claim prediction** — End-to-end claim probability model with customer risk tiering (Low/Medium/High) served through an interactive Streamlit decision-support dashboard.
- **Disease risk analysis** — Full data-mining pipeline (KNN imputation, DBSCAN/Isolation Forest/LOF outlier handling, grid-searched models) reaching **99% accuracy**, cross-validated against unsupervised cluster structure.
- **Healthcare frameworks** — Eleven clinical ML notebooks spanning breast cancer classification, COVID-19 chest X-ray detection (PyTorch), DNA sequence classification, diabetes prediction (PySpark MLlib and MLP), coronary artery disease diagnosis, heart failure EDA, and drug-safety hypothesis testing.

---

## Repository Layout

```
Actuarial_Insurance_Frameworks/          5 actuarial research projects (01–05)
Azure-data-engineering-project/          Olist e-commerce pipeline on Azure
Databricks-end-to-end-data-pipeline.../  Retail lakehouse with SCD & streaming
Microsoft-Azure-Medallion-Data-pipeline/ On-prem SQL → Azure migration
Snowflake-ELT-Pipeline-with-dbt-and-Airflow/
Insurance-claim-prediction/              Streamlit app + models
Medical-Insurance-Cost-Prediction/       Notebooks, reports, Tableau dashboard
Disease-Risk-Analysis-with-Machine-Learning/
Healthcare_Frameworks/                   11 clinical ML notebooks
src/, inference.py, train.ipynb          Computer vision prototype (Faster R-CNN)
```

Each project directory has its own README with architecture diagrams, methodology, and results.

---

## Tech Stack

**Cloud & Platforms** — Azure (Data Factory, Databricks, ADLS Gen2, Synapse, Key Vault, AAD), Snowflake
**Engineering** — PySpark, Delta Lake, dbt, Apache Airflow, SQL, MongoDB, MySQL, Docker
**ML & Modelling** — TensorFlow/Keras, PyTorch, scikit-learn, XGBoost, Optuna, SHAP, PySpark MLlib
**Analytics & BI** — Power BI, Tableau, Microsoft Fabric, Streamlit

---

## License

MIT — see [Permissions.txt](./Permissions.txt).

> These projects are prototypes built for research and portfolio purposes. Models are not validated for production underwriting, pricing, or clinical decision-making.
