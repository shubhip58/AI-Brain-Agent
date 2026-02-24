from fastapi import FastAPI
from models import AgentRequest, AgentResponse
from router import agent_router
from tools import tool_calculate, tool_save_memory, tool_get_memory
from database import init_db

app = FastAPI(title="AI Agent Brain")

init_db()

@app.post("/agent/query", response_model=AgentResponse)
def agent_query(req: AgentRequest):
    tool, input1, input2 = agent_router(req.prompt)

    if tool == "calculator":
        result = tool_calculate(input1)
        return {
            "original_prompt": req.prompt,
            "chosen_tool": "calculator",
            "tool_input": input1,
            "response": result
        }

    elif tool == "memory_save":
        result = tool_save_memory(input1, input2)
        return {
            "original_prompt": req.prompt,
            "chosen_tool": "memory_write",
            "tool_input": f"{input1} = {input2}",
            "response": result
        }

    elif tool == "memory_read":
        result = tool_get_memory(input1)
        return {
            "original_prompt": req.prompt,
            "chosen_tool": "memory_read",
            "tool_input": input1,
            "response": result
        }

    return {
        "original_prompt": req.prompt,
        "chosen_tool": "none",
        "tool_input": "",
        "response": {"error": "I do not have a tool for that."}
    }