from agent_framework import ChatAgent
from agents.prompts import (TECH_WRITER_INSTRUCTIONS, NON_TECH_WRITER_INSTRUCTIONS, 
                            RESEARCHER_INSTRUCTIONS,QUALITY_CHECKER_INSTRUCTIONS)

# 1. Technical Agent --> returning the technical issue
def tech_agent(client, tools=None):
    return ChatAgent(
        chat_client = client,
        name = "Tech_writer",
        
        instructions = TECH_WRITER_INSTRUCTIONS,
        tools=tools
    )

# 2. Non Technical Agent --> explaining error to customer 
def non_tech_agent(client):
    return ChatAgent(
        chat_client = client,
        name = "Non_Tech_Writer",
        
        instructions=NON_TECH_WRITER_INSTRUCTIONS
    )

# 3. Adding agent that will work as a tool 
def research_tool_agent(client):
    return ChatAgent(
        chat_client=client,
        name = "Researcher",
        instructions=RESEARCHER_INSTRUCTIONS
    )
  
# 4. Adding agent for Quality Checking
def quality_checker(client):
    return ChatAgent(
        chat_client=client,
        name = "Checker",
        instructions=QUALITY_CHECKER_INSTRUCTIONS
    ) 