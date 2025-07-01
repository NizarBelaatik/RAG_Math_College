from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from typing import Optional, Dict, List
import torch
from .config import INDEX_PATH

class MathRAGSystem:
    def __init__(self, index_path: str = "math_college_index"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            model_kwargs={"device": self.device}
        )
        self.vectorstore = FAISS.load_local(
            INDEX_PATH,#index_path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )

    def hybrid_search(self, query: str, k: int = 3, filters: Optional[Dict] = None) -> List[Dict]:
        results = self.vectorstore.similarity_search(query, k=k, filter=filters)
        return [
            {
                "question": doc.page_content.split("\nSolution:")[0].replace("Question:", "").strip(),
                "solution": doc.page_content.split("\nSolution:")[1].strip() if "\nSolution:" in doc.page_content else "",
                "metadata": doc.metadata
            }
            for doc in results
        ]
