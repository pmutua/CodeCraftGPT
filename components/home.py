import streamlit as st




def show_home_page():
    
    st.title('CodeCraft GPT: The Ultimate Dev Hack!')
    
    
    st.markdown("CodeCraft AI is an all-in-one platform that revolutionizes the coding experience for developers. With its advanced Language Models, it offers intelligent suggestions and automates the refactoring process, allowing developers to focus on building robust software. It provides real-time feedback on coding style, enforcing best practices and enhancing code quality. CodeCraft AI also generates test cases for code snippets, functions, or classes, ensuring correctness and enhancing test coverage. Additionally, it facilitates code translation between programming languages, making codebase migration seamless and ensuring compatibility. Say goodbye to tedious coding tasks and unleash your creativity with CodeCraft AI!")
    
    
    st.markdown("""# How to use

        1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) above🔑

        2. Provide the code snippet you want to refactor.

        3. Specify the programming language of the code snippet.

        4. Choose your preferred coding style.

        5. Enter the test case for the code snippet.

        6. Share the source code you want to translate.

        7. Specify the target language for code translation.

        8. Wait for intelligent refinements and automated refactoring suggestions.

        9. Receive feedback on coding style and improvement suggestions.

        10. Generate test cases for the code snippet, functions, or classes.

        11. Translate the source code to the target language.

        12. View the refined code, feedback, generated test cases, and translated code.""")
