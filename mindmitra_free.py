import streamlit as st

st.set_page_config(page_title="MindMitra 💜", page_icon="💜")

st.title("MindMitra 💜")
st.write("Your Free AI Mental Health Buddy")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def get_reply(user_input):
    text = user_input.lower()

    if "sad" in text:
        return "I'm really sorry you're feeling this way 💜 I'm here for you."
    elif "happy" in text:
        return "That’s amazing 😊 Keep smiling!"
    elif "stress" in text:
        return "Take a deep breath 🌿 You’ll be okay."
    elif "lonely" in text:
        return "I'm here with you 💜 You're not alone."
    else:
        return "Tell me more 💜"

user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    reply = get_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

st.warning("This is not a replacement for professional help.")
