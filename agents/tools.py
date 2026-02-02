from agent_framework import ChatAgent
from agents.prompts import (TECH_WRITER_INSTRUCTIONS, NON_TECH_WRITER_INSTRUCTIONS, 
                            QUALITY_CHECKER_INSTRUCTIONS, MAIN_AGENT_INSTRUCTIONS)

# 1. Technical Agent --> returning the technical issue
def tech_agent(client):
    return ChatAgent(
        chat_client = client,
        name = "tech_expert", 
        # Description is Metadata of the tool. 
        description="Solves complex technical issues, provides root causes, and technical resolution steps.",     
        instructions = TECH_WRITER_INSTRUCTIONS
    )

# 2. Non Technical Agent --> explaining error to customer 
def non_tech_agent(client):
    return ChatAgent(
        chat_client = client,
        name = "customer_editor",  
        description="Translates technical jargon into friendly, simple language for customers.",    
        instructions=NON_TECH_WRITER_INSTRUCTIONS
    )
  
# 3. Adding agent for Quality Checking
def quality_checker(client):
    return ChatAgent(
        chat_client=client,
        name = "Checker",
        description="Checks the quality of the customer editor's output on the scale of 1-10.",
        instructions=QUALITY_CHECKER_INSTRUCTIONS
    ) 