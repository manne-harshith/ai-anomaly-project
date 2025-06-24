import os
import requests
from dotenv import load_dotenv

# Load OpenRouter API key from .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise EnvironmentError("❌ OPENROUTER_API_KEY not found in environment!")

# Use Mistral from OpenRouter
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def explain_anomaly(user_id, amount, location):
    prompt = (
        f"A transaction of ₹{amount} was made by user {user_id} in {location}. "
        f"Is this suspicious? Explain in 2 lines."
    )

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful anomaly detection assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        # Handle OpenRouter errors gracefully
        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        elif "error" in result:
            return f"⚠️ OpenRouter Error: {result['error']['message']}"
        else:
            return f"⚠️ Unexpected Response: {result}"

    except Exception as e:
        return f"❌ Exception: {str(e)}"

# Local test
if __name__ == "__main__":
    explanation = explain_anomaly("U1001", 7500, "Delhi")
    print("🧠 Explanation:\n", explanation)
