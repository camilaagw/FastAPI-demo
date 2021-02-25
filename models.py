from pydantic import BaseModel, constr
from typing import List


class Article(BaseModel):
    content: constr(max_length=255)
    comments: List[str] = []
