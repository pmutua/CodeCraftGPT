import os
import streamlit as st
from streamlit_option_menu import option_menu
from components import (
    home,
    refactor_page,
    style_page,
    test_page, lang_page,
    code_documentation_page)


# Set OpenAI API key from Streamlit secret
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(
    page_title="CodeCraft GPT: A Comprehensive Code Enhancement Platform",
    page_icon="🚀",
    layout="wide",
)


with st.sidebar:
    selected = option_menu(
        menu_title="CodeCraftGPT",
        options=["Home", "RefactorRite", "StyleSculpt", "TestGenius", "LangLink", "CodeDocGenius" ],
        icons=['house', 'gear', 'palette', 'clipboard2-pulse', 'code-slash', 'file-text'],
        default_index=0
    )

if selected == "RefactorRite":
    refactor_page.show_refactor_page()
elif selected == "StyleSculpt":
    style_page.show_style_page()
elif selected == "TestGenius":
    test_page.show_test_page()
elif selected == "LangLink":
    lang_page.show_lang_page()
elif selected == "CodeDocGenius":
    code_documentation_page.show_doc_page()
elif selected == "Home":
    home.show_home_page()
