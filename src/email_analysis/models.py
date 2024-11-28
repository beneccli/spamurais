from pydantic import BaseModel

class StartEmailAnalysisPayload(BaseModel):
    email: str
    content: str