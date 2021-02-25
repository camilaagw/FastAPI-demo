from fastapi import FastAPI

app = FastAPI(
    title="Cool API",
    description="A cool *API* to test **FastAPI** 🚀",
    version="0.1.0"
)


@app.get("/")
def say_hello():
    """Say hello to the *fabulous* **Team!!!**.
    * Hallo!
    * Salut!
    * Hola!
    """
    return {"message": "Hello Team! This API seems to be working"}

