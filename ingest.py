from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_vertexai import VertexAIEmbeddings

load_dotenv()

loader = PyPDFLoader("docs/sample.pdf")
pages = loader.load()
print(f"✅ Loaded {len(pages)} pages")

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(pages)
print(f"✅ Split into {len(chunks)} chunks")

embeddings = VertexAIEmbeddings(model_name="text-embedding-005")
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
print(f"✅ Stored in ChromaDB successfully!")