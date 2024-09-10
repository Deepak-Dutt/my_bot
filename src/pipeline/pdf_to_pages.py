from langchain.document_loaders import PyPDFLoader
from config.paths import DOCUMENT_PATHS

def to_pages():
    path=DOCUMENT_PATHS.get('PDF')
    
    if path:
        loader=PyPDFLoader(path)
        pages=loader.load_and_split()
    else:
        ValueError(f'Path is not found')

    return pages