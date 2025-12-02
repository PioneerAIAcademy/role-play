# Deployment Guide

This guide provides instructions on how to deploy the BYU-Pathway Role-Play Training application to [Render](https://render.com/).

## Prerequisites

- A Render account.
- The project pushed to a GitHub repository.

## Deployment Steps

1.  **Push your project to GitHub:**
    - Make sure your `.gitignore` file includes `venv/`, `__pycache__/`, and `.env`.
    - Create a new repository on GitHub and push your local project to it.

2.  **Create a New Web Service on Render:**
    - Go to your Render dashboard and click "New + " > "Web Service".
    - Connect your GitHub account and select your project repository.

3.  **Configure the Web Service:**
    - **Name:** Give your service a unique name.
    - **Region:** Choose a region close to your users.
    - **Branch:** Select the branch you want to deploy (e.g., `main`).
    - **Runtime:** Render should automatically detect `Python 3`.
    - **Build Command:** Set this to `pip install -r requirements.txt`.
    - **Start Command:** Set this to `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`.
    - **Instance Type:** The "Free" instance type is sufficient for this application.

4.  **Add Environment Variables:**
    - In the "Environment" section, click "Add Environment Variable".
    - Add your OpenAI API key:
        - **Key:** `OPENAI_API_KEY`
        - **Value:** `sk-...` (your actual OpenAI API key)

5.  **Deploy:**
    - Click the "Create Web Service" button.
    - Render will start the deployment process by running your build command and then the start command.
    - You can monitor the deployment logs from your service's dashboard.
    - Once the deployment is complete, your application will be available at the URL provided by Render.

## Updating the App

To update the application, you just need to push your changes to the connected GitHub repository. Render will automatically detect the changes and redeploy your app.
