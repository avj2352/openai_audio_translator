# OpenAI Audio Translator

Python POC example to leverage AI (OpenAI) to:

- Transcribe English audio mp3 file / Youtube URL to text (creates a .txt file)
- Translate english.txt file to hindi.txt file
- Generate Audio MP3 file from translated hindi.txt file

![High level architecture](./design/high_level_architecture.jpg)

This project consists of: 

- **py_poc**: POC python project
- **api**: FastAPI rest service
- **ui**: React, Typescript based app for UI interface

## Important Links
- [OpenAI API Dashboard page](https://platform.openai.com)
- [UV homepage](https://docs.astral.sh/uv/)
- [OpenAI speech to text docs](https://platform.openai.com/docs/guides/speech-to-text)
- [Pytubefix docs page](https://pypi.org/project/pytubefix/)
- [Using Gemini to transcribe video](https://www.youtube.com/watch?v=L3qAzagAtCs)


## Test Data

- [Youtube Sample Video for Transcribe](https://www.youtube.com/watch?v=SEQcdGkzmo4)


## OpenAI API Key generation

- Login to [OpenAI API dashboard](https://platform.openai.com)
- Login using SSO (pramod.jingade@gmail.com)
- Navigate under `your profile` -> `API keys` -> `+ Create new secret key`
- Documentation for speech to text can be found in [OpenAI speech to text](https://platform.openai.com/docs/guides/speech-to-text)

## Pre-requisite

The following are the pre-requisite to run the project

#### 1. OpenAI API Key
You need to setup a `.env` file with the following key

> NOTE: OpenAI requires you have credits to use audio-text transcribe and TTS conversion features

```bash
# create .env at root folder

# your openai api key
OPENAI_API_KEY=<your-openai-api-key>
```

#### 2. Create a `downloads` folder

All the audio mp3 files and transcribed text get stored in the downloads folder


## OpenAI Costs

- Cost to transcribe 37 min audio (MP3 file)
  - Cost: $0.22
  - Time: ~1.5 mins
- Cost for TTS conversion and generate audio -> .mp3 file (into Hindi)
  - Cost: ??
  - Time: ??
