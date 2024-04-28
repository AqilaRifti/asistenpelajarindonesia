from app.api_router import api_router
from app.models import ai21_provider
from app.logger import primary_logger

primary_logger.name = __name__

@api_router.get("/ai21/{query}", tags=["ai21"])
async def ai21_response(query: str):
    try:
        return {
            "answer": ai21_provider.ai21(query)
        }
    finally:
        primary_logger.info(query)
