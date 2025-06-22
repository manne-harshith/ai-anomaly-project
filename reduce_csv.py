import pandas as pd

# Load only the first 30000 rows from the large CSV
df = pd.read_csv("data/transactions.csv", nrows=30000)

# Overwrite the same file with reduced size
df.to_csv("data/transactions.csv", index=False)

print("✅ Reduced to 30,000 rows successfully.")
