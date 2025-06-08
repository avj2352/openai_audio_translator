"""
    API router for
    - translate text-to-text
    - translate text-to-speech
"""
import logging
from fastapi import APIRouter, HTTPException, status

# ..custom
from dto.requests import TranslateTextToTextRequest
from dependencies.ai_helper import translate_text

translate_router = APIRouter()

@translate_router.post("/text-to-text")
def translate_text_to_text(payload: TranslateTextToTextRequest):
    """
        transcribe youtube url video
        to english text file
    """
    # download
    logging.info("(main) download youtube file...")
    try:
        # transcribe
        logging.info("-> (resource) translate...")
        # display
        source = payload.from_language or "english"
        response = translate_text(
            content=payload.content,
            src=source,
            dest=payload.to_language
        )
        logging.debug("-> (resource) Translated text \n\n")
        # logging.debug(f"{transcribe_text}")
        if response is None or response == "":
            raise ValueError("ERROR (main)!: translated text is empty!")
        return {
            "status": 200,
            "text": response
        }
    except Exception as err:
        logging.error(f"(resource): an error occured: {err.__class__} - {str(err)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error with transcribing youtube file"
        )

