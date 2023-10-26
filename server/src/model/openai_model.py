import os
import sys
import openai
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_PATH = os.path.join(CURRENT_DIR, '..', 'resources')

class OpenAI:
    @staticmethod
    def get_completion(messages: list[dict]):
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return completion.choices[0].message.content
    
    @classmethod
    def get_single_completion(cls, message: str) -> str:
        # cls.messages.append({"role": "user", "content": message})
        completion: openai.Completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # messages=cls.messages
            messages= [
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message.content
    
    @classmethod
    def initialize(cls) -> None:
        cls.messages: List[Dict[str, str]] = [{"role": "system", "content": "You are a useful teacher's assistant for an advanced algorithm's class"}]
        with open(f'{RESOURCE_PATH}/cs4349_chida.txt', 'r') as file:
            cls.syllabus_text = file.read()


if __name__ == '__main__':
    print(OPENAI_API_KEY)
    print(OpenAI.initialize())
    # print(OpenAI.get_completion([{"role": "user", "content": "whats merge sort"}]))