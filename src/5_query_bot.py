import pickle
import faiss
import numpy as np
import os
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set in .env file")

# Load FAISS vector index
index = faiss.read_index("faiss_index.index")

# Load stored document chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load embedding model (HuggingFace MiniLM)
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load Gemini Flash model via LangChain
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.2,
    google_api_key=API_KEY
)

def ask_question(question: str, top_k=3):
    # Step 1: Embed query
    question_embedding = np.array(embedder.embed_query(question), dtype="float32").reshape(1, -1)

    # Step 2: Search similar chunks
    distances, indices = index.search(question_embedding, top_k)
    relevant_chunks = [chunks[i] for i in indices[0]]
    context = "\n".join(relevant_chunks)

    # Step 3: Build prompt
    prompt = (
        "You are a helpful assistant bot that will provide information about the daily inventory, sales, expenses, and profit of the Polo Café. You ar designed to take question from the users and answer these questions in simple English. Answer questions based on extracted text from a PDF document.Your response must be clean text, without any formatting. You  give reponse in brief unless stated otherwise. \n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )

    # Step 4: Invoke Gemini model
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# Wrapper for main.py
def query_bot(question: str):
    return ask_question(question)

# CLI mode for text interaction
if __name__ == "__main__":
    while True:
        user_q = input("\n💬 Ask a question (or type 'exit'): ")
        if user_q.lower() == 'exit':
            break
        answer = ask_question(user_q)
        print(f"\n🤖 Answer:\n{answer}")
