import streamlit as st

st.set_page_config(page_title="Mood Chatbot", page_icon="🧠")

st.title("🤖 Mood & Motivation Chatbot")
st.write("Tell me how you're feeling today, and I'll try to respond like a friend 👂")

#user input
user_input = st.text_input("What's on your mind")

# Button to get response
if st.button("Send"):
    if user_input == "":
        st.warning("Please type something first.")
    else:
        # Basic keyword detection
        if "sad" in user_input.lower():
            st.write("😔 It's okay to feel sad. You're not alone. Take some rest 💖")
        elif "happy" in user_input.lower():
            st.write("😊 That's awesome! Keep shining and share your joy with others!")
        elif "angry" in user_input.lower():
            st.write("😤 Deep breaths, my friend. You got this.")
        elif "tired" in user_input.lower():
            st.write("😴 Sounds like you need a break. Rest is productive too!")
        else:
            st.write("🤖 I'm not sure how to respond, but I'm here for you!")

        #save bot messege
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

# --- Display chat history with bubbles ---
for sender, messege in st.session_state.chat
    if sender == "You":
        st.markdown(f"<div style='background:#e0f7fa;padding:10px;border-radius:10;margin-bottom:5px;text-align:right'><b>🧍 {sender}:</b> {message}</div>",
                    unsafe_allow_html=true)
    else:
        st.markdown(
            f""<div style='background:#f1f8e9;padding:10px;border-radius:10px;margin-bottom:5px'><b>🤖 {sender}:</b> {message}</div>",
            unsafe_allow_html=True)

st.markdown(f"<div style='background:#f1f1f1;padding:10px;border-radius:10px;margin-bottom:10px;'>👤 {user_input}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='background:#dcf8c6;padding:10px;border-radius:10px;margin-bottom:10px;'>🤖 {response}</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ by Dafiq Elhaq")
