import streamlit as st
from brain import groq_ai_client
from agents.agent import tech_agent, non_tech_agent
from dotenv import load_dotenv
import asyncio 


# Page configuration 
st.set_page_config(page_icon="spinner", page_title="AI Agent", layout="centered")
st.title("Assistant for Engineers")
st.write("Enter your technical problem here")

async def logic(user_input):
    load_dotenv()
    client = groq_ai_client()

    writer = tech_agent(client)
    editor = non_tech_agent(client)

    with st.status("Here is Technical solution...", expanded=True):
        draft_response = await writer.run(user_input)
        draft_text = draft_response.text
        st.write(f"Solution: \n {draft_text}")

    # this is final work
    with st.status("Non technical editor is writing the draft...", expanded=True):
        final_prompt = f"Polish the technical draft: {draft_text}"
        final_response = await editor.run(final_prompt)
        final_response_text = final_response.text
        st.write(f"Solution: {final_response_text}")

    return "We hope that your problem is resolved!"

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
