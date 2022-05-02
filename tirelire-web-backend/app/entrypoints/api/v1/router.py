from fastapi import APIRouter

from app.entrypoints.api.v1.user.router import user_router


v1_router = APIRouter( prefix='/v1')
v1_router.include_router(user_router, prefix='/user')
