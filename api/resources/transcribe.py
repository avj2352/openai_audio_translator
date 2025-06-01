import logging
from fastapi import APIRouter, HTTPException, status

# ..custom
from dto.requests import YoutubeTranscribeRequest
from dependencies.ai_helper import transcribe_audio_file
from dependencies.video_helper import get_audio_file



transcribe_router = APIRouter()

@transcribe_router.post("/youtube")
def transcribe_text_from_youtube(payload: YoutubeTranscribeRequest):
    """
        transcribe youtube url video
        to english text file
    """
    # download
    logging.info("(main) download youtube file...")
    try:
        audio_file_path: str = get_audio_file(url=payload.url, filename=payload.filename)
        # transcribe
        logging.debug(f"-> (resource) audio_file_path is: {audio_file_path}")
        logging.info("-> (resource) transcribe...")
        transcribe_text: str = transcribe_audio_file(filepath=audio_file_path)
        # display
        logging.debug("-> (resource) Transcribed text \n\n")
        # logging.debug(f"{transcribe_text}")
        if transcribe_text is None or transcribe_text == "":
            raise ValueError("ERROR (main)!: transcribe_text is empty!")
        return {
            "status": 200,
            "text": transcribe_text
        }
    except Exception as err:
        logging.error(f"(resource): an error occured: {err.__class__} - {str(err)}")
        raise HTTPException(
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error with transcribing youtube file"
                        )
