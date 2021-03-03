from fastapi import APIRouter

router = APIRouter()


@router.get("/",  tags=['Greetings'])
def say_hello():
    """Say hello to the *fabulous* **Team!!!**.
    * Hallo!
    * Salut!
    * Hola!
    """
    return {"message": "Hello Team! This API seems to be working"}