#API KEYS and other settings for payment gateway
import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

from dotenv import load_dotenv
load_dotenv()  # lade .env datei im projekt root

class Settings(BaseSettings):

    APP_ENV: str = "development"  # or "production"
    WORDPRESS_DB_HOST: str = os.getenv('WORDPRESS_DB_HOST')
    WORDPRESS_DB_USER: str = os.getenv('WORDPRESS_DB_USER')
    WORDPRESS_DB_PASSWORD: str = os.getenv('WORDPRESS_DB_PASSWORD')
    SYS_DB_NAME: str = os.getenv('SYS_DB_NAME')

    @property
    def database_url(self) -> str:
        return f"mysql+aiomysql://{self.WORDPRESS_DB_USER}:{self.WORDPRESS_DB_PASSWORD}@{self.WORDPRESS_DB_HOST}/{self.SYS_DB_NAME}"

settings = Settings()