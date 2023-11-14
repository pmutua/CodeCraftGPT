import streamlit as st
from streamlit_option_menu import option_menu
from components import (
    home,
    refactor_page,
    style_page,
    test_page, lang_page,
    code_documentation_page)

st.set_page_config(
    page_title="CodeCraft GPT: A Comprehensive Code Enhancement Platform",
    page_icon="🚀",
    layout="wide",
)

# Get the OpenAI API key from the user input in the sidebar
openai_api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

# Render the home page by default
if not (openai_api_key and openai_api_key.startswith("sk-") and len(openai_api_key) >= 20):
    home.show_home_page()

# Ensure the API key is provided and meets the required format
if openai_api_key and openai_api_key.startswith("sk-") and len(openai_api_key) >= 20:
    with st.sidebar:
        selected = option_menu(
            menu_title="CodeCraftGPT",
            options=["Home", "RefactorRite", "StyleSculpt", "TestGenius", "LangLink", "CodeDocGenius" ],
            icons=['house', 'gear', 'palette', 'clipboard2-pulse', 'code-slash', 'file-text'],
            default_index=0
        )

    if selected == "RefactorRite":
        refactor_page.show_refactor_page(openai_api_key)
    elif selected == "StyleSculpt":
        style_page.show_style_page(openai_api_key)
    elif selected == "TestGenius":
        test_page.show_test_page(openai_api_key)
    elif selected == "LangLink":
        lang_page.show_lang_page(openai_api_key)
    elif selected == "CodeDocGenius":
        code_documentation_page.show_doc_page(openai_api_key)
    elif selected == "Home":
        home.show_home_page()
