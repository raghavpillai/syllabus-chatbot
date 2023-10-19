import openai
from dotenv import load_dotenv
import os, sys

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# load tokenized pdf from ../resources - agnostic from where script called
# script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
# target_file_path = os.path.join(script_directory, '..', 'resources', 'cs4349_chida.txt')
# with open(target_file_path, 'r') as file:
#     SYLLABUS_TEXT = file.read()

class OpenAI:
    @staticmethod
    def get_completion(messages: list[dict]):
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return completion.choices[0].message.content

if __name__ == '__main__':
    print(OPENAI_API_KEY)
    # print(SYLLABUS_TEXT)
    print(OpenAI.get_completion([{"role": "user", "content": "whats merge sort"}]))