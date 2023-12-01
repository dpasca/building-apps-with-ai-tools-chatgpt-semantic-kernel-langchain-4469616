import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    user_input = input("Enter a phrase to classify as happy or sad: ")
    if (user_input == "quit" or user_input == "exit"):
        break
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": """
You are a sentiment classifier. You are given a sentence and you have to determine the mood.
Reply with a single word from the group {happy, sad, neutral}.
"""},
            {"role": "user",
             "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]
    print(response_message)
