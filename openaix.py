# 
# Application for translation using the OpenAI API
# 


# -- Code -----------------------------------------------------

import os
import openai
# import config
from flask import Flask, redirect, render_template, request, url_for

openai.api_key = os.getenv("OPENAI_API_KEY")

def getLanguageTanslation(prompt, language):
    if request.method == "POST":
        response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Translate from portuguese:\nVamos começar a traduzir.",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)