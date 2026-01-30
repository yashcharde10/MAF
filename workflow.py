import asyncio
from agents.agent import tech_agent, non_tech_agent, research_tool_agent
from dotenv import load_dotenv
from brain import groq_ai_client


async def work_flow(user_problem):

    load_dotenv()
    client = groq_ai_client()

    # initiaizing the tool agent 
    researcher = research_tool_agent(client)

    # Loading the agents
    writer = tech_agent(client)
    editor = non_tech_agent(client)

    

    # 1. Technical writer will work here
    
    draft_response = await writer.run(f"use the researcher tool while answering the problem : {user_problem}")
    draft_text = draft_response.text

    print(f"Technical draft: {draft_text}\n")
    tool = [researcher]



    # 2. Non technical --> editor will work here 
    
    final_prompt = f"please polish this technical draft : {draft_text}"
    non_tech_draft = await editor.run(final_prompt)
    non_tech_draft_text = non_tech_draft.text
    print(f"The user friendly reponse is here : {non_tech_draft_text}")


    
    return draft_text, non_tech_draft_text
