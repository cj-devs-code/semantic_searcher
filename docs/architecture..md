# 🧠 System Architecture: Semantic Searcher

## 🔁 Data Flow Overview
1. User types a natural-language query in the Gradio UI
2. Gradio sends the query to a FastAPI backend via HTTP
3. Backend uses Voyage AI to generate a vector embedding
4. Embedding is sent to Azure AI Search (AAIS) for semantic retrieval
5. Top-k quotes and metadata are returned to the backend
6. Backend sends results to Gradio, which displays them

## 🧩 Component Breakdown

### Frontend
- **Tool**: Gradio (Python-based UI framework)
- **Responsibility**: Capture user queries, display quote results

### Backend
- **Tool**: FastAPI (Python async web server)
- **Responsibility**:
  - Accept query requests
  - Fetch embeddings via Voyage AI
  - Call Azure AI Search
  - Return ranked quote matches

### Vector Search
- **Service**: Azure AI Search
- **Index Type**: Vector + metadata
- **Function**: Store quote embeddings and return nearest neighbors

### Embeddings
- **Service**: Voyage AI (`voyage-3.5` model)
- **Why**: Tuned for conceptual, emotional, and intent-rich queries

## 🐳 Deployment Overview

| Component | Hosting Target        | Notes                      |
|----------|------------------------|----------------------------|
| Gradio UI | Hugging Face Spaces   | Lightweight, easy deploy   |
| Backend   | Render or HF Spaces   | Dockerized FastAPI         |
| Vector DB | Azure AI Search       | Managed, scalable          |

## 🔐 Environment Variables (Handled via `.env`)
- `VOYAGE_API_KEY`
- `AAIS_ENDPOINT`
- `AAIS_KEY`
- `RUNDOCKERTEST` (optional, for container testing mode)