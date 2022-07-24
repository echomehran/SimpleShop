from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "payment"
    redis_host: str 
    redis_port: str
    redis_password: str

    class Config:
        env_file = ".env"
