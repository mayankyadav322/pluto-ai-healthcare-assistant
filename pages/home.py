import streamlit as st

st.set_page_config(page_title="Pluto Health", layout="wide")

# Hero Section
st.markdown("""
    <style>
    .hero { text-align: center; padding: 60px 0; }
    .btn { font-size: 20px !important; }
    </style>
    <div class="hero">
        <h1>Welcome to Pluto Health 🩺</h1>
        <h3>Your AI-Powered Clinical Diagnostic Assistant</h3>
        <p>Empowering your health journey with real-time, professional analysis.</p>
    </div>
""", unsafe_allow_html=True)

# Call to Action
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Start Your Consultation Now"):
        st.switch_page("app.py")

st.markdown("---")

# Founder Section
col_a, col_b = st.columns([1, 2])
with col_a:
    st.image("https://ui-avatars.com/api/?name=Mayank+Yadav&size=200", width=200)
with col_b:
    st.subheader("Message from the Founder")
    st.write("**Mayank Yadav**")
    st.write("I built Pluto Health to bridge the gap between initial symptom awareness and clinical action.")