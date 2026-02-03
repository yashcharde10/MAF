import streamlit as st
from brain import groq_ai_client
from agents.tools import tech_agent, non_tech_agent, quality_checker
from dotenv import load_dotenv
import asyncio 
from workflow import work_flow
from database import Session_Local, ChatHistory, init_db


# Page configuration 
st.set_page_config(page_icon="🤖", page_title="AI Agent", layout="centered")
st.title("Assistant for Engineers")
st.write("Enter your technical problem here")

# Initializing the session state --> this helps to keep the chats on screen when session starts
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Loading some (last 4 or 5) chats to screen on startup
    db = Session_Local()
    past_chats = db.query(ChatHistory).order_by(ChatHistory.timestamp.asc()).limit(5).all()
    for chat in past_chats:
        st.session_state.messages.append({"role": "user", "content": chat.user_query})
        st.session_state.messages.append({"role": "assistant", "content": chat.ai_response})
    db.close()

# 3. Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Input Logic
if prompt := st.chat_input("Describe your technical issue..."):
    
    # Display user message immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        # We use a status box inside the chat to show the agent thinking
        with st.status("Solving your problem...", expanded=False) as status:
            st.write("Orchestrating agents...")
            # Run your workflow
            _, final_response = asyncio.run(work_flow(prompt))
            status.update(label="Solution Generated!", state="complete", expanded=False)
        
        # Display the final answer
        st.markdown(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})

# 5. Sidebar for Database History (Simple View)
with st.sidebar:
    st.title("📜 Database Logs")
    if st.button("Clear Screen"):
        st.session_state.messages = []
        st.rerun()
    
    st.info("Your responses are being saved.")

