import pandas as pd

df = pd.read_csv('data/transactions.csv')
print(df.columns)

import pandas as pd
import random

df = pd.read_csv('data/transactions.csv')
print("🧾 Columns in original CSV:")
print(df.columns)
df['location'] = [random.choice(['Hyderabad', 'Delhi', 'Mumbai']) for _ in range(len(df))]
print("✅ Columns after processing:")
print(df.columns)
