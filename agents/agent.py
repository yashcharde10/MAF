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
        instructions = "Provide the technical fix for the user's error code."
    )
    
# 2. Non Technical Agent --> explaining error to customer 
def non_tech_agent(client):
    return ChatAgent(
        chat_client = client,
        name = "Non_Tech_Writer",
        instructions="Write the technical fix non-technically, user friendly for customers.."
    )

