from fastapi import FastAPI
from .email_analysis import run_email_analysis, StartEmailAnalysisPayload
from src.rag_system import rag_instance

app = FastAPI()

@app.post("/start-email-analysis")
async def send_email(payload: StartEmailAnalysisPayload):
    return run_email_analysis(payload)

rag_instance.feed_email("User's name is Benoit Eccli.")
rag_instance.feed_email("User's is 32 years old.")
rag_instance.feed_email("User's nationality is French.")
rag_instance.feed_email("User is an expat living in Hong Kong.")
rag_instance.feed_email("User has a girlfriend called Vaishnavi.")
