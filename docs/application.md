# Application Logic (`app.py`)

This document explains the structure and logic of the main application file, `app.py`.

The application is built using [Streamlit](https://streamlit.io/) and uses the [OpenAI API](https://openai.com/) to generate responses from the AI personas.

## Structure

The `app.py` file has the following structure:

1.  **Imports:** Necessary libraries such as `streamlit`, `openai`, and `os` are imported.
2.  **Configuration:**
    - The OpenAI API key is loaded from the environment variables.
    - The `REGIONS` dictionary is defined, which maps geographical regions to the available personas and their corresponding system prompt files.
3.  **Helper Functions:**
    - `load_system_prompt(persona_file)`: Reads the content of a persona's system prompt file.
    - `load_grading_prompt()`: Reads the content of the grading prompt file.
    - `format_conversation_transcript(messages)`: Formats the conversation history into a string for the grading prompt.
4.  **Main Application UI:**
    - The Streamlit UI is created, including the title, sidebar, and chat interface.
    - The user selects a region and a persona from the sidebar.
    - The conversation history is stored in the `st.session_state.messages`.
    - When the user sends a message, it is added to the conversation history and a request is sent to the OpenAI API to get a response from the persona.
    - The persona's response is then displayed in the chat interface.
5.  **Grading:**
    - When the user clicks the "Evaluate" button, the conversation transcript is sent to the OpenAI API with the grading prompt.
    - The API returns a grade and feedback, which is then displayed to the user.

## Key Components

- **`REGIONS` Dictionary:** This is a crucial data structure that defines the available personas and their locations. To add a new persona, you need to add an entry to this dictionary.

- **`st.session_state`:** Streamlit's session state is used to store the conversation history and other session-specific variables.

- **OpenAI API Calls:** The application makes two types of calls to the OpenAI API:
    1.  **Chat Completion:** To get responses from the AI personas.
    2.  **Grading Completion:** To get a grade and feedback on the conversation.
