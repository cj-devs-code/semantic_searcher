# 🚧 Roadmap: Semantic Searcher

## ✅ MVP Goals
- [x] Pick appropriate book for start
- [x] Set up clean repo structure (frontend/, backend/, etc.)
- [x] Add CI pipeline with GitHub Actions
- [x] Create `.env.example` and document secrets in README
- [x] Add Gradio frontend scaffold
- [X] Add Docker deployment for backend
- [ ] Add tests for quote retrieval from book.
- [ ] Install and configure Voyage AI embeddings
- [ ] Implement `POST /search` endpoint in FastAPI
- [ ] Create Azure AI Search instance
- [ ] Semantic chunk book for embeddings with Voyage AI
- [ ] Send embeddings to Azure AI Search for top-k retrieval
- [ ] Connect Gradio frontend to backend via `requests`
- [ ] Return results and display top matches in UI

## 🔮 Near-Term Enhancements
- [ ] Deploy backend to Hugging Face Spaces or Render

## 🚀 Future Directions
- [ ] Add support for audio input (e.g., voice search)
- [ ] Add user feedback collection loop
- [ ] Expand pdf embeddings 