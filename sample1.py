from dotenv import load_dotenv
import os
from openai import OpenAI
import google.genai as genai

# Load variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Create client
# client = OpenAI(api_key=api_key)

# response = client.responses.create(
#     model="gpt-4.1-mini",
#     input="Explain AI in one sentence"
# )

# print(response.output_text)



client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain AI in one sentence"
)

print(response.text)