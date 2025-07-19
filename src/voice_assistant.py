import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import importlib.util
import time
import os
import random
import string

WAKE_WORD = "alexa"

# Load query_bot from 5_query_bot.py
def import_query_function():
    spec = importlib.util.spec_from_file_location("query_bot", "5_query_bot.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.query_bot

# Speak function using gTTS
def speak(text):
    print(f"🤖 Bot: {text}")
    try:
        # Create a unique filename for each response
        filename = ''.join(random.choices(string.ascii_lowercase, k=8)) + ".mp3"
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)
        playsound(filename)
        os.remove(filename)  # Delete after playing
    except Exception as e:
        print(f"⚠️ TTS Error: {e}")

def listen_for_phrase():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"🎧 Listening for wake word... (say '{WAKE_WORD}')")
        audio = recognizer.listen(source)
    try:
        phrase = recognizer.recognize_google(audio).lower()
        return phrase
    except:
        return ""

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for your question...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣 You said: {command}")
        return command
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio.")
        return None
    except sr.RequestError:
        print("⚠️ STT service unavailable.")
        return None

if __name__ == "__main__":
    query_bot = import_query_function()
    speak(f"Voice assistant is active. Say '{WAKE_WORD}' to wake me up.")
    
    while True:
        phrase = listen_for_phrase()
        if WAKE_WORD in phrase:
            speak("Yes, I'm listening. What's your question?")
            question = listen_for_command()
            
            if question and question.lower() in ["exit", "quit", "stop"]:
                speak("Goodbye!")
                break
            
            if question:
                response = query_bot(question)
                speak(response)
                print("✅ Back to wake mode.\n")
            else:
                speak("Sorry, I didn't catch that.")
        else:
            time.sleep(1)  # Avoid busy looping
