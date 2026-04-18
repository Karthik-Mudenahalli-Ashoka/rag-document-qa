import streamlit as st
import tempfile
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from typing import List
from google import genai

load_dotenv()

# Same custom LLM from qa_chain.py
class GoogleGenAIChat(BaseChatModel):
    model: str = "gemini-3.1-pro-preview"

    def _generate(self, messages: List[BaseMessage], stop=None, run_manager=None, **kwargs) -> ChatResult:
        client = genai.Client(
            vertexai=True,
            api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"),
        )
        prompt = messages[-1].content
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        message = AIMessage(content=response.text)
        return ChatResult(generations=[ChatGeneration(message=message)])

    @property
    def _llm_type(self) -> str:
        return "google-genai"

# Page config
st.set_page_config(page_title="📄 Ask Your Documents", page_icon="📄")
st.title("📄 Ask Your Documents")
st.write("Upload a PDF and ask any question about it")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Reading and indexing your document..."):
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            f.write(uploaded_file.read())
            tmp_path = f.name

        # Load and split
        loader = PyPDFLoader(tmp_path)
        pages = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(pages)

        # Embed and store
        embeddings = VertexAIEmbeddings(model_name="text-embedding-005")
        vectorstore = Chroma.from_documents(chunks, embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # Build chain
        llm = GoogleGenAIChat()
        prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the context below.

Context: {context}

Question: {question}
""")
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

    st.success(f"✅ Document ready! ({len(chunks)} chunks indexed)")

    # Question input
    question = st.text_input("Ask a question about your document:")

    if question:
        with st.spinner("Thinking..."):
            answer = chain.invoke(question)
        st.markdown("### 🤖 Answer")
        st.write(answer)