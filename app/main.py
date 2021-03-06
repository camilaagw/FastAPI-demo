from fastapi import FastAPI

from .routers import analytics, articles, greetings

app = FastAPI(
    title="Cool API",
    description="A cool *API* to test **FastAPI** 🚀`",
    version="0.1.0",
)

app.include_router(greetings.router)
app.include_router(articles.router)
app.include_router(analytics.router)
