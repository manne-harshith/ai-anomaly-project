from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scripts.explain_anomalies import explain_anomaly
from scripts.use_graphrag import get_suspicious_txns, format_for_llm, query_openrouter

app = FastAPI()

# ✅ Add CORS (non-blocking for frontend calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust in production)
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Anomaly Detection API is running!"}

@app.get("/explain")
def get_explanation(user_id: str, amount: float, location: str):
    """
    Explain a specific anomaly using Hugging Face LLM.
    """
    explanation = explain_anomaly(user_id, amount, location)
    return {"explanation": explanation}

@app.get("/analyze")
def analyze():
    """
    Analyze all suspicious transactions using Graph + OpenRouter.
    """
    suspicious_txns = get_suspicious_txns()
    if not suspicious_txns:
        return {"message": "No suspicious transactions found."}

    context_prompt = format_for_llm(suspicious_txns)
    result = query_openrouter(context_prompt)
    return {"explanation": result}
