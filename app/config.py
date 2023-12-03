from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    database_hostname: str = <hostname>
    database_password: str= 
    database_port: 
    database_username: str= 
    database_name: str= 
    secret_key: str= 
    algorithm: str= 
    access_token_expire_minutes: int= 
