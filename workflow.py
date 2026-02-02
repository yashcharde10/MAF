import asyncio
from agents.agent import main_agent
from agents.tools import tech_agent, non_tech_agent, quality_checker, research_tool_agent
from dotenv import load_dotenv
from brain import groq_ai_client
from agent_framework.exceptions import ServiceResponseException
import re 

async def work_flow(user_problem):
    try:
        load_dotenv()
        client = groq_ai_client()

        # Initialize the Main Agent
        master_agent = main_agent

        print("Master Agent is starting...")

        response = await master_agent.run(user_problem)

        return "Below is the solution :  ", response.text  
    
    except Exception as e:
        return f"Error: {str(e)}", ""

"""
async def work_flow(user_problem):
    try:
        load_dotenv(override=True)
        client = groq_ai_client()

        # initiaizing the tool agent 
        researcher = research_tool_agent(client)

        # Loading the agents
        writer = tech_agent(client, tools=[researcher])
        editor = non_tech_agent(client)
        checker = quality_checker(client)

        print("🤖 System: Agents initialized. Starting process...")
    
    except ServiceResponseException:
        
        return "Check connectivity", ""
    except Exception as e:
        
        return f"An unexpected error occurred: {str(e)}", ""


    

    # 1. Technical writer will work here  
    print("🔍 Step 1: Technical Writer is analyzing and researching...")
    draft_response = await writer.run(f"use the researcher tool while answering the problem : {user_problem}")
    draft_text = draft_response.text

    print("✅ Technical draft completed.")
    tool = [researcher]


    # 2. Non technical --> editor will work here 
    print("✍️  Step 2: Editor is simplifying for user-friendly language...")   
    final_prompt = f"please polish this technical draft : {draft_text}"
    non_tech_draft = await editor.run(final_prompt)
    non_tech_draft_text = non_tech_draft.text
    print("✅ User-friendly version created.")
 
    

    # 3. Quality Checker:
    check_draft = await checker.run(f"Audit this content : {non_tech_draft_text}")
    score_match = re.search(r'(\d+)/10', check_draft.text)
    score = int(score_match.group(1)) if score_match else 0
    print(f"✅ score is here : {score}")
    
    if score >= 7:
        print(f"The user friendly reponse is here : {non_tech_draft_text}")
    else:
        print(f"⚠️ Low Quality ({score}/10). Re-polishing...")
        
        # We send it BACK to the writer with the checker's critique
        correction_prompt = f"Your previous draft got a low score. Critique: {check_draft.text}. Please rewrite it to be more empathetic and simple."
        final_response = await editor.run(correction_prompt)
        
    #thread 
        
        return draft_text, final_response.text

    return draft_text, non_tech_draft_text

"""