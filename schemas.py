from pydantic import BaseModel
from models import Menu, Submenu, Dishes
from typing import Optional


class MenuSchema(BaseModel):
    title: str

    class Meta:
        orm_model = Menu

    class Config:
        orm_mode = True


class SubmenuSchema(BaseModel):
    title: str
    menu_id: int
    description: Optional[str]

    class Meta:
        orm_model = Submenu

    class Config:
        orm_mode = True


class DishSchema(BaseModel):
    submenu_id: int
    menu_id: int
    title: str
    price: float
    description: Optional[str]

    class Meta:
        orm_model = Dishes

    class Config:
        orm_mode = True

