"""
    Consists of API requests dto
"""
from pydantic import BaseModel, Field

class YoutubeTranscribeRequest(BaseModel):
    url: str = Field(..., description="Enter youtube url")
    filename: str = Field(..., description="Provide name of the output text file")
