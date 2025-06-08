"""
    Consists of API requests dto
"""
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List


supported_languages: List[str] = ['english', 'hindi', 'tamil']

class YoutubeTranscribeRequest(BaseModel):
    url: str = Field(..., description="Enter youtube url")
    filename: str = Field(..., description="Provide name of the output text file")


class TranslateTextToTextRequest(BaseModel):
    content: str = Field(..., description="text content to translate")
    from_language: Optional[str] = Field(default="english", title="from language", description="source language")
    to_language: str = Field(..., description="translated language")

    # custom validation
    @field_validator("from_language")
    def check_from_language(cls, v):
        if v not in supported_languages:
            raise ValueError('value must be of type - english | hindi | tamil')
        return v.title()

    # custom validation
    @field_validator("to_language")
    def check_to_language(cls, v):
        if v not in supported_languages:
            raise ValueError('value must be of type - english | hindi | tamil')
        return v.title()

