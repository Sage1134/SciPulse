# Import libraries
import openai
from dotenv import load_dotenv
import os

# Define API key
load_dotenv("Vars.env")
key = os.getenv("APIKEY")
openai.api_key = key

# Get response from API
def getResponse(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt + " but answer very short. Max 2 sentences."}
        ]
    )

    response = response.choices[0].message.content.strip()
    return response