"""
TestGenius - Code Testing and Test Case Generation

Empowers developers to create reliable and comprehensive test suites effortlessly. TestGenius uses AI
to generate test cases for code snippets, functions, or classes, fostering correctness and enhancing
test coverage. This accelerates the development cycle while ensuring robust software quality.
"""

import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)
from data.testing_libraries import TESTING_LIBRARIES

def show_test_page(openai_api_key):
    """
    Display the TestGenius page with a title, description, and code and test case input form.

    Parameters:
    - openai_api_key (str): API key for accessing the OpenAI GPT-3.5 model.
    """

    st.title("TestGenius - Code Testing and Test Case Generation")

    st.markdown('Empowers developers to create reliable and comprehensive test suites effortlessly. '
                'TestGenius uses AI to generate test cases for code snippets, functions, or classes, '
                'fostering correctness and enhancing test coverage. This accelerates the development '
                'cycle while ensuring robust software quality.')

    with st.form(key="test_form"):
        # Provide examples as placeholders in text areas
        code_snippet = st.text_area(
            "Enter code snippet (e.g., def add_numbers(a, b): return a + b)", value="", height=200)

        selected_testing_library = st.selectbox(
            "Select Testing Library", TESTING_LIBRARIES)

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.text(f"Creating Tests... ✨")

            chat = ChatOpenAI(
                model="gpt-3.5-turbo-16k",
                openai_api_key=openai_api_key,
                temperature=0.7
            )
            system_template = f"""You are a software tester using {selected_testing_library}. Your task is to generate test functions and test cases for the given code snippet or functions."""
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_template)
            human_template = f"""Please generate test functions and test cases for the following code snippet using {selected_testing_library}

    {code_snippet}"""
            human_message_prompt = HumanMessagePromptTemplate.from_template(
                human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )

            chain = LLMChain(llm=chat, prompt=chat_prompt)
            result = chain.run(code_snippet=code_snippet)

            st.markdown(result)
