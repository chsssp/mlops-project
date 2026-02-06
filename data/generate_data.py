import pandas as pd
import numpy as np
from pathlib import Path

Path("data").mkdir(exist_ok=True)

np.random.seed(42)
age = np.random.randint(20, 60, 200)
salary = np.random.randint(30000, 120000, 200)
buy = (salary > 60000).astype(int)

df = pd.DataFrame({
    "age": age,
    "salary": salary,
    "buy": buy
})

df.to_csv("data/train.csv", index=False)
print("Data generated: data/train.csv")
