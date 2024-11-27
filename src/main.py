from fastapi import FastAPI
from .email_analysis.service import run_email_analysis

app = FastAPI()

@app.get("/start-email-analysis")
async def root():
    """
    A simple endpoint that returns a message fetched from an external service.
    """
    message = run_email_analysis()
    return {"message": f"Hello World! External message: {message}"}
