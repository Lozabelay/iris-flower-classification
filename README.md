# 🌸 Iris Flower Classification System

An interactive Machine Learning application that classifies Iris flowers into three species using 10 different classification algorithms.

The application allows users to compare model performance, select their preferred algorithm, enter flower measurements, and receive predictions through a Streamlit interface.

## 🚀 Project Overview

This project demonstrates a complete beginner-to-intermediate Machine Learning workflow, from data exploration and preprocessing to model training, evaluation, and deployment.

### 🎯 Objectives

- Explore and understand the Iris dataset.
- Perform Exploratory Data Analysis (EDA).
- Prepare data for machine learning.
- Train and compare 10 classification models.
- Evaluate model performance.
- Build an interactive prediction application using Streamlit.

## 📊 Dataset

The project uses the Iris dataset, containing 150 flower observations.

It includes four numerical features:

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal in centimeters |
| Sepal Width | Width of the sepal in centimeters |
| Petal Length | Length of the petal in centimeters |
| Petal Width | Width of the petal in centimeters |

### Target Classes

The system predicts one of three Iris species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

## 🤖 Machine Learning Models

The project implements and compares 10 classification algorithms:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree
4. Random Forest
5. Support Vector Machine (SVM)
6. Gaussian Naive Bayes
7. Gradient Boosting
8. Extra Trees
9. AdaBoost
10. Linear Discriminant Analysis (LDA)

Each model is evaluated using a held-out test dataset.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## 📁 Project Structure

```text
flower/
│
├── data/
│   └── IRIS(1).xls
│
├── notebooks/
│   └── iris_analysis.ipynb
│
├── src/
│
├── models/
│   └── iris_models_bundle.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate into the project

```bash
cd flower
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the environment

On Linux:

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 Application Features

- Compare the performance of 10 machine learning models.
- View model descriptions and test accuracy.
- Select a classification algorithm.
- Enter four flower measurements.
- Predict the flower species interactively.

## 📈 Model Evaluation

Models are evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Cross-validation

Accuracy displayed in the application represents performance on the project's held-out test dataset. It does not guarantee the same performance on unseen real-world data.

## 🔮 Future Improvements

- Add interactive prediction probability charts.
- Improve the dashboard design.
- Add more evaluation metrics.
- Perform hyperparameter optimization.
- Experiment with additional classification algorithms.
- Deploy the application online.
- Add an API for external application integration.

## 👨‍💻 Author

Developed as a Machine Learning classification project.

---

**Project:** Iris Flower Classification System  
**Category:** Machine Learning / Classification  
**Interface:** Streamlit