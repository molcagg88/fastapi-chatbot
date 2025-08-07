from pydantic import BaseModel

class RequestModel(BaseModel):
    message: str

class ResponseModel(BaseModel):
    message: str
    addi: str