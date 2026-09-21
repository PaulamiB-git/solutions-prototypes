# Project 01: Motor Insurance Pricing - GLM vs. Machine Learning

This repository explores modern insurance pricing techniques using the French Motor Third-Party Liability (MTPL) dataset. The project compares traditional actuarial models with Machine Learning and Deep Learning approaches.

## 📖 Documentation
For a detailed breakdown of the actuarial framework, model governance (XAI), and mathematical foundations, please refer to our:
👉 **[Technical White Paper (METHODOLOGY.md)](METHODOLOGY.md)**

## 📊 Model Comparison & Results

The performance is measured using **Poisson Deviance** (lower is better).

| Model | Poisson Deviance | Improvement vs GLM | Key Characteristics |
| :--- | :--- | :--- | :--- |
| **GLM (Benchmark)** | 0.5923 | - | High interpretability, regulatory standard |
| **XGBoost** | 0.5646 | **+4.67%** | Captures non-linearities, superior performance |
| **Neural Network** | 0.3089* | N/A* | CANN architecture, high scalability |

*\*Note: Neural Network deviance is reported on a different scale/preprocessing setup but shows strong convergence after handling numerical stability via Batch Normalization.*

---

## 🛠️ Project Structure

The project is designed with a focus on **production-readiness** and **cross-platform compatibility** (optimized for both Apple Silicon and Intel architectures).

* `notebooks/`: 
    * `01_eda_and_modeling.ipynb`: Data exploration, GLM benchmark, and XGBoost training.
    * `02_neural_networks.ipynb`: Deep Learning implementation (CANN) using TensorFlow/Keras.
* `insurance_utils.py`: Modular utility library for data preprocessing and custom actuarial loss functions.
* `train_model.py`: Production-ready script to train and export the "Champion" XGBoost model.
* `requirements.txt`: Full dependency list for reproducibility.

---

## 🔍 Key Technical Highlights

* **Numerical Stability:** Implemented **Batch Normalization** and **Softplus** activation in Deep Learning to prevent gradient explosion and NaN issues.
* **Explainable AI (XAI):** Integrated **SHAP** values to interpret XGBoost predictions, ensuring the model remains "auditable" for actuarial purposes.
* **Actuarial Engineering:** Handled exposure clipping and claim frequency capping to align with standard insurance practices.
* **Production Oriented:** Separated research logic (Notebooks) from execution logic (Python scripts).

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt