from langchain.embeddings import HuggingFaceEmbeddings
import pickle
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Read chunks created in previous step
with open("chunks.txt", "r", encoding="utf-8") as f:
    chunks_raw = f.read()

# Re-split into individual chunks
chunks = [chunk.strip() for chunk in chunks_raw.split("\n--- Chunk") if chunk.strip()]

# Initialize LangChain's Hugging Face embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Generate embeddings
print("🔄 Generating embeddings...")
embeddings = embedding_model.embed_documents(chunks)

print(f"✅ Generated {len(embeddings)} embeddings")

# Save embeddings + chunks for next step
with open("embeddings.pkl", "wb") as f:
    pickle.dump((chunks, embeddings), f)

print("💾 Saved to 'embeddings.pkl'")
