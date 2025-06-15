"""
    module which uses openai to -
    - read audio file
    - audio-to-text transcribe conversion
    - text-to-speech conversion 
"""
import logging
from openai import OpenAI
from openai.types.responses import Response
from util.env_config import OPENAI_API_KEY, OPENAI_DEFAULT_MODEL
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

# translate text content from source to destination language
def translate_text(content: str, src: str, dest: str) -> str:
    """
        converts text content from specified source language
        to specified destination language
    """
    user_prompt = f"Translate the following text from {src} to {dest}: {content}"
    logging.info(f"->>{user_prompt}")
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response: Response = client.responses.create(
            model=OPENAI_DEFAULT_MODEL,
            input=user_prompt
        )
        logging.debug(f"->> (openai) translate response is: {response.output_text}")
        if response is None:
            logging.error("ERROR (openai) an error occurred with response: invalid response")
            raise ValueError("Invalid response")
        return response.output_text
    except Exception as err:
        logging.error(f"an exception occurred (class): {err.__class__}")
        logging.error(f"{err}")
        raise OpenAIClientException("ERROR (openai)! an error occcurred when translating the given content")

# translate text content from source to destination language
def fetch_ai_assist(content: str) -> str:
    """
        API to fetch openai LLM chat assist
    """
    user_prompt = f"{content}"
    logging.info(f"->>{user_prompt}")
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response: Response = client.responses.create(
            model=OPENAI_DEFAULT_MODEL,
            input=user_prompt
        )
        logging.debug(f"->> (openai) ai_assist response is: {response.output_text}")
        if response is None:
            logging.error("ERROR (openai) an error occurred with response: invalid response")
            raise ValueError("Invalid response")
        return response.output_text
    except Exception as err:
        logging.error(f"an exception occurred (class): {err.__class__}")
        logging.error(f"{err}")
        raise OpenAIClientException("ERROR (openai)! an error occcurred when fetching ai_assist response")

