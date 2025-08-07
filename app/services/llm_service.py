from openai import OpenAI, APIConnectionError, APIError, RateLimitError, APIStatusError
from app.core.config import settings
from app.models.schema import RequestModel, ResponseModel
from fastapi import HTTPException
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self) -> None:
        self.model = settings.LLM_MODEL
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.LLM_API_KEY,
        )
        
    async def askQuestion(
        self, 
        input: RequestModel, 
        temperature: float = 0.2, 
        max_tokens: int = 500
    ) -> ResponseModel:
        messages = []
        
        try:
            try:
                with open('context.txt', 'r') as file:
                    context = file.read()
                    if context.strip():
                        try:
                            context_data = json.loads(context)
                            if isinstance(context_data, dict):
                                messages.append({"role": "system", "content": str(context_data)})
                            else:
                                messages.append({"role": "system", "content": context})
                        except json.JSONDecodeError:
                            messages.append({"role": "system", "content": context})
            except FileNotFoundError:
                logger.info("Context file not found, starting with empty context")
            except Exception as e:
                logger.error(f"Error reading context file: {str(e)}")

            messages.append({"role": "user", "content": input.message})

            try:
                completion = self.client.chat.completions.create(
                    extra_body={"response_format": {"type": "text"}},
                    model=settings.LLM_MODEL,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                answer = completion.choices[0].message.content
                
                try:
                    with open("context.txt", "a") as file:
                        conversation = {
                            "user_asked": input.message,
                            "bot_answered": answer
                        }
                        file.write(json.dumps(conversation) + "\n")
                except Exception as e:
                    logger.error(f"Failed to write to context file: {str(e)}")
                
                return ResponseModel(
                    message=answer, 
                    addi=completion.choices[0].finish_reason
                )

            except APIConnectionError as e:
                logger.error(f"Connection error with OpenRouter API: {str(e)}")
                raise HTTPException(
                    status_code=503,
                    detail="Service temporarily unavailable. Failed to connect to OpenRouter API."
                )
            except RateLimitError as e:
                logger.error(f"Rate limit exceeded: {str(e)}")
                raise HTTPException(
                    status_code=429,
                    detail="Rate limit exceeded. Please try again later."
                )
            except APIStatusError as e:
                logger.error(f"OpenRouter API status error: {str(e)}")
                raise HTTPException(
                    status_code=502,
                    detail=f"OpenRouter API error: {str(e)}"
                )
            except APIError as e:
                logger.error(f"OpenRouter API error: {str(e)}")
                raise HTTPException(
                    status_code=500,
                    detail=f"OpenRouter API error: {str(e)}"
                )
                
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Unexpected error in askQuestion: {str(e)}", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail="An unexpected error occurred while processing your request."
            )
    
llmservice = LLMService()