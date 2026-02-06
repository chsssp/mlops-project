# MLOps Project – End-to-End Training, Tracking, and Inference Pipeline

This repository demonstrates an end-to-end machine learning workflow including data generation, model training, experiment tracking, containerized inference, and continuous integration. The project reflects production-oriented MLOps practices focused on reproducibility, automation, and reliable model delivery.

---

## Architecture Overview

Data generation → Model training → Experiment tracking → Model artifact persistence → API-based inference → CI validation

This lifecycle enables repeatable experimentation, consistent model serving, and automated validation on every code change.

---

## Project Structure

mlops_project/
- api/                FastAPI inference service  
- data/               Data generation and datasets  
- training/           Model training with MLflow  
- model/              Trained model artifact  
- .github/workflows/  GitHub Actions CI pipeline  
- Dockerfile          Container definition  
- requirements.txt    Python dependencies  
- README.md           Documentation  

---

## Technology Stack

- Python  
- scikit-learn  
- FastAPI  
- MLflow  
- Docker  
- GitHub Actions  

---

## Model Training and Tracking

The training pipeline loads tabular data, trains a classification model, evaluates accuracy, logs metrics and artifacts using MLflow, and saves the trained model for inference.

```bash
python training/train.py
