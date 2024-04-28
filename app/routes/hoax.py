from app.api_router import api_router
from app.models import fake_news_classifier_provider
from app.logger import primary_logger

primary_logger.name = __name__

@api_router.get("/hoax/{query}", tags=["wizard"])
async def wizard_response(query: str):
    answer = fake_news_classifier_provider.predict_news(query)
    try:
        return {
            "answer": answer
        }
    finally:
        primary_logger.info(query)
        primary_logger.info(answer)
