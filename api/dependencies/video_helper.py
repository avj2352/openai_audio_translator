"""
    module related to download
    & parse video / audio stream
    from youtube url specified
"""
import logging
from pytubefix import YouTube
from exceptions.custom_exception import YoutubeClientException

# parse and save as audio file
def get_audio_file(url: str, filename: str) -> str:
    logging.debug("->>(pytube) download audio file...")
    if url == "" or filename == "":
        raise YoutubeClientException(f"ERROR! url / filename cannot be empty!")
    """
        this function will download
        the audio stream from specified url
        by using pytubefix.Youtube
        @params - youtube url
        @params - filename
        @returns - audio file path
    """
    try:
        yt = YouTube(url)
        # generate audio file
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream is None:
            raise YoutubeClientException("ERROR (pytube)! audio_stream is not available")
        logging.debug("->> Downloading audio to downloads folder")
        audio_file_path = audio_stream.download(output_path="downloads", filename="audio.mp3")
        if audio_file_path is None or audio_file_path == "":
            raise YoutubeClientException("ERROR (pytube)! error saving audio file path")
        return audio_file_path
    except Exception as err:
        logging.error(f"an exception occurred (class): {err.__class__}")
        logging.error(f"{err}")
        raise YoutubeClientException("ERROR (pytube)! an error occurred when streaming audio file from url")
    
