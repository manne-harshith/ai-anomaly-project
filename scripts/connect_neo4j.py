from neo4j import GraphDatabase

# Connect to Neo4j
URI = "neo4j+s://2135db93.databases.neo4j.io"
AUTH = ("neo4j", "Q9uegzi8sGzWFwz7iXlckEqBq0RCLt-ZLiLKaC3U-2M")  # Replace with the correct password from Aura Console
driver = GraphDatabase.driver(URI, auth=AUTH)

# Function to ingest a transaction
def ingest_transaction(txn):
    with driver.session() as session:
        session.run('''
        MERGE (u:User {id: $user_id})
        MERGE (l:Location {name: $location})
        MERGE (t:Txn {amount: $amount, timestamp: $timestamp})
        MERGE (u)-[:PERFORMED]->(t)-[:IN]->(l)
        ''', txn)

# Sample transaction data
sample_txn = {
    "user_id": "U1",
    "location": "Hyderabad",
    "amount": 150.75,
    "timestamp": "2025-06-22T22:15:00"
}

# Ingest the transaction
ingest_transaction(sample_txn)

# Close connection
driver.close()
