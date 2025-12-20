
import streamlit as st
import google.generativeai as genai

# Setup API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Gunakan model yang paling standar di API Google saat ini
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="KAMU ADALAH GHOST. ASISTEN JUAN GANTENG. JAWAB SINGKAT DAN JELAS."
)

st.title("💀 GHOST SIMPLE")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Apa perintahmu, Juan?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Generate tanpa safety settings dulu agar tidak konflik
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
