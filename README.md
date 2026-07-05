# Project Feedback Analyzer

A simple AI-powered feedback analysis app that helps a business review customer comments, classify each review, assign a sentiment score, and identify the main topic of the feedback.

## What it does

- Accepts customer reviews from the user
- Sends each review to a backend service for analysis
- Classifies each review as positive, negative, or neutral
- Assigns a score from 1 to 5
- Detects the main theme of the feedback
- Displays a summary of the results in a Streamlit dashboard
- Saves analyzed reviews to a local SQLite database for history

## Tech stack

- Python
- FastAPI for the backend API
- Streamlit for the web dashboard
- Google GenAI for review analysis
- SQLite for saved review history

## Project structure

- app.py - Streamlit frontend dashboard
- api.py - FastAPI backend that calls the AI model
- database.py - SQLite database helpers for saving and loading history
- sample_reviews.txt - Example reviews you can test with
- pyproject.toml - Project dependencies and Python version requirements

## Prerequisites

- Python 3.14+ (as declared in pyproject.toml)
- A Google AI API key
- uv (recommended) or pip

## Setup

1. Clone the repository and move into the project folder.
2. Create a .env file in the project root and add your Google AI API key:

   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```

3. Install dependencies:

   ```bash
   uv sync
   ```

   If you prefer pip:

   ```bash
   pip install -e .
   ```

## Run the app

Start the backend API in one terminal:

```bash
uv run uvicorn api:app --reload
```

In a second terminal, start the Streamlit app:

```bash
uv run streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Usage

- Paste one review per line into the text area
- Click Analyze to process the reviews
- Review the results table and summary metrics
- Click Save to database to keep a history of the analyzed reviews

## Example input

You can try the sample reviews in sample_reviews.txt by copying them into the app.
