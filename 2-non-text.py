import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg"
                },
            },
        ],
    }
]

response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

content = response.choices[0].message.content

print(content)
