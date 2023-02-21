from flask import Flask, render_template, request, flash
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")
app = Flask(__name__)


def generate_response(prompt):

    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
 )
    message = completions.choices[0].text
    return message.strip()


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(generate_response(userText))


if __name__ == '__main__':
    app.run(debug=True)