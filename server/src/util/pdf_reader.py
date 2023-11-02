import os
import re
import PyPDF2

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_PATH = os.path.join(CURRENT_DIR, '..', 'resources')


class PDFReader:
    @classmethod
    def tokenize_pdf(cls) -> str:
        with open(f'{RESOURCE_PATH}/cs4349_chida.pdf', 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            num_pages = len(pdf_reader.pages)
            detected_text = ''

            for page_num in range(num_pages):
                page_obj = pdf_reader.pages[page_num]
                detected_text += page_obj.extract_text()

        cls.tokenized_pdf_text: str = re.sub(r'(\n\s*)+\n+', '\n\n', detected_text)
        print(f"Initialized PDF Reader with {num_pages} pages.")
        
        return detected_text