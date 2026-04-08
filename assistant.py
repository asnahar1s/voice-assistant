import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# ─── Text to Speech ────────────────────────────────────────────
def speak(text):
    """Convert text to speech."""
    print(f"Assistant: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ─── Listen to microphone ────────────────────────────────────────
def listen():
    """Capture voice input and return as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            speak("Speech service is unavailable. Check your internet connection.")
        return ""

# ─── Map commands to actions ─────────────────────────────────────
def process_command(command):
    """Map voice command to an action."""
    if not command:
        return

    # Tell time
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")

    # Tell date
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}.")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    # Open Google
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    # Open GitHub
    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://www.github.com")

    # Search the web
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}.")
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        else:
            speak("What would you like me to search for?")

    # Open Notepad
    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")

    # Open Calculator
    elif "open calculator" in command:
        speak("Opening Calculator.")
        os.system("calc")

    # Greet user
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Tell a joke
    elif "joke" in command:
        speak("Why do programmers prefer dark mode? Because light attracts bugs!")

    # List available commands
    elif "help" in command or "commands" in command:
        speak("Here are some things I can do: tell the time, tell the date, open YouTube, open Google, open GitHub, search the web, open Notepad, open Calculator, tell a joke, or say hello.")

    # Exit
    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("Sorry, I don't know how to handle that command yet.")

# ─── Main loop ───────────────────────────────────────────────────
def main():
    speak("Hello! I am your voice assistant. Say help to hear what I can do, or exit to quit.")
    while True:
        command = listen()
        process_command(command)

if __name__ == "__main__":
    main()