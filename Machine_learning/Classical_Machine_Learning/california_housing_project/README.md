# California Housing Price Prediction

This project implements an end-to-end machine learning pipeline for predicting housing prices in California using the California Housing dataset.

## Project Structure

```
california_housing_project/
├── config/
│   └── config.py
├── src/
│   ├── data/
│   │   └── data_processor.py
│   ├── features/
│   │   └── feature_selector.py
│   ├── models/
│   ├── training/
│   │   ├── model_trainer.py
│   │   └── training_pipeline.py
│   └── inference/
│       └── inference_pipeline.py
├── tests/
├── notebooks/
├── docs/
└── azure-pipelines.yml
```

## Features

- Data processing and feature engineering pipeline
- Feature selection using univariate selection and RFE
- Hyperparameter optimization using Optuna
- Model training with ElasticNet regression
- MLflow tracking for experiment management
- Azure ML integration for training and deployment
- CI/CD pipeline using Azure Pipelines

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Training

To train the model:
```bash
python src/training/train.py
```

## Deployment

The model is automatically deployed through Azure Pipelines when changes are pushed to the main branch.

## MLOps Pipeline

The project includes a complete MLOps pipeline:

1. **Testing Stage**: Runs unit tests and generates coverage reports
2. **Training Stage**: Trains the model using Azure ML compute
3. **Deployment Stage**: Deploys the model to Azure Web App

## Monitoring

Model performance is tracked using MLflow and can be viewed in the Azure ML workspace.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
