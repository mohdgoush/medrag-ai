from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq( api_key=os.getenv("GROQ_API_KEY"))

def generate_response(query, retrieved_chunks, chat_history):

    context = ""
    for chunk in retrieved_chunks:
        context += f"""
Content:
{chunk['text']}
"""
    history = ""

    for message in chat_history:
        role = message["role"]
        content = message["content"]
        history += f"{role}: {content}\n"

    prompt = f"""
Conversation History:
{history}

Medical Report Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are a medical report explanation assistant.

Rules:
1. Explain medical reports in simple language.
2. Do not diagnose diseases.
3. Do not prescribe medicines.
4. Mention abnormal values if present.
5. Suggest consulting a healthcare professional when needed.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1024
    )

    return response.choices[0].message.content