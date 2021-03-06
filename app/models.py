from pydantic import BaseModel, constr
from typing import Dict, List


class Article(BaseModel):
    content: constr(max_length=255)
    comments: List[str] = []


class ArticleServer(BaseModel):
    id: int
    content: constr(max_length=255)
    comments: List[str] = []


class ArticleSentiment(BaseModel):
    article_content: constr(max_length=255)
    sentiment: str


class ArticleEntities(BaseModel):
    article_content: constr(max_length=255)
    entities: Dict[str, str] = {
        'entity1': 'label',
        'entity2': 'label',
        'entity3': 'label',
    }
