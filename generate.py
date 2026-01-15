import os
from sarvamai import SarvamAI
from dotenv import load_dotenv

load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

if not SARVAM_API_KEY:
    raise ValueError("SARVAM_API_KEY not found in environment")

client = SarvamAI(
    api_subscription_key=SARVAM_API_KEY
)

def generate_answer(question: str, chunks: list[str]) -> str:
    """
    Generate an answer using Sarvam LLM based on retrieved legacy code chunks.
    """

    # 🔴 IMPORTANT: keep context short to avoid token overflow
    context = "\n\n".join(chunks[:3])

    prompt = f"""
You are an expert legacy system analyst.

Using ONLY the context below (Java legacy code),
answer the question in clear business terms.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions(
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=700
    )

    # ✅ CORRECT Sarvam response access
    return response.choices[0].message.content
