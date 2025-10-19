# stripe key
# datenbank

# zentrale stelle dafuer
# alles ueber .env datei

from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    STRIPE_API_KEY: str = os.getenv("STRIPE_API_KEY")

    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")

settings = Settings()