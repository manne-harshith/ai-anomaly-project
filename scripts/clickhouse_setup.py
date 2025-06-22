from clickhouse_connect import get_client

client = get_client(
    host='mu1q0f2kws.asia-southeast1.gcp.clickhouse.cloud',
    port=8443,  # 👈 Use port 8443 for HTTP interface
    username='default',
    password='sJJ5mmbL_8E.K',
    secure=True  # 👈 Required for SSL (HTTPS)
)

client.command('''
CREATE TABLE IF NOT EXISTS transactions (
    user_id UInt32,
    amount Float32,
    type String,
    timestamp DateTime,
    location String
) ENGINE = MergeTree()
ORDER BY timestamp
''')

print("✅ Table 'transactions' created successfully.")
