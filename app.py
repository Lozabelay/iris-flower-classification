import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Iris Classification System",
    page_icon="🌸",
    layout="wide"
)

# -----------------------------
# LOAD MODELS
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "iris_models_bundle.pkl"

try:
    model_collection = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("Model file not found. Please train and save the models first.")
    st.stop()
except Exception as e:
    st.error(f"Unable to load models: {e}")
    st.stop()

# -----------------------------
# MODEL DESCRIPTIONS
# -----------------------------
descriptions = {
    "Logistic Regression": "A statistical classification algorithm that estimates the probability of each flower species.",
    "KNN": "Classifies a flower by looking at the nearest data points with similar measurements.",
    "Decision Tree": "Uses a sequence of decision rules to classify flower species.",
    "Random Forest": "Combines multiple decision trees to improve prediction performance.",
    "SVM": "Finds decision boundaries that separate different flower species.",
    "Naive Bayes": "Uses probability and Bayes' theorem to predict the most likely species.",
    "Gradient Boosting": "Builds models sequentially, with each model improving on previous errors.",
    "Extra Trees": "Combines randomized decision trees to make predictions.",
    "AdaBoost": "Combines several weak learners into a stronger classifier.",
    "LDA": "Finds combinations of features that best distinguish flower species."
}

# -----------------------------
# APPLICATION HEADER
# -----------------------------
st.title("🌸 Iris Flower Classification")
st.write(
    "An interactive machine-learning application "
    "that compares 10 classification algorithms."
)

st.divider()

# -----------------------------
# MODEL COMPARISON
# -----------------------------
st.header("📊 Model Performance")

comparison = pd.DataFrame([
    {
        "Model": name,
        "Accuracy": details["accuracy"]
    }
    for name, details in model_collection.items()
])

comparison = comparison.sort_values(
    by="Accuracy",
    ascending=False
)

comparison["Accuracy"] = comparison["Accuracy"].map(
    lambda x: f"{x:.2%}"
)

st.dataframe(comparison, use_container_width=True)

# -----------------------------
# MODEL SELECTION
# -----------------------------
st.divider()
st.header("🤖 Choose Your Machine Learning Model")

selected_model = st.selectbox(
    "Select a classification algorithm:",
    list(model_collection.keys())
)

selected_details = model_collection[selected_model]

st.subheader(selected_model)

st.write(descriptions[selected_model])

st.metric(
    label="Test Accuracy",
    value=f"{selected_details['accuracy']:.2%}"
)

# -----------------------------
# FLOWER MEASUREMENTS
# -----------------------------
st.divider()
st.header("🌷 Enter Flower Measurements")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.1,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.1,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with col2:
    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.1,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.1,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🔍 Predict Flower Species", use_container_width=True):

    input_data = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ]
    )

    model = selected_details["model"]

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Flower Species: {prediction}")

    st.balloons()