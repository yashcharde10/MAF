from brain import groq_ai_client
from agents.agent import ai_agent
import asyncio
import os
from dotenv import load_dotenv


async def run_demo():

    # load .env 
    load_dotenv()

    # Get brain
    client = groq_ai_client()

    # get agent 
    agent = ai_agent(client)

    response = await agent.run("what is an AI agent in 5 words?")
    print(f"Agent Response: {response.text}")

if __name__ == "__main__":
    asyncio.run(run_demo())

    