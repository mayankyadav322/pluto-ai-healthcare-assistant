import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from fpdf import FPDF

# 1. Configuration
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. UI/UX: Professional Design (CSS)
st.set_page_config(page_title="Pluto Health Doctor", page_icon="🩺", layout="wide")

# Navigation Button (Added)
st.sidebar.markdown("---")
if st.sidebar.button("🏠 Back to Home"):
    st.switch_page("pages/home.py")
st.sidebar.markdown("---")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stChatMessage { border-radius: 15px; padding: 10px; }
    .sidebar .stButton>button { width: 100%; border-radius: 5px; border: 1px solid #008080; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🩺 Pluto Health Doctor")
st.subheader("Professional AI Diagnostic Assistant")
st.markdown("---")

# 3. Sidebar
with st.sidebar:
    st.header("Patient Profile")
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    
    if st.button("Save Profile"):
        st.session_state.age = age
        st.session_state.gender = gender
        st.success("Profile saved!")

    st.divider()
    
    # Simple PDF Logic: Always show if history exists
    if "messages" in st.session_state and len(st.session_state.messages) > 0:
        if st.button("Prepare PDF Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(200, 10, txt="Pluto Health Doctor Summary", ln=True, align='C')
            pdf.set_font("Arial", size=12)
            
            for msg in st.session_state.messages:
                pdf.multi_cell(0, 10, txt=f"{msg['role'].upper()}: {msg['content']}")
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            
            st.download_button(
                label="Click here to download PDF",
                data=pdf_bytes,
                file_name="Pluto_Report.pdf",
                mime="application/pdf"
            )

# 4. Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Describe your symptoms..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        system_prompt = {"role": "system", "content": "You are a professional medical assistant. Always be cautious."}
        response = client.chat.completions.create(
            messages=[system_prompt] + st.session_state.messages,
            model="llama-3.3-70b-versatile",
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun()