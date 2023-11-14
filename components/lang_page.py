"""
LangLink - Code Translation and Cross-Language Compatibility

Overcome language barriers with LangLink, an AI-powered tool facilitating smooth code translation
between programming languages. Developers can confidently migrate codebases, ensuring compatibility
and seamless transitions across different languages.
"""

import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate)

from data.programming_languages import PROGRAMMING_LANGUAGES

def show_lang_page():
    """
    Displays the LangLink page for code translation.

    Parameters:
    - openai_api_key (str): The API key for OpenAI.

    Returns:
    None
    """
    st.title("LangLink - Code Translation and Cross-Language Compatibility")

    st.markdown('Overcome language barriers with LangLink, an AI-powered tool facilitating smooth '
                'code translation between programming languages. Developers can confidently migrate '
                'codebases, ensuring compatibility and seamless transitions across different languages.')

    with st.form(key="lang_form"):
        source_code = st.text_area("Enter source code")
        target_language = st.selectbox("Select programming language", PROGRAMMING_LANGUAGES)

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            
            st.text(f"Translating code snippet to {target_language}................✨")

            chat = ChatOpenAI(
                model="gpt-3.5-turbo-16k",
                temperature=0
            )
            system_template = """You are a code translator. Your task is to translate the given source code to {target_language}."""
            system_message_prompt = SystemMessagePromptTemplate.from_template(
                system_template)
            human_template = """Please translate the following source code to {target_language}: '{source_code}'."""
            human_message_prompt = HumanMessagePromptTemplate.from_template(
                human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )

            chain = LLMChain(llm=chat, prompt=chat_prompt)
            result = chain.run(source_code=source_code,
                               target_language=target_language)
            
            st.markdown(result)
            