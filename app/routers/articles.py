from fastapi import APIRouter
from typing import List

from ..database import articles
from ..models import Article, ArticleServer
from ..utils import validate_article_id


router = APIRouter(tags=["Articles"])
responses = {404: {'description': 'Not found'}}


@router.get("/articles", response_model=List[ArticleServer])
def show_articles():
    return articles


@router.get("/article/{article_id}", response_model=ArticleServer, responses=responses)
def retrieve_article(article_id: int, uppercase: bool = False):
    validate_article_id(article_id, articles)
    my_article = articles[article_id]
    return ArticleServer(
        content=my_article.content.upper() if uppercase else my_article.content,
        comments=my_article.comments,
        id=article_id
    )


@router.post("/article", response_model=ArticleServer)
def post_article(article: Article):
    new_article = ArticleServer(id=len(articles), **dict(article))
    articles.append(new_article)
    return new_article


@router.delete("/last_article", response_model=ArticleServer)
def delete_last_article():
    return articles.pop()


@router.put("/article/{article_id}", response_model=ArticleServer, responses=responses)
def update_article(article: Article, article_id: int):
    validate_article_id(article_id, articles)
    articles[article_id] = ArticleServer(id=article_id, **dict(article))
    return articles[article_id]
