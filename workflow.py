import asyncio
from agents.agent import tech_agent, non_tech_agent
from dotenv import load_dotenv
from brain import groq_ai_client


async def work_flow(user_problem):

    load_dotenv()
    client = groq_ai_client()

    # Loading the agents
    writer = tech_agent(client)
    editor = non_tech_agent(client)

    

    # 1. Technical writer will work here
    print("Tech writer is working ...")
    draft_response = await writer.run(user_problem)
    draft_text = draft_response.text
    print(f"Technical draft: {draft_text}\n")

    # 2. Non technical --> editor will work here 
    print("Non Technical --> editor is working here")
    final_response = f"please polish this technical draft : {draft_text}"
    non_tech_draft = await editor.run(final_response)
    non_tech_draft_text = non_tech_draft.text
    print(f"The user friendly reponse is here : {non_tech_draft_text}")

if __name__ == "__main__":
    asyncio.run(work_flow())