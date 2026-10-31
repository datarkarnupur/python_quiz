import streamlit as st

st.title("SIMPLE CHATBOT")

name=st.chat_input("Type your massege...")

if name:
    st.chat_message("user").write(name)

    if"hello"in name.lower():
      reply="hello!how are you?"
    elif"ai" in name.lower():
      reply="AI means Artifial Intelligence."
    elif"bye"in name.lower():
       reply="goodbye!"
    else:
       reply = "sorry, I don't understand."

    st.chat_message("bot").write(reply)            

