from fastapi import APIRouter, HTTPException
from app.models.schema import RequestModel, ResponseModel
from app.services.llm_service import llmservice

router = APIRouter()

@router.post("/")
async def chat_send(requestData: RequestModel)->ResponseModel:
    try:
        response = await llmservice.askQuestion(requestData)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, detail=f"error at route '/': {e}")
    return response

@router.get('/')
async def home():
    return "hey"