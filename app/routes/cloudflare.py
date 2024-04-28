from fastapi import APIRouter
from app.models import cloudflare_provider

router = APIRouter()

@router.get("/cloudflare/{query}", tags=["cloudflare"])
async def cloudflare_response(query: str):
    return {
        "answer": cloudflare_provider.cloudflare(query)
    }

