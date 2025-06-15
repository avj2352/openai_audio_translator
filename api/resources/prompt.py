"""
    API router for
    - translate text-to-text
    - user prompt ai assist
"""
import logging
from fastapi import APIRouter, HTTPException, status

# ..custom
from dto.requests import TranslateTextToTextRequest, UserPromptAssistRequest
from dependencies.ai_helper import translate_text, fetch_ai_assist

prompt_router = APIRouter()

@prompt_router.post("/translate")
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
            detail="Error with translating input content"
        )


@prompt_router.post("/ai_assist")
def user_prompt_assist(payload: UserPromptAssistRequest):
    """
        transcribe youtube url video
        to english text file
    """
    # download
    logging.info("(prompt) passing down user prompt")
    try:
        response = fetch_ai_assist(
            content=payload.user_prompt
        )
        logging.debug("-> (resource) AI assist response \n\n")
        # logging.debug(f"{transcribe_text}")
        if response is None or response == "":
            raise ValueError("ERROR (main)!: AI assist response is empty!")
        return {
            "status": 200,
            "text": response
        }
    except Exception as err:
        logging.error(f"(resource): an error occured: {err.__class__} - {str(err)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error with AI assist"
        )

