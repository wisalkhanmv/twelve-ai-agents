import os
from openai import OpenAI

def get_client():
    """
    Creates and returns an OpenAI client.
    Make sure to set OPENAI_API_KEY environment variable.
    """
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))