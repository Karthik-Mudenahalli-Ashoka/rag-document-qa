from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from google import genai
from google.genai import types
import os

load_dotenv()

# Custom LLM wrapper using the new google-genai SDK
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from typing import Any, List, Optional

class GoogleGenAIChat(BaseChatModel):
    model: str = "gemini-2.0-flash"
    
    def _generate(self, messages: List[BaseMessage], stop=None, run_manager=None, **kwargs) -> ChatResult:
        client = genai.Client(
            vertexai=True,
            api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"),
        )
        # Get the last message content
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

load_dotenv()

# Embeddings
embeddings = VertexAIEmbeddings(model_name="text-embedding-005")
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Use new SDK
llm = GoogleGenAIChat(model="gemini-3.1-pro-preview")

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

question = "What is this document about?"
print(f"\n🙋 Question: {question}")
answer = chain.invoke(question)
print(f"\n🤖 Answer: {answer}")