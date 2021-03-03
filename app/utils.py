from fastapi import HTTPException
from app.models import Article
from typing import List


def validate_article_id(article_id: int, articles:List[Article]):
    if article_id > len(articles) - 1:
        raise HTTPException(status_code=404, detail='Article not found')
