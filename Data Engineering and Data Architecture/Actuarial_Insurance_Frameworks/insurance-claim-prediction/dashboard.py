import os
import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Insurance Claim Prediction & Risk Analysis",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# FILE PATH
# ============================================================

MODEL_PATH = "models/insurance_claim_model.pkl"
DATA_PATH = "data/insurance_claims.csv"

MODEL_COMPARISON_PATH = (
    "outputs/model_comparison.csv"
)

FEATURE_IMPORTANCE_PATH = (
    "outputs/feature_importance.csv"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 25px;
    }

    .risk-low {
        background-color: #d1fae5;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #065f46;
    }

    .risk-medium {
        background-color: #fef3c7;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #92400e;
    }

    .risk-high {
        background-color: #fee2e2;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #991b1b;
    }

    .info-box {
        background-color: #f3f4f6;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD MODEL
# ============================================================

if not os.path.exists(MODEL_PATH):

    st.error(
        "Model belum ditemukan."
    )

    st.info(
        "Jalankan terlebih dahulu: "
        "python train_model.py"
    )

    st.stop()


model_package = joblib.load(
    MODEL_PATH
)

model = model_package["model"]

model_name = model_package["model_name"]


# ============================================================
# LOAD DATA
# ============================================================

if os.path.exists(DATA_PATH):

    df = pd.read_csv(
        DATA_PATH
    )

else:

    df = None


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🛡️ Insurance Claim Prediction'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Insurance Claim Prediction '
    '& Risk Analysis System'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(
    "🛡️ Insurance AI"
)

st.sidebar.markdown(
    "### Navigation"
)

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Overview",
        "🔮 Claim Prediction",
        "📊 Risk Analysis",
        "🤖 Model Performance",
        "📁 Dataset"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    f"Model digunakan: {model_name}"
)


# ============================================================
# OVERVIEW
# ============================================================

