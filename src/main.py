from fastapi import FastAPI
from .email_analysis import run_email_analysis, StartEmailAnalysisPayload
from src.email_analysis.initalize_rag import initialize_rag_email_analysis

app = FastAPI()

@app.post("/start-email-analysis")
async def send_email(payload: StartEmailAnalysisPayload):
    return run_email_analysis(payload)

initialize_rag_email_analysis()