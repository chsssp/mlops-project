# Beginner MLOps Project (From Scratch)

This is a **very beginner-friendly MLOps project** you can showcase on GitHub.

You will learn:
- How to train a ML model
- How to save the model
- How to expose it using FastAPI
- How to version code using GitHub

## Project Flow
1. Generate sample data
2. Train ML model
3. Save model
4. Run API
5. Call API for predictions

## Setup (Mac)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Step 1: Generate data
```bash
python data/generate_data.py
```

## Step 2: Train model
```bash
python training/train.py
```

## Step 3: Run API
```bash
uvicorn api.app:app --reload
```

## Step 4: Test API
```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"age":40,"salary":70000}'
```
