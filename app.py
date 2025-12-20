
import streamlit as st
import google.generativeai as genai

# Inisialisasi API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Menggunakan model paling dasar agar tidak kena Error 404
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gagal Konfigurasi: {e}")

st.title("💀 GHOST RECOVERY")
st.write("Mode Penyelamatan Aktif.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ketik pesan di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Sistem Google Error: {e}")
            st.info("Coba ganti model di kode jika 404 berlanjut.")
