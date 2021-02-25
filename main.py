from fastapi import FastAPI
from models import Article

app = FastAPI(
    title="Cool API",
    description="A cool *API* to test **FastAPI**. Made with ❤️ by `Unit8`",
    version="0.1.0"
)

my_article = {
    "content": "Apple buys U.K. startup for 1 billion"
}


@app.get("/")
def say_hello():
    """Say hello to the *fabulous* **Team!!!**.
    * Hallo!
    * Salut!
    * Hola!
    """
    return {"message": "Hello Team! This API seems to be working"}


@app.get("/article/{article_id}")
def retrieve_article(article_id: int, uppercase: bool = False):
    return {
        "content": my_article["content"].upper() if uppercase else my_article["content"],
        "id": article_id
    }


@app.post("/article")
def post_article(article: Article):
    return article
