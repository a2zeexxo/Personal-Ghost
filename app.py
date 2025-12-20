
import streamlit as st
import google.generativeai as genai
import os

# Paksa konfigurasi API ke jalur stabil
os.environ["GOOGLE_API_USE_MTLS"] = "never"

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # PERUBAHAN KRUSIAL: Memanggil model tanpa embel-embel beta melalui jalur generik
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Gagal Konfigurasi: {e}")

st.set_page_config(page_title="GHOST FINAL", page_icon="💀")
st.title("💀 GHOST FINAL STAND")
st.caption("Jalur Stabil v1 Aktif")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Perintah terakhir, Juan?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Generate content
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Jika masih 404, server wilayah Anda sedang memblokir model Flash.")
