import os

# that means that I wanna use a tool that can read my .env file which containing my api secret code 
from dotenv import load_dotenv

## this is the tool that I use to make my code talk with the brain of my project google gemini without needing to set an connection
#genai = a helper that lets Python talk to Google's AI
from google import genai

load_dotenv()

client = genai.client(api_key=os.getenv("GEMINI_API_KEY"))

response =  client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Why is the sky blue?"
)

print(response.text)