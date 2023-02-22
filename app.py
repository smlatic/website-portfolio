# Importing necessary libraries

from flask import Flask, render_template, request
import os
import openai
from dotenv import load_dotenv
from prompts import custom1

# Loading environment variables
load_dotenv()

# Setting up OpenAI API key
openai.api_key = os.getenv("API_KEY")

# Initializing the Flask app and server
app = Flask(__name__)



# Defining a function to generate the AI response to user input
def generate_response(prompt):

    # Using OpenAI to generate response
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=custom1 + "\n" + prompt + "\n",
        temperature=0.5,
        max_tokens=80,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
 )
    # Extracting the AI-generated message from the API response
    message = completions.choices[0].text
    return message.strip()



# Setting up the home page route
@app.route('/')
def home():
    return render_template("index.html")


# Setting up the route to get the AI response to user input
@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(generate_response(userText))


if __name__ == '__main__':
    app.run(debug=True)