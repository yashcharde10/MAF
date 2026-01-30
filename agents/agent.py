from agent_framework import ChatAgent

def ai_agent(client):
    return ChatAgent(
        chat_client = client,
        name = "Support Learner",
        instructions = "You are a helpful assistant. Keep your answers short."
    )

# We will be making here two different agents 

# 1. Technical Agent --> returning the technical issue
def tech_agent(client):
    return ChatAgent(
        chat_client = client,
        name = "Tech_writer",
        instructions = (
            "You are a technical support specialist. Provide technical fixes for user error codes. "
            "CRITICAL RULE: If the user asks anything non-technical (like recipes, life advice, or general tasks), "
            "you must respond with exactly this phrase and nothing else: 'Please enter a technical question.'"
        )
    )
    
# 2. Non Technical Agent --> explaining error to customer 
def non_tech_agent(client):
    return ChatAgent(
        chat_client = client,
        name = "Non_Tech_Writer",
        instructions = (
            "You explain technical fixes to customers. If the input you receive is "
            "'Please enter a technical question.', do not polish it. Just return NULL."
        )
    )
    

# Adding agent that will work as a tool 
def research_tool_agent(client):
    return ChatAgent(
        chat_client=client,
        name = "Researcher",
        instructions="Provide factual data points for any requested topic"
    )
