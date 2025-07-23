import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_script(script_name):
    print(f"\n🚀 Running: {script_name}")
    try:
        # Use sys.executable to ensure the correct Python (venv) is used
        result = subprocess.run(
            [sys.executable, script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        if result.stdout.strip():
            print(f"✅ STDOUT from {script_name}:\n{result.stdout.strip()}")
        if result.stderr.strip():
            print(f"⚠️ STDERR from {script_name}:\n{result.stderr.strip()}")
        if result.returncode != 0:
            print(f"❌ {script_name} exited with code {result.returncode}")
            sys.exit(result.returncode)  # Stop pipeline on failure
    except Exception as e:
        print(f"💥 Exception while running {script_name}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Step 1: Run preprocessing pipeline
    script_sequence = [
        "1_read_pdf.py",
        "2_split_chunks.py",
        "3_generate_embeddings.py",
        "4_store_in_vector_db.py",
    ]
    for script in script_sequence:
        run_script(script)

    print("\n✅ Preprocessing done!")
