from flask import Flask, request, jsonify, render_template
import os
import sys
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import FakeListLLM
import openai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # loads templates/index.html

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_msg = data.get("message", "")

    USE_MOCK = False

    if USE_MOCK:
        model = FakeListLLM(
            responses=["This is a mock response from fake model."]
        )
    else:
        model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Reply to the user's message:\n\nUser: {topic}\nAssistant:"
    )
    parser = StrOutputParser()

    chain = prompt | model | parser

    try:
        reply = chain.invoke({"topic": user_msg})
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)

