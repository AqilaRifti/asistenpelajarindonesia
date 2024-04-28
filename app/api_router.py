from fastapi import APIRouter
from app.on_startup import ON_STARTUP
from app.on_shutdown import ON_SHUTDOWN

api_router = APIRouter(prefix="/api/v2", on_startup=ON_STARTUP, on_shutdown=ON_SHUTDOWN)
