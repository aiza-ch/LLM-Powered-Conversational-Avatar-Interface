import streamlit as st
from voice_input import get_voice_input
from text_to_speech import speak_text
from creatures.dragon import Dragon
from creatures.elf import Elf
from creatures.goblin import Goblin

# Character and avatar setup
creature_classes = {
    "Dragon": Dragon,
    "Elf": Elf,
    "Goblin": Goblin
}
avatars = {
    "Dragon": "avatars/dragon.png",
    "Elf": "avatars/elf.png",
    "Goblin": "avatars/goblin.png"
}

# UI styling
st.set_page_config(page_title="🧙 Mythical Creatures AI", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: #e0e0f0;
    }
    .stButton > button {
        color: white;
        background-color: #5a189a;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #7b2cbf;
    }
    .status-box {
        padding: 10px;
        border-radius: 8px;
        background-color: #2a2a40;
        color: #f1f1f1;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Session state
if "creature_choice" not in st.session_state:
    st.session_state.creature_choice = None
if "creature" not in st.session_state:
    st.session_state.creature = None
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "is_speaking" not in st.session_state:
    st.session_state.is_speaking = False
if "voice" not in st.session_state:
    st.session_state.voice = "en-GB-RyanNeural"
if "intro_spoken" not in st.session_state:
    st.session_state.intro_spoken = False

# App title
st.title("🧝 Mythical Creatures AI")

# Character selection screen
if not st.session_state.chat_started:
    st.subheader("🧙 Choose Your Guide")
    creature_choice = st.selectbox("Select a mythical character:", list(creature_classes.keys()))
    if st.button("🔮 Begin Chat"):
        st.session_state.creature_choice = creature_choice
        st.session_state.creature = creature_classes[creature_choice]()
        st.session_state.chat_started = True
        st.session_state.conversation = []
        st.session_state.intro_spoken = False
        st.rerun()

# Chat UI
if st.session_state.chat_started:
    creature_choice = st.session_state.creature_choice
    st.subheader(f"🎭 Now Speaking to the {creature_choice}")

    # Avatar display
    st.image(avatars[creature_choice], width=250)

    # Speak the intro once
    if not st.session_state.intro_spoken:
        intro = st.session_state.creature.introduce()
        st.session_state.conversation.append((creature_choice, intro))
        st.session_state.is_speaking = True
        st.markdown('<div class="status-box">🗣️ Speaking...</div>', unsafe_allow_html=True)
        speak_text(intro, st.session_state.voice)
        st.session_state.is_speaking = False
        st.session_state.intro_spoken = True
        st.rerun()

    # Show current status
    if st.session_state.is_speaking:
        st.markdown('<div class="status-box">🗣️ Speaking...</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-box">🎤 Listening... Say something!</div>', unsafe_allow_html=True)

    # Display chat history
    for speaker, msg in st.session_state.conversation:
        st.markdown(f"**{speaker}:** {msg}")

    # Buttons
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("🎙️ Speak Now"):
            user_input = get_voice_input()
            if user_input:
                if "stop" in user_input.lower():
                    st.warning("🛑 Chat ended.")
                    st.session_state.chat_started = False
                else:
                    st.session_state.conversation.append(("You", user_input))
                    with st.spinner(f"{creature_choice} is thinking..."):
                        response = st.session_state.creature.respond(user_input)
                        st.session_state.conversation.append((creature_choice, response))

                        # AI speaks
                        st.session_state.is_speaking = True
                        st.rerun()  # Triggers below block in next run

    # Speak AI response if is_speaking = True
    if st.session_state.is_speaking and st.session_state.intro_spoken:
        last_response = st.session_state.conversation[-1][1]
        speak_text(last_response, st.session_state.voice)
        st.session_state.is_speaking = False
        st.rerun()

    with col2:
        if st.button("❌ End Chat"):
            st.warning("❌ Chat ended.")
            st.session_state.chat_started = False
