from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DB_USER: str = Field(..., alias="DB_USER")
    DB_PASSWORD: str = Field(..., alias="DB_PASSWORD")
    DB_HOST: str = Field(..., alias="DB_HOST")
    DB_PORT: str = Field(default="5432", alias="DB_PORT")
    DB_NAME: str = Field(..., alias="DB_NAME")

    PROJECT_NAME: str = "FastAPI App"
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    @property
    def DB_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"  # Optional if you're using k8s env vars

settings = Settings()
