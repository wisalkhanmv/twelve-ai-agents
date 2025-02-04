import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_client():
    """
    Creates and returns an OpenAI client.
    Make sure to set OPENAI_API_KEY environment variable.
    """
    key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=key)