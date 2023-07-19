from backend.routers import route_blog
from backend.routers import route_login
from backend.routers import route_user
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(route_user.router, prefix="/users", tags=["users"])
api_router.include_router(route_blog.router, prefix="/blogs", tags=["blog"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
