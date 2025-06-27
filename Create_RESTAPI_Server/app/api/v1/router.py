from fastapi import APIRouter
from app.api.v1.endpoints import users_endpoint, healthcheck_endpoint

router = APIRouter()
router.include_router(users_endpoint.router, prefix="/api/v1/users", tags=["Users"])
router.include_router(healthcheck_endpoint.router, prefix="/healthcheck", tags=["Health"])
