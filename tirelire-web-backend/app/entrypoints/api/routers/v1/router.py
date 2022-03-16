from fastapi import APIRouter

from app.entrypoints.api.routers.v1._router import _router


v1_router = APIRouter()

v1_router.include_router(_router, prefix='/v1')
