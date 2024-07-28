from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import pathlib


load_dotenv()

class ModelConfig(BaseSettings):

    MODEL_PATH : str

    class config :

        env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"

        
ModelConfig = ModelConfig()