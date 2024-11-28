from fastapi import FastAPI
from .email_analysis import run_email_analysis, StartEmailAnalysisPayload

app = FastAPI()

@app.post("/start-email-analysis")
async def send_email(payload: StartEmailAnalysisPayload):
    return run_email_analysis(payload)
