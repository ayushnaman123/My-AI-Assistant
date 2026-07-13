import streamlit as st
from automation import handle_automation
from nlp_analyzer import analyze_text_sentiment
from utils import generate_secure_token

# Application Dashboard Architecture
st.set_page_config(page_title="Ayush Naman | Project Hub", page_icon="⚡", layout="wide")

# Custom UI Injector
st.markdown("""
    <style>
    .main-heading { font-size: 40px; font-weight: 800; color: #1E88E5; font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar UI Initialization
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6840/6840478.png", width=90)
    st.markdown("### **Developer Profile**")
    st.markdown("## **Ayush Naman**")
    st.caption("MCA Graduate | Software & Data Analytics Enthusiast")
    st.markdown("---")
    st.info("Architecture: Modular Model (Multi-file)")

# Primary View Canvas
st.markdown("<p class='main-heading'>⚡ Next-Gen Interactive Dashboard</p>", unsafe_allow_html=True)
st.write("Welcome to my core Python project. Built using clean, modular architectural practices.")

# Navigation Controller Tabs
task_bot, sentiment_analyst, trivia_hub, dev_tools = st.tabs([
    "🤖 Core Automation Bot", "🧠 Text Sentiment Analyzer", "🎮 Technical Trivia", "🔐 Security Utility"
])

# ------------------------------------------
# TAB 1: OPERATIONAL BOT PIPELINE
# ------------------------------------------
with task_bot:
    st.subheader("System Automation & Information Parsing")
    user_command = st.text_input("Enter action prompt:", key="action_prompt")
    
    if st.button("Trigger Pipeline", type="primary"):
        if not user_command.strip():
            st.error("Input syntax invalid: Prompt field required.")
        else:
            # Invoking background architecture with a localized frontend spinner
            with st.spinner("Processing command request..."):
                response = handle_automation(user_command)
                
            if response["status"] == "success":
                if response["type"] == "wiki":
                    st.success("📚 Result from Wikipedia:")
                    st.info(response["data"])
                elif response["type"] == "play":
                    st.success(f"🎵 Automation Process Initiated for '{response['target']}'")
                    st.markdown(f"[👉 Click Here to Watch on YouTube]({response['data']})")
                elif response["type"] == "time":
                    st.metric(label="System Response Time", value=response["data"])
            elif response["status"] == "warning":
                st.warning(response["message"])
            else:
                st.error(response["message"])

# ------------------------------------------
# TAB 2: SENTIMENT INTELLIGENCE MATRIX
# ------------------------------------------
with sentiment_analyst:
    st.subheader("🎭 Text Classification & Sentiment Mapping")
    raw_text = st.text_area("Provide feedback text to evaluate:")
    
    if st.button("Analyze Dataset"):
        if not raw_text.strip():
            st.error("Lexical validation failed: Text block field empty.")
        else:
            analysis = analyze_text_sentiment(raw_text)
            if analysis["result"] == "positive":
                st.balloons()
                st.success(f"🤖 Positive Metrics Found 😊 (Score: {analysis['score']})")
            elif analysis["result"] == "negative":
                st.error(f"🤖 Negative Metrics Detected 😡 (Score: {analysis['score']})")
            else:
                st.warning("🤖 Indeterminate / Neutral Sentiment 😐")

# ------------------------------------------
# TAB 3: ENTERPRISE ARCHITECTURE QUIZ
# ------------------------------------------
with trivia_hub:
    st.subheader("🎮 Core Architecture Trivia")
    choice = st.radio("Which tool manages dependencies in Python?", ["A) npm", "B) pip", "C) Maven", "D) Git"])
    if st.button("Verify Submission"):
        if "B)" in choice:
            st.success("🎉 Correct Validation! `pip` handles packages.")
        else:
            st.error("❌ Evaluation Failed.")

# ------------------------------------------
# TAB 4: DEPLOYMENT UTILITY UTILS
# ------------------------------------------
with dev_tools:
    st.subheader("🔐 Cryptographic String Engine")
    token_length = st.slider("Define String Length:", min_value=8, max_value=24, value=14)
    if st.button("Generate Secure Token"):
        token = generate_secure_token(token_length)
        st.code(token, language="text")
