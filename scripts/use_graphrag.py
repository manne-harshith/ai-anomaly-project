import requests
from neo4j import GraphDatabase

# 🔗 Neo4j connection
URI = "neo4j+s://2135db93.databases.neo4j.io"
AUTH = ("neo4j", "Q9uegzi8sGzWFwz7iXlckEqBq0RCLt-ZLiLKaC3U-2M")
driver = GraphDatabase.driver(URI, auth=AUTH)

# 🔐 OpenRouter API Key
OPENROUTER_API_KEY = "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" 
# 🧠 Step 1: Get suspicious transactions
def get_suspicious_txns():
    with driver.session() as session:
        result = session.run("""
            MATCH (u:User)-[:PERFORMED]->(t:Txn)-[:IN]->(l:Location)
            WHERE t.amount > 100
            RETURN u.id AS user, t.amount AS amount, l.name AS location
        """)
        return [record.data() for record in result]

# 📜 Step 2: Format into LLM prompt
def format_for_llm(txns):
    prompt = "Analyze the following suspicious transactions:\n\n"
    for txn in txns:
        prompt += f"- User {txn['user']} made a ₹{txn['amount']} transaction at {txn['location']}\n"
    prompt += "\nIdentify which ones might be anomalous and explain why."
    return prompt

# 🚀 Step 3: Send prompt to OpenRouter
def query_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful fraud detection assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        result = response.json()

        # 💡 Defensive parsing
        if "choices" in result and result["choices"]:
            return result["choices"][0]["message"]["content"]
        elif "error" in result:
            return f"⚠️ OpenRouter Error: {result['error'].get('message', 'Unknown error')}"
        else:
            return f"⚠️ Unexpected response format: {result}"

    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {str(e)}"
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

# 🎯 Main Logic
if __name__ == "__main__":
    suspicious_txns = get_suspicious_txns()

    if suspicious_txns:
        context_prompt = format_for_llm(suspicious_txns)
        print("\n🧠 Prompt to OpenRouter LLM:\n")
        print(context_prompt)

        print("\n💬 LLM Response:\n")
        explanation = query_openrouter(context_prompt)
        print(explanation)
    else:
        print("No suspicious transactions found.")

    driver.close()
