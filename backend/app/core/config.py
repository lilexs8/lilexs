from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LN1"
    environment: str = "development"
    database_url: str = "sqlite:///./ln1_dev.db"
    jwt_secret: str = "change_this_secret"
    claude_api_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
