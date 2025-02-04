from pydantic import BaseModel

class ItemCreate(BaseModel):
    title: str
    description: str


class Item(BaseModel):
    id: int
    title: str
    description: str