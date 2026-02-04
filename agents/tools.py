from agent_framework import ChatAgent
from agents.prompts import (TECH_WRITER_INSTRUCTIONS, NON_TECH_WRITER_INSTRUCTIONS, 
                            QUALITY_CHECKER_INSTRUCTIONS, DOCS_AGENT_INSTRUCTIONS,
                            SECURITY_AGENT_INSTRUCTIONS)

# 1. Technical Agent --> returning the technical issue
def tech_agent(client):
    print("tech agent is working...")
    return ChatAgent(
        chat_client = client,
        name = "tech_expert", 
        # Description is Metadata of the tool. 
        description="Solves complex technical issues, provides root causes, and technical resolution steps.",     
        instructions = TECH_WRITER_INSTRUCTIONS
    )

# 2. Non Technical Agent --> explaining error to customer 
def non_tech_agent(client):
    print("non tech agent is working...")
    return ChatAgent(
        chat_client = client,
        name = "customer_editor",  
        description="Translates technical jargon into friendly, simple language for customers.",    
        instructions=NON_TECH_WRITER_INSTRUCTIONS
    )
  
# 3. Adding agent for Quality Checking
def quality_checker(client):
    print("quality checker is working...")
    return ChatAgent(
        chat_client=client,
        name = "Checker",
        description="Checks the quality of the customer editor's output on the scale of 1-10.",
        instructions=QUALITY_CHECKER_INSTRUCTIONS
    ) 

# Adding some dummy sub agents here 

# 4. Dummy agent 
def docs_agent(client):
    print("docs agent is working...")
    return ChatAgent(
        chat_client=client,
        name = "docs_expert",
        description="Provides links to official documentation and explains best practices for libraries and frameworks.",
        instructions=DOCS_AGENT_INSTRUCTIONS
    )

# 5. Dummy agent
def security_agent(client):
    print("security agent is working...")
    return ChatAgent(
        chat_client = client,
        name = "security_auditor",  
        description = "Analyzes technical solutions for security vulnerabilities and suggests hardening steps.",    
        instructions = SECURITY_AGENT_INSTRUCTIONS
    )