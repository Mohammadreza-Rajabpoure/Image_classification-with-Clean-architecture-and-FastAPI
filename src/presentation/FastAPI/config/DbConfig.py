from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import pathlib

load_dotenv()

class classifiyConfig(BaseSettings):

    LOCAL_HOSTE : str

    DATABASE_NAME : str
    
    COLLECTION_NAME : str

    
    class config :
        
        env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"
        

classifiyConfig = classifiyConfig()