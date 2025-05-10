from pathlib import Path
from pypdf import PdfReader
from langchain.docstore.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def get_document_text(file_path, title=None):
    docs = []
    fname = file_path.name if hasattr(file_path, 'name') else str(file_path)
    if not title:
        title = os.path.basename(fname)

    pdf_reader = PdfReader(file_path)
    for num, page in enumerate(pdf_reader.pages):
        page_text = page.extract_text()
        doc = Document(page_content=page_text, metadata={'title': title, 'page': (num + 1)})
        docs.append(doc)

    return docs

def load_and_split_docs(data_dir="data"):
    docs = []
    paths = Path(data_dir).glob('**/*.pdf')
    for path in paths:
        this_lst = get_document_text(path)
        docs += this_lst
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
    return splitter.split_documents(docs)