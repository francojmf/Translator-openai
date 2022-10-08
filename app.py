import os

import openai
from flask import Flask, redirect, render_template, request, url_for
# from prompt import app

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # translate_input = input("What to Translate: ")
        aiPrompt = request.form["aiPrompt"]
        language = request.form['aiLanguage']
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt= "Translate to " + language + ": \n" + aiPrompt ,
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

