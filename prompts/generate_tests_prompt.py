from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)

def create_test_generation_prompt(selected_testing_library, code_snippet):
    """
    Create a chat prompt for a software tester generating test functions and test cases.

    Parameters:
    - selected_testing_library (str): The testing library to be used for generating tests.
    - code_snippet (str): The code snippet or functions for which test functions and cases are to be generated.

    Returns:
    langchain.chat_models.ChatPromptTemplate: The generated chat prompt template.
    """
    # Define system and human message templates for the AI conversation
    system_template = f"""You are a software tester using {selected_testing_library}. Your task is to generate test functions and test cases for the given code snippet or functions."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    human_template = f"""Please generate test functions and test cases for the following code snippet using {selected_testing_library}

    {code_snippet}"""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    return chat_prompt