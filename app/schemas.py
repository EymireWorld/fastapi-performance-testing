from pydantic import BaseModel


__all__ = ['ItemSchema']


class ItemSchema(BaseModel):
    id: int
    name: str
    value: float
    quantity: int
