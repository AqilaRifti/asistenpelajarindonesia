from fastapi import FastAPI
from app.routes import ai21
from app.routes import users
from app.routes import camel_lm
from app.routes import wizard_lm
from app.routes import zephyr_lm
from app.routes import stable_lm

app = FastAPI()


# Basics AI Providers
app.include_router(camel_lm.api_router)
app.include_router(wizard_lm.api_router)
app.include_router(zephyr_lm.api_router)
app.include_router(stable_lm.api_router)
app.include_router(users.api_router)

# Masters AI Providers
app.include_router(ai21.api_router)


@app.get("/")
async def root():
    return {"status": "UP"}
