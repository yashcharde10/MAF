from agent_framework import ChatAgent
from agents.prompts import  MAIN_AGENT_INSTRUCTIONS
from agents.tools import tech_agent, non_tech_agent, quality_checker

# MAIN AGENT 
def main_agent(client):
    # Initializing the SUB AGENTS [TOOLS]
    tech_tool = tech_agent(client)
    non_tech_tool = non_tech_agent(client)
    checker = quality_checker(client)

    return ChatAgent(
        chat_client=client,
        name = "Main_Agent",
        instructions=MAIN_AGENT_INSTRUCTIONS,
        tools=[tech_tool, non_tech_tool, checker]
    )