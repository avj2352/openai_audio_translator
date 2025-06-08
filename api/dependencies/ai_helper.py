"""
    module which uses openai to -
    - read audio file
    - audio-to-text transcribe conversion
    - text-to-speech conversion 
"""
import logging
from openai import OpenAI
from util.env_config import OPENAI_API_KEY
from exceptions.custom_exception import OpenAIClientException

# read from audio file and transcribe to text
def transcribe_audio_file(filepath: str) -> str:
    logging.info(f"->>(openai) transcribe text to file: {filepath}")
    logging.debug(f"->>(openai) OPEN_API_KEY: {OPENAI_API_KEY}")
    if filepath == "":
        raise OpenAIClientException("ERROR (openai)! invalid filepath")
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        # read file
        audio_file = open(filepath, "rb")
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        logging.debug("Generating text...\n")
        return response.text
    except Exception as err:
        logging.error(f"an exception occurred (class): {err.__class__}")
        logging.error(f"{err}")
        raise OpenAIClientException("ERROR (openai)! an error occcurred when transcribing audio file")
