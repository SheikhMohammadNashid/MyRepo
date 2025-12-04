"""
Basic LangChain Demo Script
---------------------------
This script demonstrates how to use LangChain with OpenAI (or a mock LLM)
to generate text using an LCEL chain (Prompt → Model → Parser).

Prerequisites:
    pip install langchain langchain-openai langchain-community

Usage:
    python langchain_basic.py [topic]

If no topic is provided, it defaults to "Artificial Intelligence".
"""

import os
import sys
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import FakeListLLM
import openai


def run_langchain_demo():
    print("\n--- Basic LangChain Demo ---\n")

    # ---------------------------
    # 1. Setup OpenAI API Key
    # ---------------------------
    if "OPENAI_API_KEY" not in os.environ:
        print("Warning: OPENAI_API_KEY not found in environment.")

    # Toggle MOCK mode (No API cost)
    USE_MOCK = False

    # ---------------------------
    # 2. Initialize the Model
    # ---------------------------
    try:
        if USE_MOCK:
            print("NOTE: Using MOCK model (no API cost).")
            model = FakeListLLM(
                responses=[
                    "Artificial Intelligence is the simulation of human intelligence by machines."
                ]
            )
        else:
            model = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0.7
            )

    except Exception as e:
        print(f"Error initializing model: {e}")
        return

    # ---------------------------
    # 3. Create Prompt Template
    # ---------------------------
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Please explain {topic} in a detailed paragraph."
    )

    # ---------------------------
    # 4. Output Parser
    # ---------------------------
    parser = StrOutputParser()

    # ---------------------------
    # 5. Build LCEL Chain
    # ---------------------------
    chain = prompt | model | parser

    # ---------------------------
    # 6. Get Topic from CLI Args
    # ---------------------------
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = "Artificial Intelligence"
        print("No topic provided. Using default: 'Artificial Intelligence'")
        print("Usage: python langchain_basic.py [topic]\n")

    print(f"Asking AI about: {topic}...\n")

    # ---------------------------
    # 7. Invoke Chain
    # ---------------------------
    try:
        response = chain.invoke({"topic": topic})
        print("Response:\n")
        print(response)

    except openai.RateLimitError:
        print("\n!!! OPENAI API ERROR: INSUFFICIENT QUOTA !!!")
        print("Your code is correct, but your OpenAI account is out of credits.")
        print("Solution: Add credits at https://platform.openai.com/account/billing")
        print("-" * 50)
        print("Falling back to MOCK mode...\n")

        mock_model = FakeListLLM(
            responses=[
                "(Mock Response) AI is computer systems capable of "
                "performing tasks that typically require human intelligence."
            ]
        )

        mock_chain = prompt | mock_model | parser
        print("Response:", mock_chain.invoke({"topic": topic}))

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    run_langchain_demo()

