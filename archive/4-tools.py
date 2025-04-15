import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


def multiply(a, b):
    return a * b


messages = [{"role": "user", "content": "What is 1834.2384 multiplied by 3935.2384 ?"}]

tools = [
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Returning value of a multiplied by b",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First value of argument"},
                    "b": {"type": "number", "description": "Second value of argument"},
                },
                "required": ["a", "b"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages, tools=tools
)

tool_call = response.choices[0].message.tool_calls[0]  # []
args = json.loads(tool_call.function.arguments)

tool_result = multiply(args["a"], args["b"])

messages.append(
    {
        "role": "function",
        "name": tool_call.function.name,
        "content": json.dumps(tool_result),
    }
)

messages.append(response.choices[0].message)
messages.append(
    {"role": "tool", "tool_call_id": tool_call.id, "content": str(tool_result)}
)

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages, tools=tools
)
result_content = response.choices[0].message.content
print(messages)
print(result_content)
