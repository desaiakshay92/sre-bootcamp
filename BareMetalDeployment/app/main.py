from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1.router import router
from app.utils.logger import init_logger  # 👈 Add this import

app = FastAPI()

@app.on_event("startup")
def startup():
    init_logger()  # 👈 Initialize the logger
    Base.metadata.create_all(bind=engine)

app.include_router(router)