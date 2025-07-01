from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import SearchRequest, SearchResult
from .rag_system import MathRAGSystem

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the RAG system at startup
rag_system = MathRAGSystem()

@app.get("/health")
async def health_check():
    return {"status": "healthy", "device": rag_system.device}

@app.post("/api/search", response_model=List[SearchResult])
async def search(request: SearchRequest):
    print(f"Received query: {request.query}")
    results = rag_system.hybrid_search(
        query=request.query,
        k=request.k,
        filters=request.filters
    )
    print(f"Returning {len(results)} results")
    return results


