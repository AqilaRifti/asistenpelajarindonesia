from app.api_router import api_router
from app.database.user_database import (
    login,
    register,
    get_user,
    User
)

@api_router.get("/get_user/{username}", tags=["users"])
async def get_user(username: str):
    return get_user(username)


@api_router.get("/user/register/{name}/{email}/{password}", tags=["users"])
async def register_route(name, email, password):
    register(User(name, email, password))
    return login(name, password)


@api_router.get("/user/login/{username}/{password}", tags=["users"])
async def login_route(username: str, password: str):
    return login(username, password)