from config.paths import DOCUMENT_PATHS

def to_text(pages):
    path=DOCUMENT_PATHS.get('TEXT')
    
    cont=''
    if path:
        for doc in pages:
            cont=cont+f'{doc.page_content}\next_page'
        
        with open(path, 'w') as f:
            f.write(cont)
    else:
        ValueError(f'Text file is not saved!!!')

    return None