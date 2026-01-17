import streamlit as st
from truthcore import calculate_confidence

password = st.text_input("Beta Password:", type="password")
if password != "truthsetsfree":
    st.stop()

api_key = st.secrets["API_KEY"]

st.title("TruthCore Beta - Probabilistic Truth Verifier")

st.write("""
Welcome to the TruthCore beta! Enter a claim below, along with its source and any supporting evidences or historical reliability data. We'll compute a confidence score based on probabilistic analysis.
Note: This is an early prototype—scores use real fact-checks.
""")

# User inputs
claim = st.text_area("Enter the claim or statement:")
source = st.selectbox("Source credibility:", ["Reputable", "Neutral", "Unreliable"])
evidences = st.text_area("Supporting evidences (one per line):").split("\n") if st.text_area else []
source_history = st.text_input("Historical reliability scores (comma-separated, e.g., 0.8,0.9):").split(",") if st.text_input else []

if st.button("Verify Confidence"):
    if claim:
        score = calculate_confidence(claim, source, evidences, source_history, api_key=api_key)
        st.success(f"Confidence Score: {score}%")
        st.write("Breakdown (simulated except consistency, which uses real API):")
        st.write("- Source Lineage: Based on selected credibility.")
        st.write("- Evidence Consistency: From Google Fact Check API or fallback.")
        st.write("- Historical Reliability: Average of provided scores.")
        st.write("- Manipulation Signals: Checked for sensationalism.")
    else:
        st.error("Please enter a claim.")

# Feedback section for beta users
st.subheader("Beta Feedback")
feedback = st.text_area("What do you think? Suggestions?")
if st.button("Submit Feedback"):
    # In production, save to a file/DB or email it
    st.success("Thanks for your feedback! (Simulated submission)")

# Sidebar for beta info
st.sidebar.title("Beta Signup")
st.sidebar.write("Already signed up? Great! If not, join the waitlist.")
st.sidebar.markdown('[Sign Up Here](https://forms.gle/Y5RL7GXd9zcQ2cmi9)')
