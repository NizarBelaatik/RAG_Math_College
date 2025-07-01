from pydantic import BaseModel
from typing import Dict, Optional, List

class SearchRequest(BaseModel):
    query: str
    filters: Optional[Dict] = None
    k: int = 3

class SearchResult(BaseModel):
    question: str
    solution: str
    metadata: Dict
