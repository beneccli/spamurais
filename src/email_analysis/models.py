from pydantic import BaseModel, Field

class StartEmailAnalysisPayload(BaseModel):
    email: str = Field(..., example="example@example.com")
    content: str = Field(..., example="What is the user's name and age?")
