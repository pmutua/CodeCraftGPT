import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)

def show_test_page(openai_api_key):
    st.title("TestGenius - Code Testing and Test Case Generation")
    
    st.markdown('Empowers developers to create reliable and comprehensive test suites effortlessly. TestGenius uses AI to generate test cases for code snippets, functions, or classes, fostering correctness and enhancing test coverage. This accelerates the development cycle while ensuring robust software quality.')

    with st.form(key="test_form"):
        code_snippet = st.text_area("Enter code snippet")
        test_case = st.text_area("Enter test case")

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            chat = ChatOpenAI(
                model="gpt-3.5-turbo-16k",
                openai_api_key=openai_api_key,
                temperature=0.7
            )
            system_template = """You are a software tester. Your task is to generate test cases for the given code snippet or functions."""
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_template)
            human_template = """Please generate test cases for the following code snippet or functions:

    {code_snippet}

    Test case: {test_case}"""
            human_message_prompt = HumanMessagePromptTemplate.from_template(
                human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )

            chain = LLMChain(llm=chat, prompt=chat_prompt)
            result = chain.run(code_snippet=code_snippet, test_case=test_case)
            st.markdown(result)

