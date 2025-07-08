from fastapi import APIRouter
import logging

router = APIRouter()
logger = logging.getLogger("fastapi_app")

@router.get("/", tags=["Health"])
def healthcheck():
    logger.debug("Healthcheck endpoint hit")
    return {"status": "ok", "message": "API is healthy!"}