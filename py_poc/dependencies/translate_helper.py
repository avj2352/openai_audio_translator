"""
    Facade layer which uses
    AudioLanguageConverter class to:
    1. generate hindi text
    2. convert hindi text to hindi audio file
"""
import logging
# ..custom
from util.env_config import OPENAI_API_KEY
from dependencies.converter import AudioLanguageConverter

# init class
converter_service = AudioLanguageConverter(api_key=OPENAI_API_KEY)

# translate english
def translate_english_text_to_hindi_text(input_file_path: str, output_file_path: str) -> None:
    """
        this function translates the input english text to hindi 
    """
    logging.info(f"english input text file: {input_file_path}")
    try:
        ...
    except Exception as err:
        logging.error(f"Error translating the file to hindi text: {err.__class__} - {str(err)}")
        raise ValueError("ERROR: Error translating text file")
