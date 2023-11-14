"""
CodeDocGenius - Code Documentation Generator

Automatically generates documentation for code snippets in any programming language.
"""

import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)

def show_doc_page():
    """
    Display the CodeDocGenius page with a title, description, and code input form.

    Parameters:
    - openai_api_key (str): API key for accessing the OpenAI GPT-3.5 model.
    """

    st.title("CodeDocGenius - Code Documentation Generator")
    
    st.markdown('Automatically generates documentation for code snippets in any programming language.')

    with st.form(key="doc_form"):
        code_snippet = st.text_area("Enter code snippet")

        submit_button = st.form_submit_button(label='Generate Documentation')
        
        if submit_button:
            
            st.text(f"Generating documentation... ✨")
            
            chat = ChatOpenAI(
                model="gpt-3.5-turbo-16k",
                temperature=0.7
            )
            system_template = """You are a code documentation generator. Your task is to automatically generate documentation for the given code snippet."""
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_template)
            human_template = """Please automatically generate documentation for the following code snippet:

            {code_snippet}
            
            And provide the modified code with the generated documentation.
            """
            human_message_prompt = HumanMessagePromptTemplate.from_template(
                human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )

            chain = LLMChain(llm=chat, prompt=chat_prompt)
            result = chain.run(code_snippet=code_snippet)

            st.text_area("Generated Documentation", result, height=400)