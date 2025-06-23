import streamlit as st

st.set_page_config(page_title="Mood Chatbot", page_icon="💬")

st.title("🤖 Mood & Motivation Chatbot")
st.write("Tell me how you're feeling today, and I'll chat back like a friend 💖")

# --- Initialize chat history ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- Input from user ---
user_input = st.text_input("💬 Type your message:")

# --- On send ---
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something.")
    else:
        # Bot response logic
        msg = user_input.lower()
        if "sad" in msg:
            response = "😔 It's okay to feel sad. You're not alone. Take a deep breath 💖"
        elif "happy" in msg:
            response = "😊 That's wonderful! Stay joyful and spread the happiness!"
        elif "angry" in msg:
            response = "😤 Try counting to 10 and breathing. You’ve got this!"
        elif "tired" in msg:
            response = "😴 Rest is productive too. Take a break."
        else:
            response = "🤖 I'm here for you. Just talk to me anytime."

        # Save both messages
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

# --- Display chat history with bubbles ---
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(
            f"<div style='background:#e0f7fa;padding:10px;border-radius:10px;margin-bottom:5px;text-align:right;color:black'><b>🧍 {sender}:</b> {message}</div>",
            unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div style='background:#f1f8e9;padding:10px;border-radius:10px;margin-bottom:5px;color:black'><b>🤖 {sender}:</b> {message}</div>",
            unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with 💙 by Dafiq Elhaq")
