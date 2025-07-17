# 🚀 Deployment Instructions

## 🐳 Backend (FastAPI)

### Local (Dockerized)
```bash
docker build -t quote-searcher .
docker run -p 7860:7860 quote-searcher