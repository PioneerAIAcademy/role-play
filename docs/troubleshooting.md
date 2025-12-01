# Troubleshooting Guide

This guide provides solutions to common problems you might encounter while running the application.

## `ModuleNotFoundError: No module named 'openai'`

This error means that the required Python packages are not installed correctly.

**Solution:**

1.  Make sure your virtual environment is activated.
    -   On macOS/Linux: `source venv/bin/activate`
    -   On Windows: `venv\Scripts\activate`
2.  Install the dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## OpenAI API Key Not Found or Invalid

If you see errors related to the OpenAI API key, it means the application cannot access your key.

**Symptoms:**
- An error message saying the API key is missing.
- A `401 Unauthorized` error from the OpenAI API.

**Solution:**

1.  Ensure you have a `.env` file in the root directory of the project.
2.  Make sure the `.env` file contains your API key in the correct format:
    ```
    OPENAI_API_KEY="sk-..."
    ```
3.  Verify that your API key is correct and has not been revoked. You can check your API keys on the [OpenAI website](https://platform.openai.com/account/api-keys).

## `FileNotFoundError` when selecting a persona

This error occurs if the application cannot find the system prompt file for the selected persona.

**Solution:**

1.  Open `app.py` and find the `REGIONS` dictionary.
2.  Check the file path for the persona you selected.
3.  Verify that the file path is correct and that the file exists in the `roleplay-content/prompts/` directory.
4.  Ensure there are no typos in the file name or the path in the `REGIONS` dictionary.
