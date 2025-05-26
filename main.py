from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from context import context_manager
from llm import query_llm

app = FastAPI()

class MessageInput(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
async def chat(input: MessageInput):
    session_id = input.session_id
    user_msg = input.message

    context_manager.add_message(session_id, "user", user_msg)
    context = context_manager.get_context(session_id)

    try:
        response = await query_llm(context)
        context_manager.add_message(session_id, "assistant", response)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/reset")
def reset_session(session_id: str):
    context_manager.reset_context(session_id)
    return {"status": "context reset"}
