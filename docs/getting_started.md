# Getting Started

This document provides instructions on how to set up and run the BYU-Pathway Role-Play Training application.

## Prerequisites

- Python 3.7+
- An OpenAI API key

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    - Create a file named `.env` in the root of the project.
    - Add your OpenAI API key to the `.env` file:
      ```
      OPENAI_API_KEY="your-api-key"
      ```

## Running the Application

Once you have completed the installation steps, you can run the application using Streamlit:

```bash
streamlit run app.py
```

The application will be available at the URL provided in the terminal (usually `http://localhost:8501`).
