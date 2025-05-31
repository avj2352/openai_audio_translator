from pytubefix import YouTube
from openai import OpenAI
from dotenv import load_dotenv

# load openai_api_key from env variables
load_dotenv()

# download from youtube url and transcribe audio
def transcribe_youtube_video(url):
    # Download audio from YouTube video
    try:
        yt = YouTube(url)
        client = OpenAI()

        # generate audio file
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream is None:
            raise ValueError("->> main: Error! audio_stream not availabe!")
        audio_file_path = audio_stream.download(filename="audio.mp3")
        if audio_file_path is None or audio_file_path == "":
            raise ValueError("->> main: Error saving audio file path")

        audio_file= open(audio_file_path, "rb")
        response = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
        )
        print("Generating text...")
        print("\n")
        return response.text

    except Exception as err:
        print(f"Error when trying to transribe: {err.__class__}")
        raise


# main function
def main():
    video_url = input("Enter youtube url to transcribe: ")
    print(f"transcribing text....")
    transcription = transcribe_youtube_video(video_url)
    print(f" transribed text is: {transcription}")

if __name__ == "__main__":
    main()
