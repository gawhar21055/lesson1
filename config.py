# import os

# import dotenv

# dotenv.load_dotenv()

# API_TOKEN=os.getenv("TOKEN")
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
    )
    api_token: str
    admin_ids: set = {1276569860, 123}


settings = Settings()
