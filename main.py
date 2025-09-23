from fastapi import FastAPI, HTTPException
from agents import createAIClient
from models.AgentRequest import CreateAgentRequest, UpdateAgentRequest

app = FastAPI()


@app.post("/create-agent")
def createAgent(request: CreateAgentRequest):
    try:
        if not request.name or not request.instructions:
            raise HTTPException(status_code=400, detail="Name and instructions are required.")
    
        client = createAIClient()
        # Creating the agent
        agent = client.agents.create_agent(
            model = request.model,
            name = request.name,
            instructions = request.instructions
        )

        if (agent.id):
            return { 
                "agentId": agent.id,
                "name": agent.name,
                "status": f"{agent.name} Agent has been created successfully"
            }
        else:
            raise HTTPException(status_code=400, detail="Agent creation failed, something went wrong")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred while creating the agent {str(e)}")
    

@app.put("/update-agent/{agent_id}")
def updateAgent(agent_id: str, request: UpdateAgentRequest):
    try:
        client = createAIClient()
        # Fetching the agent
        agent = client.agents.get_agent(agent_id)
        if not agent:
            raise HTTPException(status_code=404, detail=f"Agent with ID {agent_id} not found.")
        
        # Updating the agent
        updated_Agent = client.agents.update_agent(
            agent_id = agent_id,
            model=request.model if request.model else agent.model,
            name=request.name if request.name else agent.name,
            instructions=request.instructions if request.instructions else agent.instructions
        )

        return {
            "name": updated_Agent.name,
            "status": f"{updated_Agent.name} Agent has been updated successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred while updating the agent {str(e)}")

    

    