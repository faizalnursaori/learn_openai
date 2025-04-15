import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

messages = [
    {"role": "user", "content": "What is the different between OpenAI and ChatGPT?"}
]

response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

content = response.choices[0].message.content

print(content)
