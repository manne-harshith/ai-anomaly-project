import os
from openai import OpenAI
from dotenv import load_dotenv

print("📦 Loading environment...")
load_dotenv()

print("🔑 Fetching API key...")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def explain_anomaly(user_id, amount, location):
    prompt = f"User {user_id} made a transaction of Rs.{amount} in {location}. Is it anomalous? Explain in 2 lines."
    print(f"🧠 Sending prompt: {prompt}")
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  # safer model choice
            messages=[{"role": "user", "content": prompt}]
        )
        print("✅ Got response from model.")
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

if __name__ == "__main__":
    print("🚀 Running anomaly explanation...")
    result = explain_anomaly(1012, 12000, "Mumbai")
    print("🧠 Explanation:\n", result)
