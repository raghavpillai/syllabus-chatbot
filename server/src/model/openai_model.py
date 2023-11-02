import os
import sys
import openai
from pathlib import Path
from dotenv import load_dotenv

from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from typing import List, Dict, Any, Tuple

current_dir = Path(__file__).resolve()
three_layers_up = current_dir.parents[2]
sys.path.append(str(three_layers_up))

from src.util.pdf_reader import PDFReader

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY
print(OPENAI_API_KEY)

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
        result: Dict[str, Any] = cls.conv_interface({"question": message,})
        # cls.chat_history.append((message, result["result"]))
        print(result["answer"])
        return result["answer"]
    
    @classmethod
    def initialize(cls) -> None:
        loader: PyMuPDFLoader = PyMuPDFLoader(f"{RESOURCE_PATH}/cs4349_chida.pdf")
        documents: List[Dict[str, Any]] = loader.load()

        text_splitter: CharacterTextSplitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts: List[Dict[str, Any]] = text_splitter.split_documents(documents)

        embeddings: OpenAIEmbeddings = OpenAIEmbeddings()
        vectordb: Chroma = Chroma.from_documents(documents=texts, 
                    embedding=embeddings,
                    persist_directory=CURRENT_DIR
        )
        vectordb.persist()

        llm: ChatOpenAI = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.3)
        cls.chat_history: List[Tuple[str, str]] = []

        # cls.conv_interface = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        cls.conv_interface = ConversationalRetrievalChain.from_llm(llm, vectordb.as_retriever(), memory=memory)


        cls.messages: List[Dict[str, str]] = [
            {"role": "system", "content": """You are a useful teacher's assistant for a class at the University of Texas at Dallas.
            A student can either ask a question about the coursework, or the syllabus. If it's the syllabus, directly cite the part(s) of the syllabus that pertains to the question.
            Below is the syllabus. Make sure every syllabus question is answered completely accurately, and if you cannot do so say you do not know the answer.
            """},
            {"role": "system", "content": ""}
        ]
        


if __name__ == '__main__':
    print(OPENAI_API_KEY)
    print("Lol")
    print(OpenAI.initialize())
    print(OpenAI.get_single_completion("what is this pdf"))
    print(OpenAI.get_single_completion("what are the pre-requisites for this class?"))
    # print(OpenAI.get_completion([{"role": "user", "content": "whats merge sort"}]))
