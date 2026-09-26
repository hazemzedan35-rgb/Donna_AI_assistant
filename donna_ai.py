# the tool that make my code can talk with the computer 
import os

# that means that I wanna use a tool that can read my .env file which containing my api secret code 
from dotenv import load_dotenv

## this is the tool that I use to make my code talk with the brain of my project google gemini without needing to set an connection
#genai = a helper that lets Python talk to Google's AI
from google import genai

# read my .env file and hide my api sectret key in a temprory place in my computer memory called an environmental variable
load_dotenv()

# open a connection to google and use my api_key as id      # go check this place that that is named as "GEMINI_API_KEY" and give me its value 
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


question = input("Type: ")

# this mean use the connection that I got to generate an answer then store it in a variable called response
response =  client.models.generate_content(
    # the version of ai that will be used to generate the answer
    model="gemini-2.5-flash",

    # my question
    contents=question
)

# print the value that I stored it in text 
print(response.text)