from fastapi import APIRouter

router = APIRouter(tags=['Greetings'])


@router.get("/")
def say_hello():
    """Say hello to the *fabulous* **Team!!!**.
    * Hallo!
    * Salut!
    * Hola!
    """
    return {"message": "Hello Team! This API seems to be working"}
