from langchain.text_splitter import RecursiveCharacterTextSplitter
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Read the full text from the file saved in Step 1
with open("text.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

# Set up the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=5000,      
    chunk_overlap=500      
)

# Perform splitting
chunks = splitter.split_text(full_text)

# Print some stats
print(f"✅ Total chunks created: {len(chunks)}")
print("\n🔍 Preview of 1st chunk:\n")
print(chunks[0])

# Optional: Save chunks for next step
with open("chunks.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        f.write(f"\n--- Chunk {i+1} ---\n{chunk}\n")
