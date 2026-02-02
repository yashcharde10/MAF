import streamlit as st
from brain import groq_ai_client
from agents.agent import tech_agent, non_tech_agent
from dotenv import load_dotenv
import asyncio 
from workflow import work_flow


# Page configuration 
st.set_page_config(page_icon="spinner", page_title="AI Agent", layout="centered")
st.title("Assistant for Engineers")
st.write("Enter your technical problem here")

async def logic(user_input):
    draft, final= await work_flow(user_input)

    with st.status("Technical solution...", expanded=True):
        st.write(draft)

    with st.status("Non-technical editor...", expanded=True):
        st.write(final)

    return "Hope we solved your Problem!"


# INPUT LOGIC

user_problem = st.text_input("Describe your issue here : ", placeholder="e.g. Error 404 in page.")

if st.button("Generate Solution"):
    if user_problem:
        result = asyncio.run(logic(user_problem))

        # display the result 
        st.subheader(" ")
        st.success(result)

    else:
        st.warning("Please enter the problem first.")
