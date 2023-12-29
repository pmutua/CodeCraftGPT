import streamlit as st
from streamlit_option_menu import option_menu
from langchain.chat_models import ChatOpenAI
from components import (
    home,
    refactor_page,
    style_page,
    test_page,
    lang_page,
    code_documentation_page,
    database_page
)


def main():
    st.set_page_config(
        page_title="CodeCraft GPT: A Comprehensive Code Enhancement Platform",
        page_icon="🚀",
        layout="wide"
    )

    st.sidebar.title("OpenAI API Key")
    api_key = st.sidebar.text_input("Enter your OpenAI API key:")

    if api_key:
        chat = ChatOpenAI(
            model="gpt-3.5-turbo-16k",
            temperature=0,
            api_key=api_key
        )

        selected = option_menu(
            menu_title="CodeCraftGPT",
            options=[
                "Home", "RefactorRite", "StyleSculpt", "TestGenius", 
                "LangLink", "CodeDocGenius", "Database"
            ],
            icons=[
                'house', 'gear', 'palette', 'clipboard2-pulse', 
                'code-slash', 'file-text', 'database'
            ],
            default_index=0
        )

        # Dictionary containing functions without invoking them
        pages = {
            "RefactorRite": refactor_page.show_refactor_page,
            "StyleSculpt": style_page.show_style_page,
            "TestGenius": test_page.show_test_page,
            "LangLink": lang_page.show_lang_page,
            "CodeDocGenius": code_documentation_page.show_doc_page,
            "Database": database_page.show_database_page,
            "Home": home.show_home_page
        }

        if selected in pages:
            # Call the function corresponding to the selected page
            pages[selected](chat)  # Pass chat as argument to the function
        else:
            st.error("Page not found!")

    else:
        st.warning("Please enter your OpenAI API key to access pages.")

if __name__ == "__main__":
    main()
