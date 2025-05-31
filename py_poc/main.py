# main function
import logging
# ..custom
from dependencies.ai_helper import transcribe_audio_file
from dependencies.video_helper import get_audio_file
from dependencies.converter import AudioLanguageConverter
from util.helper import write_to_file


# logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s[%(filename)s:%(lineno)s-%(funcName)s()]-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")


def main():
    yt_url: str = input("Enter youtube url to transcribe: ")
    filename: str = input("Provide a name of the audio text file: ") 
    # download
    logging.info("(main) download...")
    audio_file_path: str = get_audio_file(url=yt_url, filename=filename)
    # transcribe
    logging.info("(main) transcribe...")
    transcribe_text: str = transcribe_audio_file(filepath=audio_file_path)
    # display
    logging.debug("{Transcribed text: \n\n}")
    logging.debug(f"{transcribe_text}")
    if transcribe_text is None or transcribe_text == "":
        raise ValueError("ERROR (main)!: transcribe_text is empty!")
    write_to_file(content=transcribe_text, filename=f"{filename}.txt")
    logging.info("⚡Completed transcribe ⚡!!")
    
if __name__ == "__main__":
    main()
