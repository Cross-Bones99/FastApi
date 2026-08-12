from fastapi import FastAPI
from pydantic import BaseModel 

app=FastAPI()

class chatmessage(BaseModel):
    message: str
    query: str



@app.post("/chat")
def chat(message: chatmessage):
    return {
        "message": message.message,
        "response": message.query
    }