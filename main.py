import streamlit as st

st.set_page_config(page_title="Mood Chatbot", page icon"🧠")

st.title("🤖 Mood & Motivation Chatbot")
st.write("Tell me how you're feeling today, and I'll try to respond like a friend 👂")

#user input
user_input = st.text_input("What's on your mind")

#button
if st.button("send"):
  if user_input == "":
    st.warning("Please type something first.")
  else:
    #basic keword
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

st.markdown("---")
st.caption("Made with ❤️ by Dafiq Elhaq")
