# Credit Risk Modeling - End-to-End Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red.svg)](https://streamlit.io)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7.6-green.svg)](https://xgboost.ai)

## 🎯 Project Overview

This project provides a comprehensive **Credit Risk Assessment System** powered by machine learning. It evaluates borrowers' default risk, calculates credit scores, and assigns credit ratings using an advanced XGBoost model with hyperparameter optimization.

### 🌟 Key Features

- **Interactive Web Interface**: User-friendly Streamlit application for real-time risk assessment
- **Advanced ML Model**: XGBoost with Optuna hyperparameter tuning achieving 98% AUC
- **Comprehensive Risk Metrics**: Default probability, credit score, and rating classification
- **Model Interpretability**: SHAP and LIME integration for explainable AI
- **Production Ready**: Complete deployment pipeline with proper error handling

### 📊 Model Performance

- **AUC Score**: 0.98
- **Gini Coefficient**: 0.97
- **KS Statistic**: 86.87%
- **Model Type**: XGBoost with under-sampling and hyperparameter optimization

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/credit-risk-modeling.git
cd credit-risk-modeling
```

2. **Create virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r project-root/requirements.txt
```

4. **Run the application**
```bash
cd project-root
streamlit run main.py
```

5. **Open your browser**
Navigate to `http://localhost:8501` to access the application.

## 📁 Project Structure

```
Credit-Risk-Modeling-End-to-End-Project/
│
├── project-root/                    # Main application directory
│   ├── main.py                     # Streamlit application
│   ├── utils.py                    # Utility functions and model logic
│   ├── requirements.txt            # Python dependencies
│   └── model/                      # Model files
│       ├── model_data.pkl          # Trained model and scaler
│       └── tuned_hyperparameters.txt
│
├── images/                         # Project images and visualizations
│   ├── Feature importance.png
│
├── .gitignore                      # Git ignore file
├── README.md                       # Project documentation
├── DEPLOYMENT.md                   # Deployment guide
└── run_app.py                      # Easy launcher script
```

## 💻 How to Use

### Web Application

1. **Input Customer Details**:
   - Age, Income, Loan Amount
   - Loan tenure and purpose
   - Credit history and utilization

2. **View Results**:
   - Default Probability (0-100%)
   - Credit Score (300-900)
   - Credit Rating (Poor/Average/Good/Excellent)

3. **Risk Insights**:
   - Automated recommendations
   - Risk level indicators
   - Actionable insights

### API Usage

```python
from utils import predict

# Example usage
probability, credit_score, rating = predict(
    age=28,
    avg_dpd_per_dm=0,
    credit_utilization_ratio=0,
    dmtlm=0,
    income=290875,
    loan_amount=2560000,
    loan_tenure_months=36,
    total_loan_months=0,
    loan_purpose='Personal',
    loan_type='Unsecured',
    residence_type='Rented'
)

print(f"Default Probability: {probability:.2%}")
print(f"Credit Score: {credit_score}")
print(f"Rating: {rating}")
```

## 🔧 Technical Details

### Model Architecture

- **Algorithm**: XGBoost Classifier
- **Preprocessing**: StandardScaler for numerical features
- **Feature Engineering**: One-hot encoding for categorical variables
- **Hyperparameter Tuning**: Optuna optimization
- **Resampling**: Under-sampling to handle class imbalance

### Key Features

- **Loan-to-Income Ratio (LTI)**: Automatic calculation
- **Credit Utilization**: Percentage-based input
- **Delinquency Metrics**: DPD and DMTLM tracking
- **Categorical Encoding**: One-hot encoding for loan purpose, type, and residence

### Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning utilities
- **xgboost**: Gradient boosting framework
- **joblib**: Model serialization

## 📈 Model Performance

### Evaluation Metrics

| Metric | Value |
|--------|-------|
| AUC Score | 0.98 |
| Gini Coefficient | 0.97 |
| KS Statistic | 86.87% |
| Precision | 0.95 |
| Recall | 0.92 |
| F1-Score | 0.93 |

### Feature Importance

The model identifies key risk factors:
1. Loan-to-Income Ratio
2. Credit Utilization
3. Delinquency History
4. Loan Amount
5. Income Level

## 🚀 Deployment

### Local Deployment

```bash
cd project-root
streamlit run main.py
```

### Cloud Deployment

The application is ready for deployment on:
- **Streamlit Cloud**: Direct GitHub integration
- **Heroku**: With Procfile configuration
- **AWS/GCP/Azure**: Container-based deployment

### Docker Deployment

```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY project-root/ .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
```

## 📊 Visualizations

The project includes comprehensive visualizations:

- **ROC Curve**: Model performance visualization
- **Feature Importance**: SHAP-based feature analysis
- **LIME Explanations**: Local interpretability
- **Decile Analysis**: Risk segmentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/Akkalaspandana)

## 🙏 Acknowledgments

- XGBoost team for the excellent gradient boosting framework
- Streamlit team for the intuitive web app framework
- Scikit-learn community for comprehensive ML tools
- SHAP and LIME for model interpretability

## 📞 Support

For support, email spandana.akkala3@gmail.com or create an issue in the repository.

---

⭐ **Star this repository if you found it helpful!**
