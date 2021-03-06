import httpx
import spacy
from fastapi import APIRouter

from ..database import articles
from ..models import ArticleEntities, ArticleSentiment
from ..utils import validate_article_id

router = APIRouter(
    prefix='/analytics',
    tags=["Analytics"]
)
responses = {404: {'description': 'Not found'}}


@router.get("/entity-recognition/{article_id}", response_model=ArticleEntities, responses=responses)
def get_article_entities(article_id: int):
    validate_article_id(article_id, articles)
    article = articles[article_id]
    ml_english_model = spacy.load("en_core_web_sm")
    doc = ml_english_model(article.content)
    return {'article_content': article.content, 'entities': {ent.text: ent.label_ for ent in doc.ents}}


@router.get("/sentiment-analysis/{article_id}", response_model=ArticleSentiment, responses=responses)
async def analyse_article_sentiment(article_id: int):
    validate_article_id(article_id, articles)
    article = articles[article_id]
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            'https://api.deepai.org/api/sentiment-analysis',
            headers={"api-key": "3a086f57-3e2c-4874-ae9c-c215463fb3f2"},
            data={"text": article.content}
        )
        resp.raise_for_status()
        data = resp.json()
    return {'article_content': article.content, 'sentiment': data['output'][0]}
