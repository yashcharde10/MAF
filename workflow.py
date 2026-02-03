import asyncio
from agents.agent import main_agent
from dotenv import load_dotenv
from brain import groq_ai_client
from agent_framework.exceptions import ServiceResponseException
import re 

async def work_flow(user_problem):
    try:
        load_dotenv()
        client = groq_ai_client()

        # Initialize the Main Agent
        master_agent = main_agent(client)

        print("Master Agent is starting...")

        response = await master_agent.run(user_problem)
    
        # DEBUG PRINT: Look at your terminal when you run the app
        print(f"DEBUG: RAW RESPONSE: {response}") 
    
        return "Below is the solution:", response.text
    
    
    except Exception as e:
        return f"Error: {str(e)}", ""

