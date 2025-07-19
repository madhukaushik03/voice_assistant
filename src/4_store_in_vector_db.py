import pickle
import faiss
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Load embeddings and text chunks
with open("embeddings.pkl", "rb") as f:
    chunks, embeddings = pickle.load(f)

# Convert to numpy array
embedding_array = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embedding_array.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
index.add(embedding_array)

# Save index for future querying
faiss.write_index(index, "faiss_index.index")

# Save chunks separately (if not already saved)
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print(f"✅ Stored {len(embeddings)} embeddings in FAISS index (dimension = {dimension})")

