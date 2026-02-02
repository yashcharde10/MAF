from agent_framework import ChatAgent
from agents.prompts import (TECH_WRITER_INSTRUCTIONS, NON_TECH_WRITER_INSTRUCTIONS,
                             QUALITY_CHECKER_INSTRUCTIONS, RESEARCHER_INSTRUCTIONS)
from agents.tools import tech_agent, non_tech_agent, quality_checker, research_tool_agent

# MAIN AGENT 

def main_agent(client):
    # Initializing the SUB AGENTS
    tech_tool = tech_agent(client)
    non_tech_tool = non_tech_agent(client)
    checker = quality_checker(client)
    researcher = research_tool_agent(client)

    return ChatAgent(
        chat_client=client,
        name = "Main_Agent",
        instructions="Pending",
        tools=[tech_tool, non_tech_tool, checker, researcher]
    )