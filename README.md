# MLOps Project – End-to-End Model Training and Inference Pipeline

This repository demonstrates an end-to-end machine learning workflow covering data generation, model training, model artifact persistence, and real-time inference using a REST API. The project follows production-oriented MLOps principles such as modular design, reproducibility, and service-based deployment.

---

## Architecture Overview

The system follows a standard machine learning lifecycle:

Data ingestion → Model training → Model persistence → API-based inference

This structure enables reliable model development and scalable serving.

---

## Project Structure

mlops-project/
api/            – FastAPI inference service  
data/           – Data generation and datasets  
training/       – Model training pipeline  
model/          – Trained model artifact  
requirements.txt – Project dependencies  

---

## Technology Stack

- Python  
- scikit-learn  
- FastAPI  
- Uvicorn  
- Joblib  
- Git and GitHub  

---

## Model Training

The training pipeline loads structured data, trains a classification model, evaluates performance, and serializes the trained model for inference.

Run training using:

```bash
python training/train.py
