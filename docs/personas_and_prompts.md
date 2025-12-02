# Personas and Prompts

This document explains how to create and manage the AI personas and their corresponding system prompts.

The `roleplay-content` directory is the heart of the application's content. It contains the detailed descriptions of the student personas and the prompts that guide the AI's behavior.

## Directory Structure

The `roleplay-content` directory is organized as follows:

```
roleplay-content/
├───personas/
│   └───<region>/
│       └───<persona-name>.md
└───prompts/
    └───<region>/
        └───<persona-name>-system-prompt.md
```

- **`personas/`**: This directory contains the detailed backstories and profiles of the student personas, organized by region. These files are for human reference and are not directly used by the application.

- **`prompts/`**: This directory contains the system prompts that are directly fed to the OpenAI API. These prompts define the AI's persona, communication style, and objectives for the conversation.

## How to Add a New Persona

To add a new persona to the application, follow these steps:

1.  **Create a Persona File:**
    - In the `roleplay-content/personas/<region>/` directory, create a new Markdown file for your persona (e.g., `john-doe.md`).
    - Use the `persona-template.md` as a guide to create a detailed profile for your new persona.

2.  **Create a System Prompt File:**
    - In the `roleplay-content/prompts/<region>/` directory, create a new system prompt file for your persona (e.g., `john-doe-system-prompt.md`).
    - This file will contain the instructions that the AI will follow. It should include the persona's backstory, personality, and any specific instructions for the role-playing exercise.
    - Look at the existing system prompts for examples.

3.  **Update `app.py`:**
    - Open the `app.py` file.
    - Locate the `REGIONS` dictionary.
    - Add a new entry for your persona in the appropriate region, following the existing format:

      ```python
      "Your Region": {
          "personas": {
              "New Persona Name": "path/to/your/new-persona-system-prompt.md",
              ...
          },
      },
      ```

4.  **Test:**
    - Run the application and select your new persona.
    - Interact with the persona to ensure that it is behaving as expected.
