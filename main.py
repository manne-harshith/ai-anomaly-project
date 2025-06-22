from fastapi import FastAPI
from scripts.explain_anomalies import explain_anomaly 

app = FastAPI()

@app.get("/explain")
def get_explanation(user_id: str, amount: float, location: str):
    explanation = explain_anomaly(user_id, amount, location)
    return {"explanation": explanation}
