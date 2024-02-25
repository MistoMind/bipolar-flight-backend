from fastapi import APIRouter

from .endpoints.user import user_router

api_router = APIRouter()

api_router.include_router(router=user_router)
