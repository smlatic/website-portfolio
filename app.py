from flask import Flask, render_template, request, flash
import os
import openai





app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def submit():
    response = request.form['name']
    return render_template("index.html", response=response)

if __name__ == '__main__':
    app.run(debug=True)


# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="",
#   temperature=0.5,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )