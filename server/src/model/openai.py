import openai
from dotenv import load_dotenv
import os, sys

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# load tokenized pdf from ../resources - agnostic from where script called
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
target_file_path = os.path.join(script_directory, '..', 'resources', 'cs4349_chida.txt')
with open(target_file_path, 'r') as file:
    SYLLABUS_TEXT = file.read()

class OpenAI:
    def __init__(self):
        pass

if __name__ == '__main__':
    print(OPENAI_API_KEY)
    print(SYLLABUS_TEXT)