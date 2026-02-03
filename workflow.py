import asyncio
from agents.agent import main_agent
from dotenv import load_dotenv
from brain import groq_ai_client
from agent_framework.exceptions import ServiceResponseException
import re 
from database import init_db, ChatHistory, Session_Local

# initializing the database as soon as app starts 
init_db()

async def work_flow(user_problem):
    db = Session_Local()
    try:
        load_dotenv()
        client = groq_ai_client()

        # Initialize the Main Agent
        master_agent = main_agent(client)

        print("Master Agent is starting...")

        response = await master_agent.run(user_problem)
        final_response = response.text

        # Save Chats
        new_chat = ChatHistory(
            user_query = user_problem,
            ai_response = final_response
        )
        db.add(new_chat)
        db.commit()

    
        # DEBUG PRINT: Look at your terminal when you run the app
        print(f"DEBUG: RAW RESPONSE: {response}") 
    
        return "Below is the solution:", response.text
    
    
    except Exception as e:
        return f"Error: {str(e)}", ""

