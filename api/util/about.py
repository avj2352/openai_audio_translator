"""
About the application
"""
from fastapi.security import HTTPBasic
from pydantic_settings import BaseSettings
from typing import List, Any

API_VERSION: str = "0.1.3"

description: str = f"""
<p>
    This API microservice is a POC solution to transcribe & translate english
    audio files / youtube url videos to hindi audio mp3
</p>
<p>
    version: <b>{API_VERSION}</b>
</p>
"""

class GlobalConfig(BaseSettings):
    """
    Global configuration for environment
    """
    tags_metadata: List[Any]  = [        
        {
            "name": "transcribe",
            "description": "Consists of API collection to create, update, read & delete assets",
        },
        {
            "name": "prompt",
            "description": "Consists of API collection related to AI LLM prompt & assist"
        },
        {
            "name": "generate",
            "description": "Consists of API collection related to generating audio video media assets",
        }
    ]
    title: str = "OpenAI Audio Translator"
    version: str = API_VERSION    

config = GlobalConfig()
security = HTTPBasic()
