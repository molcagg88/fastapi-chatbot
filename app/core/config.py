from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    API_PREFIX: str
    
    LLM_API_KEY: str
    LLM_MODEL: str
    LLM_PROVIDER: str

    class Config:
        env_file = ".env"

settings = Settings()