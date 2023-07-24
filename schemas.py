from pydantic import BaseModel
from models import Menu, Submenu, Dishes
from typing import Optional


class MenuSchema(BaseModel):
    id: int
    submenu: Optional[int]

    class Meta:
        orm_model = Menu

    class Config:
        orm_mode = True


class SubmenuSchema(BaseModel):
    id: int
    name: str
    dish: Optional[int]

    class Meta:
        orm_model = Submenu

    class Config:
        orm_mode = True


class DishSchema(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[int]

    class Meta:
        orm_model = Dishes

    class Config:
        orm_mode = True

