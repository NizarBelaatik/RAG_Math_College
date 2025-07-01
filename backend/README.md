# 📘 Math RAG Backend

A FastAPI-powered backend for retrieving math questions and solutions using hybrid semantic search (HuggingFace embeddings + FAISS). Optimized for performance with optional GPU acceleration.

---

## 🚀 Features

- 🔍 **Hybrid semantic/keyword search**
- 🧠 **HuggingFace Transformers embeddings**
- ⚡ **GPU-accelerated using PyTorch (if available)**
- 🧭 **FAISS vector index storage**
- 🔐 **Supports metadata filtering**

---

## 🧰 Technologies Used

- **Python 3.10+**
- **FastAPI**
- **LangChain + HuggingFace**
- **FAISS**
- **PyTorch**
- **Uvicorn**

---

## 📁 Project Structure


```

math\_rag\_backend/
├── app/
│   ├── **init**.py
│   ├── main.py          # FastAPI app entry point
│   ├── models.py        # Request/Response schemas
│   ├── rag\_system.py    # RAG search system logic
│   └── config.py        # Optional config file
├── math\_college\_index/  # FAISS vector index (prebuilt)
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/math-rag-backend.git
cd math-rag-backend
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Embedding Model (Optional)

Only needed if you haven't loaded the model before.

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')"
```

### 5. Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server will run on: `http://localhost:8000`

---

## 🔌 API Endpoints

| Endpoint  | Method | Description                     |
| --------- | ------ | ------------------------------- |
| `/search` | POST   | Perform a hybrid search         |
| `/health` | GET    | Check if the backend is running |

### ✅ `/search` Example Request:

**POST** `/search`

```json
{
  "query": "What is the integral of x^2?",
  "k": 3,
  "filters": null
}
```

**Response:**

```json
[
  {
    "question": "What is the integral of x^2?",
    "solution": "The integral of x^2 is (1/3)x^3 + C.",
    "metadata": {
      "subject": "calculus"
    }
  },
  ...
]
```

---

## ⚙️ Configuration

Customize FAISS index path and model inside `app/config.py` if needed.

```python
# Example config.py
INDEX_PATH = "math_college_index"
```

---

## 💡 Notes

* Make sure your `math_college_index/` contains the pre-generated FAISS index files.
* CORS is enabled for `http://localhost:3000` to allow React frontend integration.

---

## 👨‍💻 Author

Built for educational math retrieval and AI search experimentation.
