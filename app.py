import streamlit as st

from consts import FIRST_ASSISTANT_MESSAGE
from llm import get_answer, extract_user_info

def app():
    st.title("HackerEarth")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.chat_message("assistant").markdown(FIRST_ASSISTANT_MESSAGE)

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("How can I help?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)

        if len(st.session_state.messages) > 4:
            extract_user_info(user_message=prompt, conversation_history=st.session_state.messages)

        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = get_answer(prompt, st.session_state.messages)
            st.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == '__main__':

    app()
