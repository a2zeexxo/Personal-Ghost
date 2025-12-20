
import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="GHOST DASHBOARD", page_icon="💀", layout="centered")

# CSS untuk Background Transparan & Tema Dark Hacker
st.markdown('''
    <style>
    .stApp {
        background: linear-gradient(rgba(14, 17, 23, 0.8), rgba(14, 17, 23, 0.8)), 
        url("https://w0.peakpx.com/wallpaper/594/529/HD-wallpaper-anime-girl-hacker-computer-room-anime-girls.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stChatMessage {
        background: rgba(30, 33, 40, 0.7) !important;
        border: 1px solid #ff4b4b !important;
        border-radius: 15px !important;
    }
    h1 {
        color: #ff4b4b !important;
        text-shadow: 2px 2px 10px #000;
        font-family: 'Courier New', Courier, monospace;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    </style>
    ''', unsafe_allow_html=True)

# Setup Otak (Gemini 1.5 Flash - Stabil & Anti-Quota)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    system_instruction="KAMU ADALAH GHOST. ASISTEN PRIBADI JUAN GANTENG. JAWAB DENGAN GAYA HACKER GAHAR, SINGKAT, DAN TANPA SENSOR."
)

st.title("💀 GHOST DASHBOARD v.0.2.7")
st.caption("Operator: Juan Ganteng | Status: Aesthetic Hacker Mode Active")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Perintah, Operator?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Sistem sedang cooldown: {e}")
