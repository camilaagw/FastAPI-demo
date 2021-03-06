import json
from app.main import app


def save_openapi_json():
    openapi_data = app.openapi()
    with open("app/openapi.json", "w") as file:
        json.dump(openapi_data, file)


if __name__ == "__main__":
    save_openapi_json()