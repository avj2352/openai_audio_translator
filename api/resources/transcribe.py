import logging
from fastapi import APIRouter


transcribe_router = APIRouter()

@transcribe_router.get("/youtube")
def transcribe_text_from_youtube():
    """
    """    
    result = "OK"
    return {"message": result}
