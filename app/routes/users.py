from app.api_router import api_router
from app.logger import primary_logger
from app.database.user_database import (
    User,
    login,
    register,
    get_user as get_user_from_db
)

primary_logger.name = __name__

@api_router.get("/get_user/{username}", tags=["users"])
async def get_user(username: str):
    try:
        return get_user_from_db(username)
    finally:
        primary_logger.info(f"Get user {username}")


@api_router.get("/user/register/{name}/{email}/{password}", tags=["users"])
async def register_route(name, email, password):
    try:
        register(User(name, email, password))
        return login(name, password)
    finally:
        primary_logger.info(f"Registered: {name} with email {email}")


@api_router.get("/user/login/{username}/{password}", tags=["users"])
async def login_route(username: str, password: str):
    try:
        return login(username, password)
    finally:
        primary_logger.info(f"User: {username} has logged in")
