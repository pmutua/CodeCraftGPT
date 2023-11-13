import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)

def show_lang_page(openai_api_key):
    st.title("LangLink - Code Translation and Cross-Language Compatibility")
    
    st.markdown('Overcome language barriers with LangLink, an AI-powered tool facilitating smooth code translation between programming languages. Developers can confidently migrate codebases, ensuring compatibility and seamless transitions across different languages.')

    with st.form(key="lang_form"):
        source_code = st.text_area("Enter source code")
        target_language = st.text_input("Enter the target language")

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            chat = ChatOpenAI(
                model="gpt-3.5-turbo-16k",
                openai_api_key=openai_api_key,
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