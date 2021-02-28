from fastapi import FastAPI
from models import Article, ArticleServer
from typing import List

app = FastAPI(
    title="Cool API",
    description="A cool *API* to test **FastAPI**. Made with ❤️ by `Unit8`",
    version="0.1.0"
)

articles = [Article(content="Apple buys U.K. startup for 1 billion")]


@app.get("/")
def say_hello():
    """Say hello to the *fabulous* **Team!!!**.
    * Hallo!
    * Salut!
    * Hola!
    """
    return {"message": "Hello Team! This API seems to be working"}


@app.get("/articles", response_model=List[Article])
def show_articles():
    return articles


@app.get("/article/{article_id}", response_model=ArticleServer)
def retrieve_article(article_id: int, uppercase: bool = False):
    my_article = articles[article_id]
    return ArticleServer(
        content=my_article.content.upper() if uppercase else my_article.content,
        comments=my_article.comments,
        id=article_id
    )


@app.post("/article", response_model=Article)
def post_article(article: Article):
    articles.append(article)
    return article


@app.delete("/last_article", response_model=Article)
def delete_last_article():
    return articles.pop()


@app.put("/article/{article_id}", response_model=Article)
def update_article(article: Article, article_id: int):
    articles[article_id] = article
    return articles[article_id]
