from functools import lru_cache
from pydantic import BaseSettings, Field



class Settings(BaseSettings):
    SERVER_HOST: str = '0.0.0.0'
    PORT: int = 3000
    STOP_TIMEOUT = 120
    SLEEP_DURATION = 1e-4  # 0.1 ms sleep
    APP_NAME: str = "ARABIC SENTIMENTS"


@lru_cache()
def get_settings():
    return Settings()


# Instantiate the settings
settings = get_settings()