# 🧠 Mental Health Semantic Searcher

A project to make mental health advice from dense books more accessible through semantic search and quote-level retrieval.

## ✨ Motivation

When you're dysregulated, skimming a whole book or even a chapter can feel overwhelming. This tool helps you search for **therapeutically helpful language** based on what you're feeling or trying to express — so you can find quotes, not just concepts.

---

## ⚙️ Tech Stack

- **Python** – backend logic + semantic chunking
- **Azure AI Search** – vector search. rejected: Pinecone, FAISS, Vilvus
- **Vector Embeddings** - voyage 3.5. chosen for: intent, emotional, concept rich embedding. rejected: openai (too literal), cohere (unemotional), MPnet MiniLM (poor purpose handling), Google USE (too generic for quote level lookup)
- **Gradio** – frontend interface. Options rejected: streamlit, dash, next.js, react.
- **GitHub Actions** – CI pipeline
- **pytest** – test framework

---

## 📂 Project Structure

```
frontend/    # User interface (Streamlit or React)
backend/     # API + semantic search logic
data/        # Sample books and chunked quote data
notebooks/   # R&D, experiments, visualizations
scripts/     # Setup scripts, evaluators
```

---

## 🚧 Status

- [x] Repo initialized with CI
- [x] Project scaffolded
- [ ] Semantic chunker implemented
- [ ] Retrieval working end-to-end
- [ ] Frontend MVP

---

## 🧪 Running Tests

```bash
pip install -r requirements.txt
pytest
