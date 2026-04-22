# 📄 RAG Document Q&A System

An end-to-end **Retrieval Augmented Generation (RAG)** pipeline that lets users upload any PDF and ask natural language questions about it — powered by Google Gemini AI.

🚀 **Live Demo:** [huggingface.co/spaces/Karthik1018/rag-document-qa](https://huggingface.co/spaces/Karthik1018/rag-document-qa)

---

## 🎯 Business Problem

Large organizations in financial services and insurance deal with thousands of policy documents, compliance reports, and internal knowledge bases. Finding specific information manually is slow, error-prone, and expensive. This RAG system enables **employees and analysts to ask plain English questions and get instant, accurate answers from any document** — without reading through hundreds of pages.

**Real-world applications at insurance and financial companies:**
- Policy document Q&A for agents and brokers
- Compliance document search and summarization
- Internal knowledge base querying for faster decision-making
- Customer-facing chatbots grounded in official policy documents

---

## 🧠 What is RAG?

RAG combines the power of a **vector database** (for searching your documents) with a **large language model** (for generating answers). Instead of relying on general knowledge, the model answers based strictly on your uploaded document — making it accurate, reliable, and auditable.

```
User uploads PDF
      ↓
Document split into chunks → stored in ChromaDB (vector database)
      ↓
User asks a question
      ↓
System retrieves the 3 most relevant chunks
      ↓
Gemini AI reads those chunks and generates an accurate answer
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Google Gemini 1.5 Pro (via Vertex AI) |
| **Embeddings** | Vertex AI text-embedding-005 |
| **Vector Database** | ChromaDB |
| **Orchestration** | LangChain |
| **Frontend** | Streamlit |
| **Containerization** | Docker |
| **Deployment** | HuggingFace Spaces |

---

## ✨ Features

- 📤 Upload any PDF document
- 💬 Ask natural language questions about the document
- 🔍 Semantic search across document chunks
- 🤖 Context-aware answers using Gemini AI
- 🐳 Fully containerized with Docker
- ☁️ Deployed and accessible via public URL

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Streamlit UI  │────▶│   LangChain  │────▶│    ChromaDB     │
│  (File Upload + │     │ (Orchestrate)│     │ (Vector Store)  │
│   Q&A Interface)│     └──────┬───────┘     └─────────────────┘
└─────────────────┘            │
                               ▼
                    ┌──────────────────────┐
                    │  Google Gemini 1.5   │
                    │  Pro (Vertex AI)     │
                    └──────────────────────┘
```

---

## 📊 Results

- Successfully indexes and searches multi-page PDF documents
- Provides accurate, context-grounded answers
- Handles diverse document types: policy documents, research papers, reports, compliance manuals
- Zero hallucination risk — answers are strictly grounded in uploaded content

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Google Cloud account with Vertex AI enabled
- Google Cloud API key

### Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/Karthik-Mudenahalli-Ashoka/rag-document-qa.git
cd rag-document-qa
```

**2. Create virtual environment**
```bash
python3.11 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp .env.example .env
# Add your Google Cloud API key to .env
```

**5. Run the app**
```bash
python -m streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

### Run with Docker
```bash
docker build -t rag-app .
docker run -p 8501:8501 -e GOOGLE_CLOUD_API_KEY=your_key_here rag-app
```

---

## 📁 Project Structure

```
rag-document-qa/
│
├── app.py              # Main Streamlit application
├── ingest.py           # PDF loading and ChromaDB ingestion
├── qa_chain.py         # Question answering chain
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── .env.example        # Environment variables template
└── README.md           # Project documentation
```

---

## 🔮 Future Improvements

- Support for multiple PDF uploads simultaneously
- Chat history and multi-turn conversations
- Support for DOCX, TXT, and CSV files
- User authentication and personal document storage
- Fine-tuned embeddings for domain-specific documents (insurance, legal, compliance)
- Integration with enterprise knowledge bases via Azure Cognitive Search

---

## 👥 Authors

**Karthik Mudenahalli Ashoka**
- MS in Applied Artificial Intelligence — Data Engineering Concentration
- Stevens Institute of Technology
- [LinkedIn](https://www.linkedin.com/in/m-a-karthik/) | [GitHub](https://github.com/Karthik-Mudenahalli-Ashoka)

**Sirisha Manjunathan**
- MS in Data Science, Stevens Institute of Technology
- [LinkedIn](https://www.linkedin.com/in/sirisha-m-970206238/) | [GitHub](https://github.com/sirishavasisht)

---

## 📄 License

This project is licensed under the MIT License.
