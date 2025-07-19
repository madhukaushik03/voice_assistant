import subprocess
import sys
# import speech_recognition as sr
# import pyttsx3
import importlib.util

sys.stdout.reconfigure(encoding='utf-8')

def run_script(script_name):
    print(f"\n🚀 Running: {script_name}")
    try:
        result = subprocess.run(
            ['python', script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        if result.stdout:
            print(f"✅ STDOUT from {script_name}:\n{result.stdout}")
        if result.stderr:
            print(f"⚠️ STDERR from {script_name}:\n{result.stderr}")
        if result.returncode != 0:
            print(f"❌ {script_name} exited with code {result.returncode}")
    except Exception as e:
        print(f"💥 Exception while running {script_name}: {e}")

# Import query function from 5_query_bot.py
# def import_query_function():
#     spec = importlib.util.spec_from_file_location("query_bot", "5_query_bot.py")
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     return module.query_bot  # Ensure 5_query_bot.py has a function named query_bot

# # Initialize TTS engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Listening... (say 'exit' to quit)")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio)
#         print(f"🗣 You said: {text}")
#         return text
#     except sr.UnknownValueError:
#         print("⚠️ Could not understand audio.")
#         return None
#     except sr.RequestError:
#         print("⚠️ STT service unavailable.")
#         return None

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

    # Step 2: Voice Assistant Interaction
    # print("\n✅ Preprocessing done! Starting Voice Assistant...")
    # query_bot = import_query_function()

    # while True:
    #     user_input = listen()
    #     if user_input and user_input.lower() in ["exit", "quit", "stop"]:
    #         print("👋 Exiting voice assistant.")
    #         speak("Goodbye!")
    #         break
    #     if user_input:
    #         response = query_bot(user_input)  # Call chatbot logic
    #         print(f"🤖 Bot: {response}")
    #         speak(response)
