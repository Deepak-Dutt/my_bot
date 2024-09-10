import nltk
from nltk.tokenize import sent_tokenize

#nltk.download('punkt')
#nltk.download('averaged_preception_tagger')

import pickle

from config.paths import DOCUMENT_PATHS

def to_chunks(text):
    clean_text=text.replace('\t', ' ').replace('\n', ' ').replace('\next', ' ')
    sentences=sent_tokenize(clean_text)
    chunks=[]
    chunk_size=5
    
    for i in range(0, len(sentences), chunk_size):
        chunk=sentences[i:i + chunk_size]
        chunks.append(chunk)
    
    path=DOCUMENT_PATHS.get('CHUNKS')
    with open(path, 'wb') as f:
        pickle.dump(chunks, f)

    for i in chunks:
        print(i)

    return chunks