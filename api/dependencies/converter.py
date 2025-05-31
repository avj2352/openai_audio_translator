import openai
import os
from pathlib import Path
from typing import cast, Literal

class AudioLanguageConverter:
    def __init__(self, api_key: str):
        """Initialize the converter with OpenAI API key."""
        self.client = openai.OpenAI(api_key=api_key)
    
    def transcribe_audio(self, audio_file_path: str) -> str:
        """
        Transcribe English audio to text using Whisper.
        
        Args:
            audio_file_path: Path to the input MP3 file
            
        Returns:
            Transcribed text in English
        """
        try:
            with open(audio_file_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language="en"  # Specify English
                )
            return transcript.text
        except Exception as e:
            raise Exception(f"Transcription failed: {str(e)}")
    
    def translate_text(self, english_text: str) -> str:
        """
        Translate English text to Hindi using GPT.
        
        Args:
            english_text: Text to translate
            
        Returns:
            Translated text in Hindi
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a professional translator. Translate the given English text to Hindi. Maintain the tone, context, and meaning. Respond only with the Hindi translation."
                    },
                    {
                        "role": "user", 
                        "content": f"Translate this English text to Hindi: {english_text}"
                    }
                ],
                temperature=0.3
            )
            if response is None or response.choices is None \
                or len(response.choices) == 0 or response.choices[0].message is None \
                or response.choices[0].message.content is None:
                    raise ValueError("ERROR: invalid response!")
            # strip response
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")
    
    def text_to_speech(self, hindi_text: str, output_path: str, voice_input: str = "alloy") -> str:
        """
        Convert Hindi text to speech using OpenAI TTS.
        
        Args:
            hindi_text: Text in Hindi to convert to speech
            output_path: Path for output MP3 file
            voice: Voice to use (alloy, echo, fable, onyx, nova, shimmer)
            
        Returns:
            Path to the generated audio file
        """
        try:
            # input to be limited to only these types
            voice_type = Literal["alloy", "ash", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer"]
            response = self.client.audio.speech.create(
                model="tts-1",  # or "tts-1-hd" for higher quality
                voice=cast(voice_type, voice_input),
                input=hindi_text,
                response_format="mp3"
            )
            
            # Save the audio file
            with open(output_path, "wb") as f:
                f.write(response.content)
            
            return output_path
        except Exception as e:
            raise Exception(f"Text-to-speech failed: {str(e)}")
    
    def convert_english_to_hindi_audio(self, 
                                     input_mp3: str, 
                                     output_mp3: str, 
                                     voice: str = "alloy") -> dict:
        """
        Complete pipeline: English MP3 -> Hindi MP3
        
        Args:
            input_mp3: Path to input English MP3 file
            output_mp3: Path for output Hindi MP3 file
            voice: Voice to use for TTS
            
        Returns:
            Dictionary with process results and intermediate texts
        """
        results = {}
        
        print("Step 1: Transcribing English audio...")
        english_text = self.transcribe_audio(input_mp3)
        results['english_text'] = english_text
        print(f"Transcription: {english_text[:100]}...")
        
        print("Step 2: Translating to Hindi...")
        hindi_text = self.translate_text(english_text)
        results['hindi_text'] = hindi_text
        print(f"Translation: {hindi_text[:100]}...")
        
        print("Step 3: Generating Hindi audio...")
        output_path = self.text_to_speech(hindi_text, output_mp3, voice)
        results['output_file'] = output_path
        print(f"Hindi audio saved to: {output_path}")
        
        return results


# TESTING
def main():
    # Configuration
    API_KEY = os.getenv("OPENAI_API_KEY")  # Set your API key as environment variable
    if not API_KEY:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    # File paths
    input_file = "english_audio.mp3"  # Your input English MP3 file
    output_file = "hindi_audio.mp3"   # Output Hindi MP3 file
    
    # Initialize converter
    converter = AudioLanguageConverter(API_KEY)
    
    # Convert audio
    try:
        results = converter.convert_english_to_hindi_audio(
            input_mp3=input_file,
            output_mp3=output_file,
            voice="alloy"  # Choose from: alloy, echo, fable, onyx, nova, shimmer
        )
        
        print("\n" + "="*50)
        print("CONVERSION COMPLETED SUCCESSFULLY!")
        print("="*50)
        print(f"Original English: {results['english_text'][:200]}...")
        print(f"Hindi Translation: {results['hindi_text'][:200]}...")
        print(f"Output file: {results['output_file']}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")

# Alternative function for batch processing
def batch_convert_audio_files(api_key: str, input_folder: str, output_folder: str):
    """Convert multiple English MP3 files to Hindi."""
    converter = AudioLanguageConverter(api_key)
    
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True)
    
    mp3_files = list(input_path.glob("*.mp3"))
    
    for mp3_file in mp3_files:
        try:
            output_file = output_path / f"hindi_{mp3_file.name}"
            print(f"\nProcessing: {mp3_file.name}")
            
            converter.convert_english_to_hindi_audio(
                input_mp3=str(mp3_file),
                output_mp3=str(output_file)
            )
            
        except Exception as e:
            print(f"Failed to process {mp3_file.name}: {str(e)}")

if __name__ == "__main__":
    main()
