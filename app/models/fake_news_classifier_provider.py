import pickle
from app.constants import (
    NEWS_CLASSIFIER_PATH,
    FAKE_NEWS_CLASSIFIER_MODEL_PATH
)
from app.utils import filesystem

news_classifier = pickle.load(filesystem.FileOperation.read_file(NEWS_CLASSIFIER_PATH, mode="rb"))
fake_news_classifier = pickle.load(filesystem.FileOperation.read_file(FAKE_NEWS_CLASSIFIER_MODEL_PATH, mode="rb"))

def predict_news(message: str) -> str:
    if news_classifier.predict([message]) == [False]:
        return f"Menurut saya informasi HOAX\nTipe informasi {fake_news_classifier.predict(message)}"
    return "Menurut saya informasi BENAR."

