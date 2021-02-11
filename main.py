from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello():
    return {"message": "Hello Team! This API seems to be working"}

