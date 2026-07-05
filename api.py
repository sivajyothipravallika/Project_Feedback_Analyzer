from fastapi import FastAPI
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv
from google.genai import types


load_dotenv()
client = genai.Client()

app = FastAPI()

# what the caller must send us
class Review(BaseModel):
    text: str

# what gemini gives back, and what we SEND to the caller.
# we keep it small on purpose -> fewer tokens used
class Analysis(BaseModel):
    label: str # "Positive", "negative" or "neutral"
    score:int # 1 (very bad) to 5 (very good)
    theme: str # one word: what the review is mainly about (eg: "delivery")

@app.post("/analyze")
def analyze(review: Review):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            "Analyze this customer review.\n"
            "label must be 'positive', 'negative', or 'neutral'.\n"
            "score must be a number from 1 (very bad) to 5 (very good).\n"
            "theme must be ONE lowercase word for the main topic "
            "(for example: delivery, taste, price, service, quality).\n"
            f"Review: {review.text}"
        ),
        config=types.GenerateContentConfig(
            response_mime_type = "application/json",
            response_schema=Analysis
        ),
    )
    return response.parsed