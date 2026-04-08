# Voice Assistant

A Python-based voice assistant that listens to spoken commands and responds using text-to-speech. Built as part of my AI Internship at SyntecxHub.

## What It Does

- Listens to voice input via microphone using SpeechRecognition
- Maps commands to actions using rule-based command matching
- Responds out loud using pyttsx3 text-to-speech
- Handles errors gracefully with clear spoken feedback

## Supported Commands

| Command | Action |
|---|---|
| "what time is it" | Speaks the current time |
| "what is the date" | Speaks today's date |
| "open youtube" | Opens YouTube in browser |
| "open google" | Opens Google in browser |
| "open github" | Opens GitHub in browser |
| "search [query]" | Searches Google for your query |
| "open notepad" | Opens Notepad (Windows) |
| "open calculator" | Opens Calculator (Windows) |
| "tell me a joke" | Tells a programming joke |
| "help" / "commands" | Lists all available commands |
| "exit" / "stop" / "quit" | Closes the assistant |

## How It Works

Every voice input goes through 3 steps:

1. **Listen** — Microphone captures audio, Google Speech API converts it to text
2. **Match** — Text is checked against a rule map of known commands
3. **Respond** — The matched action runs and pyttsx3 speaks the result

## Project Structure

```
voice-assistant/
├── assistant.py       # Main Python script
└── screenshots/       # Terminal and demo screenshots
```

## How To Run

**Install dependencies:**

```
pip install SpeechRecognition pyttsx3 pyaudio
```


**Run the assistant:**

```
python assistant.py
```

> Make sure your microphone is connected and you have an active internet connection (required for Google Speech Recognition).

## Sample Output

```
Assistant: Hello! I am your voice assistant. Say 'help' to hear what I can do.
🎤 Listening... (speak now)
You said: what time is it
Assistant: The current time is 03:45 PM.

🎤 Listening... (speak now)
You said: open calculator
Assistant: Opening Calculator

🎤 Listening... (speak now)
You said: exit
Assistant: Goodbye! Have a great day.
```

## Tech Stack

- **Language:** Python 3.x
- **Speech-to-Text:** SpeechRecognition (Google Speech API)
- **Text-to-Speech:** pyttsx3 (offline)
- **Browser Automation:** webbrowser (built-in)
- **Libraries:** datetime, os, webbrowser (built-in)

## 🖼️ Screenshots
<img width="1179" height="623" alt="image" src="https://github.com/user-attachments/assets/69e80e9d-783e-4b0e-b372-bfae764af570" />
<img width="1179" height="614" alt="image" src="https://github.com/user-attachments/assets/c2cab58d-c858-4933-bed0-d68bec3cd099" />


## 👤 Author

Asna Haris — AI Intern at SyntecxHub

- GitHub: [asnahar1s](https://github.com/asnahar1s)
- LinkedIn: [asna-haris-684058319](https://www.linkedin.com/in/asna-haris-684058319)


## 📄 License

This project is built as part of my AI Internship Program at SyntecxHub.

Website: https://syntecxhub.com/
