# Math RAG Backend

FastAPI backend for math question retrieval.

## Features
- Hybrid semantic/keyword search
- Metadata filtering
- GPU-accelerated embeddings
- FAISS vector storage

## Technologies
- Python 3.10+
- FastAPI
- HuggingFace Transformers
- FAISS
- PyTorch 2.1+

## Setup
1. Install Python 3.10+
2. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Download embeddings model
   ```bash
   python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')"
   ```
5. Run server
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/search` | POST | Search math questions |
| `/health` | GET | Service health check |

## Configuration
Edit `config.py` for:
- FAISS index path
- Embedding model selection