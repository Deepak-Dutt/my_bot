from pipeline.pdf_to_pages import to_pages
from pipeline.pages_to_text import to_text
from pipeline.text_to_chunks import to_chunks

pages=to_pages()
text=to_text(pages)
chunks=to_chunks(text)