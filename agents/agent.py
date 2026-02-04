from agent_framework import ChatAgent
from agents.prompts import  MAIN_AGENT_INSTRUCTIONS
from agents.tools import (tech_agent, non_tech_agent, quality_checker,
                          docs_agent, security_agent)

# MAIN AGENT 
def main_agent(client):
    # Initializing the SUB AGENTS [TOOLS]
    tech_tool = tech_agent(client)
    non_tech_tool = non_tech_agent(client)
    checker = quality_checker(client)
    docs_tool = docs_agent(client)
    security_tool = security_agent(client)

    return ChatAgent(
        chat_client=client,
        name = "Main_Agent",
        instructions=MAIN_AGENT_INSTRUCTIONS,
        tools=[tech_tool, non_tech_tool, checker, docs_tool, security_tool]
    )