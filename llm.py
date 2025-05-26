import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL_NAME", "openchat/openchat-3.5-1210")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

async def query_llm(messages: list[dict]) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    payload = {
        "model": MODEL,
        "messages": messages
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