if page == "🏠 Overview":

    st.header(
        "🏠 Project Overview"
    )

    st.write(
        """
        Sistem ini menggunakan Machine Learning untuk memprediksi
        kemungkinan terjadinya insurance claim dan melakukan
        risk analysis terhadap customer.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # KPI
    # --------------------------------------------------------

    if df is not None:

        total_customers = len(
            df
        )

        total_claims = int(
            df["Claim"].sum()
        )

        claim_rate = (
            total_claims
            /
            total_customers
            *
            100
        )

        total_claim_amount = (
            df["Claim_Amount"].sum()
        )

        average_claim = (
            df.loc[
                df["Claim"] == 1,
                "Claim_Amount"
            ].mean()
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Customers",
            f"{total_customers:,}"
        )

        col2.metric(
            "Total Claims",
            f"{total_claims:,}"
        )

        col3.metric(
            "Claim Rate",
            f"{claim_rate:.2f}%"
        )

        col4.metric(
            "Total Claim Amount",
            f"Rp {total_claim_amount:,.0f}"
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Claim Distribution"
            )

            claim_chart = pd.DataFrame({

                "Status": [
                    "No Claim",
                    "Claim"
                ],

                "Customers": [
                    int(
                        (
                            df["Claim"] == 0
                        ).sum()
                    ),

                    int(
                        (
                            df["Claim"] == 1
                        ).sum()
                    )
                ]

            })

            st.bar_chart(
                claim_chart.set_index(
                    "Status"
                )
            )

        with col2:

            st.subheader(
                "Average Claim Amount"
            )

            if pd.notna(
                average_claim
            ):

                st.metric(
                    "Average Claim",
                    f"Rp {average_claim:,.0f}"
                )

            else:

                st.metric(
                    "Average Claim",
                    "Rp 0"
                )

            st.write(
                """
                Average claim amount dihitung dari
                customer yang memiliki claim.
                """
            )

    st.divider()

    st.subheader(
        "Machine Learning Workflow"
    )

    workflow = pd.DataFrame({

        "Stage": [
            "1. Dataset",
            "2. Data Cleaning",
            "3. Feature Engineering",
            "4. Model Training",
            "5. Model Evaluation",
            "6. Risk Analysis",
            "7. Prediction"
        ],

        "Description": [
            "Insurance customer data",
            "Remove duplicates & validate data",
            "Prepare numerical & categorical features",
            "Logistic Regression & Random Forest",
            "Accuracy, Precision, Recall, F1, ROC AUC",
            "Calculate claim probability & risk level",
            "Predict individual customer"
        ]

    })

    st.dataframe(
        workflow,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CLAIM PREDICTION
# ============================================================

elif page == "🔮 Claim Prediction":

    st.header(
        "🔮 Insurance Claim Prediction"
    )

    st.write(
        "Masukkan data customer untuk melakukan prediction."
    )

    st.divider()

    # --------------------------------------------------------
    # CUSTOMER
    # --------------------------------------------------------

    st.subheader(
        "Customer Information"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.number_input(
            "Age",
            18,
            70,
            30
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

    with col3:

        annual_income = st.number_input(
            "Annual Income (IDR)",
            25000000,
            250000000,
            75000000,
            step=5000000
        )


    # --------------------------------------------------------
    # POLICY
    # --------------------------------------------------------

    st.subheader(
        "Policy Information"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        policy_type = st.selectbox(
            "Policy Type",
            [
                "Basic",
                "Standard",
                "Premium"
            ]
        )

    with col2:

        policy_tenure = st.number_input(
            "Policy Tenure",
            1,
            10,
            3
        )

    with col3:

        premium_amount = st.number_input(
            "Premium Amount (IDR)",
            1000000,
            15000000,
            5000000,
            step=500000
        )


    # --------------------------------------------------------
    # VEHICLE
    # --------------------------------------------------------

    st.subheader(
        "Vehicle Information"
    )

    col1, col2 = st.columns(2)

    with col1:

        vehicle_type = st.selectbox(
            "Vehicle Type",
            [
                "Sedan",
                "SUV",
                "Hatchback",
                "Pickup",
                "Motorcycle"
            ]
        )

    with col2:

        vehicle_age = st.number_input(
            "Vehicle Age",
            0,
            15,
            5
        )


    # --------------------------------------------------------
    # CLAIM HISTORY
    # --------------------------------------------------------

    st.subheader(
        "Claim History"
    )

    col1, col2 = st.columns(2)

    with col1:

        previous_claims = st.number_input(
            "Previous Claims",
            0,
            6,
            1
        )

    with col2:

        accident_history = st.selectbox(
            "Accident History",
            [
                "Yes",
                "No"
            ]
        )


    # --------------------------------------------------------
    # DRIVING
    # --------------------------------------------------------

    st.subheader(
        "Driving Behavior"
    )

    col1, col2 = st.columns(2)

    with col1:

        annual_mileage = st.number_input(
            "Annual Mileage (km)",
            3000,
            50000,
            15000,
            step=1000
        )

    with col2:

        traffic_violations = st.number_input(
            "Traffic Violations",
            0,
            7,
            1
        )


    # --------------------------------------------------------
    # OCCUPATION
    # --------------------------------------------------------

    occupation = st.selectbox(
        "Occupation",
        [
            "Office Worker",
            "Business Owner",
            "Student",
            "Driver",
            "Engineer",
            "Teacher"
        ]
    )


    st.divider()


    # --------------------------------------------------------
    # PREDICT
    # --------------------------------------------------------

    if st.button(
        "🔮 PREDICT CLAIM",
        use_container_width=True
    ):

        input_data = pd.DataFrame({

            "Age": [age],

            "Gender": [gender],

            "Annual_Income": [annual_income],

            "Policy_Type": [policy_type],

            "Policy_Tenure": [policy_tenure],

            "Premium_Amount": [premium_amount],

            "Vehicle_Type": [vehicle_type],

            "Vehicle_Age": [vehicle_age],

            "Previous_Claims": [previous_claims],

            "Accident_History": [accident_history],

            "Annual_Mileage": [annual_mileage],

            "Traffic_Violations": [traffic_violations],

            "Occupation": [occupation]

        })


        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

        claim_probability = (
            probability * 100
        )


        # ----------------------------------------------------
        # RISK
        # ----------------------------------------------------

        if claim_probability < 30:

            risk_level = "LOW"

            css_class = "risk-low"

            recommendation = (
                "Risiko klaim rendah. "
                "Customer dapat dipertimbangkan "
                "dengan monitoring standar."
            )

        elif claim_probability < 70:

            risk_level = "MEDIUM"

            css_class = "risk-medium"

            recommendation = (
                "Risiko klaim sedang. "
                "Disarankan dilakukan review "
                "tambahan sebelum approval."
            )

        else:

            risk_level = "HIGH"

            css_class = "risk-high"

            recommendation = (
                "Risiko klaim tinggi. "
                "Disarankan dilakukan risk assessment "
                "lebih mendalam."
            )


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.divider()

        st.subheader(
            "Prediction Result"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            if prediction == 1:

                st.metric(
                    "Claim Prediction",
                    "YES"
                )

            else:

                st.metric(
                    "Claim Prediction",
                    "NO"
                )

        with col2:

            st.metric(
                "Claim Probability",
                f"{claim_probability:.2f}%"
            )

        with col3:

            st.metric(
                "Risk Score",
                f"{claim_probability:.2f}"
            )


        st.markdown(
            f"""
            <div class="{css_class}">
                RISK LEVEL: {risk_level}
            </div>
            """,
            unsafe_allow_html=True
        )


        st.subheader(
            "Recommendation"
        )

        st.info(
            recommendation
        )


        # ----------------------------------------------------
        # DOWNLOAD
        # ----------------------------------------------------

        result = input_data.copy()

        result["Prediction"] = (
            "YES"
            if prediction == 1
            else "NO"
        )

        result["Claim_Probability"] = (
            claim_probability
        )

        result["Risk_Score"] = (
            claim_probability
        )

        result["Risk_Level"] = (
            risk_level
        )

        csv_data = result.to_csv(
            index=False
        )

        st.download_button(

            label="⬇️ Download Prediction Result",

            data=csv_data,

            file_name="insurance_prediction.csv",

            mime="text/csv",

            use_container_width=True

        )


# ============================================================
# RISK ANALYSIS
# ============================================================

elif page == "📊 Risk Analysis":

    st.header(
        "📊 Risk Analysis"
    )

    if df is None:

        st.error(
            "Dataset tidak ditemukan."
        )

        st.stop()


    # --------------------------------------------------------
    # CALCULATE PROBABILITY
    # --------------------------------------------------------

    features = df.drop(
        columns=[
            "Customer_ID",
            "Claim",
            "Claim_Amount"
        ]
    )

    probabilities = model.predict_proba(
        features
    )[:, 1]

    analysis_df = df.copy()

    analysis_df["Claim_Probability"] = (
        probabilities * 100
    ).round(2)


    # --------------------------------------------------------
    # RISK LEVEL
    # --------------------------------------------------------

    def risk_category(
        probability
    ):

        if probability < 30:

            return "LOW"

        elif probability < 70:

            return "MEDIUM"

        return "HIGH"


    analysis_df["Risk_Level"] = (
        analysis_df[
            "Claim_Probability"
        ]
        .apply(risk_category)
    )


    # --------------------------------------------------------
    # KPI
    # --------------------------------------------------------

    total_customers = len(
        analysis_df
    )

    total_claims = int(
        analysis_df["Claim"].sum()
    )

    claim_rate = (
        total_claims
        /
        total_customers
        *
        100
    )

    high_risk = int(
        (
            analysis_df["Risk_Level"]
            == "HIGH"
        ).sum()
    )

    medium_risk = int(
        (
            analysis_df["Risk_Level"]
            == "MEDIUM"
        ).sum()
    )

    low_risk = int(
        (
            analysis_df["Risk_Level"]
            == "LOW"
        ).sum()
    )


    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "Claims",
        f"{total_claims:,}"
    )

    col3.metric(
        "Claim Rate",
        f"{claim_rate:.2f}%"
    )

    col4.metric(
        "High Risk",
        f"{high_risk:,}"
    )


    st.divider()


    # --------------------------------------------------------
    # RISK CHART
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Risk Distribution"
        )

        risk_counts = pd.DataFrame({

            "Risk Level": [
                "LOW",
                "MEDIUM",
                "HIGH"
            ],

            "Customers": [
                low_risk,
                medium_risk,
                high_risk
            ]

        })

        st.bar_chart(
            risk_counts.set_index(
                "Risk Level"
            )
        )


    with col2:

        st.subheader(
            "Claim Distribution"
        )

        claim_counts = pd.DataFrame({

            "Status": [
                "No Claim",
                "Claim"
            ],

            "Customers": [
                int(
                    (
                        analysis_df["Claim"]
                        == 0
                    ).sum()
                ),

                int(
                    (
                        analysis_df["Claim"]
                        == 1
                    ).sum()
                )

            ]

        })

        st.bar_chart(
            claim_counts.set_index(
                "Status"
            )
        )


    st.divider()


    # --------------------------------------------------------
    # RISK FILTER
    # --------------------------------------------------------

    st.subheader(
        "Customer Risk Explorer"
    )

    selected_risk = st.selectbox(
        "Filter Risk Level",
        [
            "ALL",
            "LOW",
            "MEDIUM",
            "HIGH"
        ]
    )


    if selected_risk == "ALL":

        filtered = analysis_df

    else:

        filtered = analysis_df[
            analysis_df["Risk_Level"]
            == selected_risk
        ]


    filtered = filtered.sort_values(
        "Claim_Probability",
        ascending=False
    )


    st.dataframe(
        filtered,
        use_container_width=True,
        height=500
    )


    csv_data = filtered.to_csv(
        index=False
    )


    st.download_button(

        "⬇️ Download Risk Analysis",

        csv_data,

        "risk_analysis.csv",

        "text/csv",

        use_container_width=True

    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

elif page == "🤖 Model Performance":

    st.header(
        "🤖 Model Performance"
    )

    st.write(
        f"Selected Model: **{model_name}**"
    )


    # --------------------------------------------------------
    # MODEL COMPARISON
    # --------------------------------------------------------

    if os.path.exists(
        MODEL_COMPARISON_PATH
    ):

        comparison = pd.read_csv(
            MODEL_COMPARISON_PATH
        )

        st.subheader(
            "Model Comparison"
        )

        st.dataframe(
            comparison,
            use_container_width=True,
            hide_index=True
        )


        st.bar_chart(
            comparison.set_index(
                "Model"
            )[[
                "Accuracy",
                "Precision",
                "Recall",
                "F1 Score",
                "ROC AUC"
            ]]
        )


    # --------------------------------------------------------
    # CONFUSION MATRIX
    # --------------------------------------------------------

    confusion_path = (
        "outputs/confusion_matrix.png"
    )

    if os.path.exists(
        confusion_path
    ):

        st.subheader(
            "Confusion Matrix"
        )

        st.image(
            confusion_path,
            use_container_width=True
        )


    # --------------------------------------------------------
    # FEATURE IMPORTANCE
    # --------------------------------------------------------

    if os.path.exists(
        FEATURE_IMPORTANCE_PATH
    ):

        importance = pd.read_csv(
            FEATURE_IMPORTANCE_PATH
        )

        st.subheader(
            "Top Risk Factors"
        )

        top_features = (
            importance
            .head(15)
            .sort_values(
                "Importance"
            )
        )

        fig, ax = plt.subplots(
            figsize=(10, 7)
        )

        ax.barh(
            top_features["Feature"],
            top_features["Importance"]
        )

        ax.set_xlabel(
            "Importance"
        )

        ax.set_ylabel(
            "Feature"
        )

        ax.set_title(
            "Top 15 Insurance Risk Factors"
        )

        st.pyplot(
            fig
        )

        plt.close(fig)


# ============================================================
# DATASET
# ============================================================

elif page == "📁 Dataset":

    st.header(
        "📁 Insurance Dataset"
    )

    if df is None:

        st.error(
            "Dataset tidak ditemukan."
        )

        st.stop()


    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Rows",
        f"{len(df):,}"
    )

    col2.metric(
        "Columns",
        len(df.columns)
    )

    col3.metric(
        "Claims",
        int(df["Claim"].sum())
    )

    col4.metric(
        "No Claims",
        int(
            (
                df["Claim"] == 0
            ).sum()
        )
    )


    st.divider()


    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )


    st.subheader(
        "Statistical Summary"
    )

    st.dataframe(
        df.describe(),
        use_container_width=True
    )


    csv_data = df.to_csv(
        index=False
    )

    st.download_button(

        "⬇️ Download Dataset",

        csv_data,

        "insurance_claims.csv",

        "text/csv",

        use_container_width=True

    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Insurance Claim Prediction & Risk Analysis | "
    "Machine Learning Project"
)