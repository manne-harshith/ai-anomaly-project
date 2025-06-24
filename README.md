# AI-Powered Anomaly Detection Using ClickHouse & Neo4j

## 🔍 Overview

This project is a cloud-deployed, AI-powered anomaly detection system designed to ingest, analyze, and explain financial transaction data. It leverages high-performance analytics (ClickHouse), graph-based reasoning (Neo4j + GraphRAG), and LLMs (OpenRouter/HuggingFace) to provide deep insights into suspicious activities.

---

## 🎯 Project Objectives

* ✅ Ingest financial transaction data into ClickHouse.
* ✅ Define a User-Defined Function (UDF) to detect anomalies like:

  * Large transactions
  * High-frequency transactions
  * Geographic outliers
* ✅ Use LLMs (OpenRouter, Hugging Face) to explain anomalies in plain English.
* ✅ Model entity relationships (users, locations) in Neo4j.
* ✅ Use GraphRAG to enhance reasoning about suspicious patterns.
* ✅ Deploy the solution to the cloud (Render) with CLI-based access.

---

## 🛠 Tech Stack

| Layer            | Technology                      |
| ---------------- | ------------------------------- |
| Data Ingestion   | Python + Pandas                 |
| Database (OLAP)  | ClickHouse + UDFs               |
| Graph Reasoning  | Neo4j + Cypher                  |
| LLM Explanation  | OpenRouter / HuggingFace APIs   |
| Cloud Deployment | Render (via GitHub integration) |
| Optional UI      | FastAPI (optional future use)   |

---

## 📁 Project Structure

```bash
ai-anomaly-project/
├── .env                    # API keys (OPENROUTER_API_KEY)
├── .gitignore              # Excludes venv, pycache, CSVs
├── requirements.txt        # All required packages
├── data/                   # Contains transactions.csv
├── scripts/                # All key scripts listed below
│   ├── check_columns.py
│   ├── clickhouse_setup.py
│   ├── load_csv_to_clickhouse.py
│   ├── connect_neo4j.py
│   ├── explain_anomalies.py
│   ├── use_graphrag.py
├── main.py (optional)
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/manne-harshith/ai-anomaly-project.git
cd ai-anomaly-project
```

### 2. Setup Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 4. Load Data to ClickHouse

```bash
python scripts/load_csv_to_clickhouse.py
```

### 5. Run Graph-Based Anomaly Reasoning

```bash
python scripts/use_graphrag.py
```

Expected Output:

* Suspicious transaction summary
* LLM explanation from OpenRouter

---

## 🚀 Deployment on Render

* GitHub branch: `main`
* Build command:

```bash
pip install -r requirements.txt
```

* Start command:

```bash
python scripts/use_graphrag.py
```

* Add environment variable: `OPENROUTER_API_KEY`

---

## 📦 AI Tool Usage Summary

| Tool           | Purpose                                       |
| -------------- | --------------------------------------------- |
| GitHub Copilot | Speed up script writing and debugging         |
| ChatGPT        | Strategy, debugging errors, code explanations |
| Hugging Face   | Anomaly interpretation (optional)             |
| OpenRouter LLM | Plain-text explanations for transactions      |

---

## 📊 Sample Output

```text
🧠 Prompt to OpenRouter LLM:
- User U1 made a ₹150.75 transaction at Hyderabad

💬 LLM Response:
This transaction might be anomalous due to unusual location or value spikes.
```

---

## 📈 Future Improvements

* Add FastAPI or Streamlit UI to visualize suspicious transactions.
* Expand UDFs to cover more anomaly types (e.g. time-of-day patterns).
* Enable anomaly feedback loop to fine-tune LLM prompts.

---

## 📬 Contact

**Author**: Manne Harshith
**GitHub**: [manne-harshith](https://github.com/manne-harshith)
**Deployed On**: [Render Dashboard](https://dashboard.render.com/)

---

> "Fraud may try to hide in patterns, but AI will always find a way to connect the dots."

---

✅ All functionality tested & verified. You're good to showcase this in your Loom demo!
