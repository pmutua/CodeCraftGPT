"""
RefactorRite - Code Refactoring Advisor

Leverage AI-driven code analysis and automated refactoring to enhance code
readability, boost performance, and improve maintainability. RefactorRite
suggests intelligent refinements and even automates the refactoring process,
allowing developers to focus on building robust software.
"""

import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)
from llm.models import chat

def show_refactor_page():
    """
    Display the RefactorRite page with a title, description, and code input form.

    Parameters:
    - openai_api_key (str): API key for accessing the OpenAI GPT-3.5 model.
    """

    st.title("RefactorRite - Code Refactoring Advisor")

    st.markdown(
        """
        Leverage AI-driven code analysis and automated refactoring to enhance code
        readability, boost performance, and improve maintainability. RefactorRite
        suggests intelligent refinements and even automates the refactoring process,
        allowing developers to focus on building robust software.
        """
    )

    with st.form(key="refactor_form"):
        # Allow users to enter a code snippet in a text area
        code_snippet = st.text_area("Enter code snippet")

        # Create a submit button within the form
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.text(f"Refactoring code snippet... ✨")

            # Define system and human message templates for the AI conversation
            system_template = """You are an AI assistant specialized in code refactoring. Your task is to suggest intelligent refinements and automate the refactoring process for the given code snippet."""
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_template)
            human_template = """Please suggest intelligent refinements and automate the refactoring process for the following code snippet:

            {code_snippet}"""
            human_message_prompt = HumanMessagePromptTemplate.from_template(
                human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )

            # Initialize an LLMChain for running the AI conversation
            chain = LLMChain(llm=chat, prompt=chat_prompt)

            # Get the result of the refactoring suggestions from the AI
            result = chain.run(code_snippet=code_snippet)

            # Display the result of the refactoring suggestions
            st.text_area("Refactor suggestions", result, height=400)