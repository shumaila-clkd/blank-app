import streamlit as st

st.set_page_config(page_title="Shumaila Tasleem - CLKD", page_icon="💖", layout="centered")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #fff5f7 0%, #ffe0ec 100%); }
h1 { color: #FF2E93; text-align: center; font-weight: 800; }
.subtitle { text-align: center; color: #6c757d; font-size: 18px; }
.card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 💖 Shumaila Tasleem")
st.markdown("<p class='subtitle'>CLKD Official Website | Professional Web Designer</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'><b>✨ Made with love at CLKD ✨</b></p>", unsafe_allow_html=True)

st.divider()

st.markdown("### 👩‍🎨 About Me")
st.write("Hello! I am **Shumaila Tasleem** from CLKD. I am passionate about creating beautiful, modern, and professional websites. This is my official profile website for CLKD.")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='card'>🎨<br><b>Creative Design</b><br>Modern UI</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>💻<br><b>Clean Coding</b><br>Professional</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'>🌸<br><b>Pretty Colors</b><br>Soft & Lovely</div>", unsafe_allow_html=True)

st.divider()

st.markdown("### 🌟 My Skills")
st.progress(90, text="Website Designing - 90%")
st.progress(85, text="Coloring & Styling - 85%")
st.progress(95, text="CLKD Projects - 95%")

st.divider()

st.markdown("### 📩 Contact Me")
name = st.text_input("Enter your name")
if name:
    st.balloons()
    st.success(f"Thank you {name}! Thanks for visiting my CLKD website 💖")

st.markdown("---")
st.markdown("<p style='text-align:center; color: #FF2E93;'>© 2026 Shumaila Tasleem | CLKD | All Rights Reserved 💖</p>", unsafe_allow_html=True)
