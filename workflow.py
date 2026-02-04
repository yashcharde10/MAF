import asyncio
from agents.agent import main_agent
from dotenv import load_dotenv
from brain import groq_ai_client
from agent_framework.exceptions import ServiceResponseException
import re 
from database import init_db, ChatHistory, Session_Local
from agent_framework import AgentThread

# initializing the database as soon as app starts 
init_db()

async def work_flow(user_problem, thread=None):
    db = Session_Local()
    try:
        load_dotenv()
        client = groq_ai_client()
        

        # Initialize the Main Agent
        master_agent = main_agent(client)
        print("Master Agent is starting...")

        # 1. Handle Thread Initialization
        if thread is None:
            # Create a new thread if one doesn't exist
            thread = master_agent.get_new_thread()

        # 2. Pass the thread to the run method
        # This allows the Main Agent and its sub-agents to access history
        response = await master_agent.run(user_problem, thread=thread)
        
        final_response = response.text
        print("✔️ Agent succesfully responded.")

        

        # Save Chats
        new_chat = ChatHistory(
            user_query = user_problem,
            ai_response = final_response
        )
        db.add(new_chat)
        db.commit()

    
        print("✔️ Agent worked !!.")
    
        return final_response, thread
    
    
    except Exception as e:
        return f"Error: {str(e)}", ""