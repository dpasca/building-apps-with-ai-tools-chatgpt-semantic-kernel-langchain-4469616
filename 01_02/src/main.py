import os
import openai
from dotenv import load_dotenv
import json


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Respond in Chinese"},
        {"role": "user", "content": "Say 'Hello world'"}
    ],
    temperature=0.7,
    max_tokens=150,
)

response_message = response["choices"][0]["message"]
txt = json.dumps(response_message, indent=4, ensure_ascii=False)
print(txt)
