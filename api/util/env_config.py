"""
   module for loading
   env variables 
"""
import os
from dotenv import load_dotenv

# load from .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") or ""
OPENAI_DEFAULT_MODEL = os.environ.get("OPENAI_DEFAULT_MODEL") or "gpt-4.1"
