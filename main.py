import uuid
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from models.api_models import APIRequest, APIResponse, ChatMessage
from services import redis_client
from chatbot import logic, prompt

app = FastAPI(
    title="Kopi Challenge API",
    description="API para un chatbot de debates.",
    version="1.0.0"
)


@app.post("/chat", response_model=APIResponse)
async def chat_endpoint(request: APIRequest):
    conversation_id = request.conversation_id
    history = []
    is_new_conversation = not conversation_id

    if is_new_conversation:
        conversation_id = str(uuid.uuid4())
        
        system_prompt = prompt.create_system_prompt(initial_statement=request.message)
        
        history.append({"role": "user", "message": system_prompt})

    else:
        history = redis_client.get_conversation_history(conversation_id)
        if not history:
            raise HTTPException(status_code=404, detail="ID de conversación no encontrado.")

    history.append({"role": "user", "message": request.message})

    bot_message_text = logic.generate_bot_response(history, request.message)

    history.append({"role": "bot", "message": bot_message_text})

    redis_client.save_conversation_history(conversation_id, history)

    response_messages = [
        ChatMessage(role=msg["role"], message=msg["message"]) 
        for msg in history 
        if not msg["message"].startswith("Eres un chatbot de debate llamado 'Kopi'")
    ]

    return APIResponse(conversation_id=conversation_id, message=response_messages[-5:])


@app.get("/", include_in_schema=False)
async def root():
    return JSONResponse(content={"message": "Kopi Challenge API está funcionando. Usa el endpoint POST /chat para interactuar."})