# 🧙 Mythical Creatures AI Chat App

An immersive real-time AI-powered voice experience where users can **speak and interact** with mythical characters — including a dragon, elf, and goblin — using natural voice conversations.

Built with **Streamlit**, **open-source LLMs**, **Edge TTS**, and **Vosk**, this app brings characters to life with spoken introductions, back-and-forth dialogue, and a sleek fantasy-style UI.

---

## ✨ Features

- 🎭 Choose from 3 characters: Dragon, Elf, Goblin
- 🗣️ Real-time **voice input** using `Vosk` (offline STT)
- 💬 AI-powered natural language responses using **open-source models** (local or Together API)
- 🔊 Real-time **text-to-speech** using `Edge TTS`
- 🎤 "Listening..." & 🗣️ "Speaking..." states for realism
- 🧝 Static avatar display per character
- 🌒 Dark themed UI with stylized buttons and layout
- ❌ End chat anytime by saying "stop" or pressing "End Chat"
- 🧱 Modular OOP design for easy extension

---

## 📁 Project Folder Structure

LLM-Powered Conversational Avatar Interface
│
├── app_streamlit.py # Main Streamlit UI app
├── voice_input.py # Real-time STT using Vosk
├── text_to_speech.py # TTS using Edge TTS
├── requirements.txt # All Python dependencies
├── README.md # You're reading it!
│
├── avatars/ # Character avatars (PNG)
│ ├── dragon.png
│ ├── elf.png
│ └── goblin.png
│
└── creatures/ # OOP classes per character
├── init.py
├── dragon.py
├── elf.py
└── goblin.py


---

## 🔧 Tech Stack
LLM-Powered Conversational Avatar Interface
| Category              | Technology |
|-----------------------|------------|
| UI                    | [Streamlit](https://streamlit.io) (Python-based frontend) |
| Speech Recognition    | [Vosk](https://alphacephei.com/vosk/) (Offline STT engine) |
| Text-to-Speech (TTS)  | [Edge-TTS](https://github.com/rany2/edge-tts) (Microsoft Edge neural voices) |
| Language Model (AI)   | [Together AI](https://www.together.ai/) API (Mixtral, LLaMA, Mistral) or HuggingFace Transformers |
| Audio Playback        | `playsound` |
| Design Philosophy     | Modular, Object-Oriented Python (OOP) |

---

## 🚀 How to Run the App
## 🛠️ Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/aiza-ch/LLM-Powered-Conversational-Avatar-Interface.git
cd LLM-Powered-Conversational-Avatar-Interface

Install dependencies:
pip install -r requirements.txt

Set your API key
Create a file called config.py and add your Together API key like this:
TOGETHER_API_KEY = "your-api-key-here"

Run the app:
streamlit run app_streamlit.py
