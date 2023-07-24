from pydantic import BaseModel
from models import Menu, Submenu, Dishes
from typing import Optional


class MenuSchema(BaseModel):
    name: str

    class Meta:
        orm_model = Menu

    class Config:
        orm_mode = True


class SubmenuSchema(BaseModel):
    name: str
    menu_id: int
    description: Optional[str]

    class Meta:
        orm_model = Submenu

    class Config:
        orm_mode = True


class DishSchema(BaseModel):
    submenu_id: int
    name: str
    price: float
    description: Optional[str]

    class Meta:
        orm_model = Dishes

    class Config:
        orm_mode = True

