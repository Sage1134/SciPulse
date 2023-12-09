import openai
from dotenv import load_dotenv
import os

load_dotenv()
APIKEY = os.getenv("APIKEY")

openai.api_key = APIKEY

def therapist(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = therapist(user_input)
        print("AI Therapist: ", response)
# test
