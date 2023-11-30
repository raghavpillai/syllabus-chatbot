import os
import json
from openai import OpenAI
from PyPDF2 import PdfReader

from ..config import Config

OPENAI_API_KEY = Config.OPENAI_API_KEY
client: OpenAI = OpenAI(api_key=OPENAI_API_KEY)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_PATH = os.path.join(CURRENT_DIR, "..", "resources")


class OpenAIModel:
    messages: list[dict[str, str]] = []

    @classmethod
    def read_pdf(cls):
        with open(f"{RESOURCE_PATH}/cs4349_chida.pdf", "rb") as f:
            reader: PdfReader = PdfReader(f)
            text: str = "".join(page.extract_text() for page in reader.pages)
        return text

    @classmethod
    def initialize(cls):
        cls.messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": """You are a useful teacher's assistant for a class at the University of Texas at Dallas.
            You should not say you're an AI, instead your name is Alice.
            A student can either ask a question about the coursework, or the syllabus. If it's the syllabus, directly cite the part(s) of the syllabus that pertains to the question.
            Wrap all LaTeX equations or output in $, for example $y = mx + b$
            Below is the syllabus. Make sure every syllabus question is answered completely accurately, and if you cannot do so say you do not know the answer.
            """,
            },
            {"role": "system", "content": cls.read_pdf()},
        ]

    @classmethod
    def ask_question_single(cls, prompt: str) -> str:
        try:
            cls.messages.append({"role": "user", "content": prompt})
            response: dict = client.chat.completions.create(
                model='gpt-4-1106-preview',
                # model="gpt-3.5-turbo",
                messages=cls.messages,
            )
            response_content: str = response.choices[0].message.content
            cls.messages.append({"role": "assistant", "content": response_content})
            return response_content
        except Exception as e:
            return str(e)

    @classmethod
    def ask_question_stream(cls, prompt: str):
        try:
            cls.messages.append({"role": "user", "content": prompt})
            response: dict = client.chat.completions.create(
                model="gpt-4-1106-preview", messages=cls.messages, stream=True
            )
            response_text: str = ""
            yield json.dumps({"type": "start", "content": True})
            for chunk in response:
                content: str = chunk.choices[0].delta.content or ""
                if content is None:
                    continue
                response_text += content

                yield json.dumps({"type": "partial", "content": response_text})

            cls.messages.append({"role": "assistant", "content": response_text})
            yield json.dumps({"type": "full", "content": response_text})
            print("Answer: ", response_text)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    OpenAIModel.initialize()
    answer: str = OpenAIModel.ask_question("What is the policy on Make-Up Exams?")
    print(answer)
