import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)


    
coding_styles = {
    "Python": "PEP 8 (Python Enhancement Proposal 8): Style Guide for Python Code",
    "JavaScript": "Airbnb JavaScript Style Guide: A widely used style guide in the JavaScript community",
    "Java": "Google Java Style Guide: The style guide used by Google for Java code",
    "C++": "Google C++ Style Guide: Google's style guide for writing C++ code",
    "C#": "Microsoft C# Coding Conventions: Microsoft's guidelines for writing C# code",
    "Ruby": "Ruby Style Guide: A community-driven Ruby coding style guide",
    "Swift": "Swift.org API Design Guidelines: Guidelines for designing Swift APIs",
}


#Because st.form is designed to not register any changes until you press the submit button
def show_refactor_page(openai_api_key):
    st.title("RefactorRite - Code Refactoring Advisor")
    
    st.markdown('Leverage AI-driven code analysis and automated refactoring to enhance code readability, boost performance, and improve maintainability. RefactorRite suggests intelligent refinements and even automates the refactoring process, allowing developers to focus on building robust software.')

    with st.form(key="refactor_form"):
        code_snippet = st.text_area("Enter code snippet")
        programming_language = st.selectbox(
        "How would you like to be contacted?",
        ("Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Swift"),
        )

        # Automatically select coding style based on the chosen programming language
        coding_style = coding_styles.get(programming_language, "")

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            print('--------------------Submitted')
            result = st.text(f"Suggested coding style for {programming_language}: {coding_styles.get(programming_language, '')}")
            chat = ChatOpenAI(
                model="gpt-3.5-turbo-16k",
                openai_api_key=openai_api_key,
                temperature=0
            )
            system_template = """You are an AI assistant specialized in code refactoring. Your task is to suggest intelligent refinements and automate the refactoring process for the given code snippet."""
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_template)
            human_template = """Please suggest intelligent refinements and automate the refactoring process for the following code snippet written in {programming_language} with {coding_style}:

    {code_snippet}"""
            human_message_prompt = HumanMessagePromptTemplate.from_template(
                human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )

            chain = LLMChain(llm=chat, prompt=chat_prompt)
            result = chain.run(code_snippet=code_snippet,
                               programming_language=programming_language, coding_style=coding_style)
           
            print('---------------------------------------------------------------@@@@@@') 
            print(result)
            st.markdown(result)

