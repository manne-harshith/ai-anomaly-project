import pandas as pd
from clickhouse_connect import get_client
import random
import numpy as np
from datetime import datetime, timedelta

# Connect to ClickHouse
client = get_client(
    host='mu1q0f2kws.asia-southeast1.gcp.clickhouse.cloud',
    port=8443,
    username='default',
    password='sJJ5mmbL_8E.K',
    secure=True
)

# Read the dataset
df = pd.read_csv('data/transactions.csv')

# Generate synthetic fields
df['user_id'] = np.random.choice(range(1000, 1050), size=len(df))
df['timestamp'] = [datetime(2023, 1, 1) + timedelta(minutes=i) for i in range(len(df))]  # Unique time per row
df['location'] = [random.choice(['Hyderabad', 'Delhi', 'Mumbai', 'Bangalore']) for _ in range(len(df))]

# Select the required columns
df = df[['user_id', 'amount', 'type', 'timestamp', 'location']]

# Convert to list of tuples
rows = [tuple(row) for row in df.values]

# Insert in smaller batches to avoid timeout
batch_size = 5000
for i in range(0, len(rows), batch_size):
    batch = rows[i:i + batch_size]
    client.insert('transactions', batch)
    print(f"✅ Inserted rows {i} to {i + len(batch)}")

print("🎉✅ All data inserted successfully into ClickHouse.")
