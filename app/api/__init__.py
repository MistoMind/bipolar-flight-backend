from fastapi import APIRouter

from .endpoints.admin import admin_router
from .endpoints.auth import auth_router
from .endpoints.user import user_router
from .endpoints.flight import flight_router

api_router = APIRouter()

api_router.include_router(router=admin_router)
api_router.include_router(router=auth_router)
api_router.include_router(router=user_router)
api_router.include_router(router=flight_router)
