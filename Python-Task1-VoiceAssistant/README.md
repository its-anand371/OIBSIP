# Voice Assistant

**Oasis Infobyte Summer Internship Program**
**Track:** Python Programming | **Task 1** | **Beginner Tier**

## Objective

This project is a Python-based voice assistant that listens to spoken commands through your microphone and responds with useful actions. It can greet users, tell the current time and date, search the web, and provide spoken feedback for every response.

## Technologies Used

- Python 3
- `speech_recognition` for converting microphone audio to text using Google Web Speech API
- `pyttsx3` for offline text-to-speech responses
- `datetime` for retrieving the current time and date
- `webbrowser` for opening searches in the default browser

## Features

- Captures voice input from the default microphone
- Responds to greetings such as "hello"
- Tells the current time
- Tells the current date
- Searches the web for requested topics
- Handles unclear speech without crashing
- Speaks and prints every response
- Continues running until the user says "exit" or "stop"

## Setup

```bash
# 1. Clone the repo and enter this folder
cd OIBSIP/Python-Task1-VoiceAssistant

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

> **Note on PyAudio:** PyAudio depends on the system-level `portaudio` library.
> - **macOS:** `brew install portaudio` or `conda install -c conda-forge portaudio`, then `pip install pyaudio`
> - **Windows:** `pip install pyaudio` usually works directly
> - **Linux:** `sudo apt-get install python3-pyaudio portaudio19-dev` then `pip install pyaudio`

## Usage

```bash
python Voice_Assistant.py
```

Once you see `I am Listening...`, speak naturally:

| Say...                        | Assistant does...                     |
|--------------------------------|----------------------------------------|
| "Hello"                        | Greets you back                        |
| "What's the time?"             | Speaks the current time                |
| "What's today's date?"         | Speaks the current date                |
| "Search for python tutorials"  | Opens a Google search in your browser  |
| "Exit" / "Stop"                | Says goodbye and ends the program      |

## Project Structure

```
OIBSIP/Python-Task1-VoiceAssistant/
├── Voice_Assistant.py   # main application
├── requirements.txt     # dependencies
└── README.md            # this file
```

---
*Submitted as part of the Oasis Infobyte Summer Internship Program (SIP).*
