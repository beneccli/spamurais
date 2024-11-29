from fastapi import FastAPI, Path
from .email_analysis import run_email_analysis, StartEmailAnalysisPayload
from src.email_analysis.initalize_rag import initialize_rag_email_analysis
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/start-email-analysis")
async def send_email(payload: StartEmailAnalysisPayload):
    return run_email_analysis(payload)

@app.post("/start-email-analysis-from-email/{email_filename}")
async def send_email(email_filename: str = Path(..., example="password_expired", description="The name of the email file to read.")):
    fullpath = './src/email_analysis/samples/' + email_filename + '.txt'
    try:
        with open(fullpath, 'r') as file:
            content = file.read()
        payload = StartEmailAnalysisPayload(email='a@a.com', content=content)
        return run_email_analysis(payload)
    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"error": f"File '{fullpath}' not found."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"An error occurred: {str(e)}"})

initialize_rag_email_analysis()