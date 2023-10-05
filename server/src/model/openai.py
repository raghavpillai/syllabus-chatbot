import openai
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class OpenAI:
    def __init__(self):
        pass

if __name__ == '__main__':
    print(OPENAI_API_KEY)