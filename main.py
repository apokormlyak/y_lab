from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import Response
import crud
import models
import schemas
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/api/v1/menus')
def get_menu(db: Session = Depends(get_db)):
    menu = crud.get_menu(db)
    return menu


@app.get('/api/v1/menus/{menu_id}')
def get_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menu = crud.get_menu_by_id(db, menu_id)
    return menu


@app.post('/api/v1/menus', response_model=schemas.MenuSchema)
def create_menu(menu: schemas.MenuSchema, db: Session = Depends(get_db)):
    new_menu = crud.create_menu(db, menu)
    return new_menu


@app.patch('/api/v1/menus/{menu_id}')
def update_menu(menu_id, new_name='default', db: Session = Depends(get_db)):
    updated_menu = crud.update_menu(db, menu_id, new_name)
    return updated_menu


@app.delete('/api/v1/menus')
def delete_menu(db: Session = Depends(get_db)):
    deleted_menu = crud.delete_menu(db)
    return 'Все меню удалены успешно'


@app.delete('/api/v1/menus/{menu_id}')
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    deleted_menu = crud.delete_menu_by_id(db, menu_id)
    return deleted_menu


@app.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}')
def get_submenu_by_id(submenu_id: int, db: Session = Depends(get_db)):
    submenu = crud.get_submenu_by_id(db, submenu_id)
    return submenu


@app.get('/api/v1/menus/{menu_id}/submenus')
def get_submenu(db: Session = Depends(get_db)):
    submenu = crud.get_submenu(db)
    return submenu


@app.post('/api/v1/menus/{menu_id}/submenus')
def add_submenu(submenu: schemas.SubmenuSchema, db: Session = Depends(get_db)):
    if (crud.get_menu_by_id(db, submenu.menu_id)) is None:
        raise HTTPException(status_code=404, detail='Меню с таким id не существует')
    if (crud.get_submenu_by_name(db, submenu.title)) is not None:
        raise HTTPException(status_code=404, detail='Подменю с таким названием уже существует')
    new_submenu = crud.add_submenu(db, submenu)
    submenu = crud.get_submenu(db)
    return submenu


@app.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}')
def delete_submenu_by_id(submenu_id: int, db: Session = Depends(get_db)):
    deleted_submenu = crud.delete_submenu_by_id(db, submenu_id)
    return deleted_submenu


@app.delete('/s/api/v1/menus/{menu_id}/submenus')
def delete_all_submenu(menu_id: int, db: Session = Depends(get_db)):
    deleted_submenu = crud.delete_all_submenu(db, menu_id)
    return 'Все подменю удалено успешны'


@app.patch('/api/v1/menus/{menu_id}/submenus/{submenu_id}')
def update_submenu(submenu_id, new_name=None, db: Session = Depends(get_db)):
    updated_submenu = crud.update_submenu(db, submenu_id, new_name)
    return updated_submenu


@app.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def get_dish_by_id(dish_id: int, db: Session = Depends(get_db)):
    dish = crud.get_dish_by_id(db, dish_id)
    return dish


@app.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes')
def get_dishes(db: Session = Depends(get_db)):
    dishes = crud.get_dishes(db)
    return dishes


@app.post('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes')
def add_dish(dish: schemas.DishSchema, db: Session = Depends(get_db)):
    if (crud.get_dish_by_name(db, dish.title)) is not None:
        raise HTTPException(status_code=404, detail='Блюдо с таким названием уже существует')
    new_dish = crud.add_dish(db, dish)
    dishes = crud.get_dishes(db)
    return dishes


@app.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def delete_dish_by_id(dish_id: int, db: Session = Depends(get_db)):
    deleted_dish = crud.delete_dish_by_id(db, dish_id)
    return deleted_dish


@app.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes')
def delete_all_dishes(submenu_id: int, db: Session = Depends(get_db)):
    deleted_dishes = crud.delete_all_dishes(db, submenu_id)
    return 'Все блюда удалены успешны'


@app.patch('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def update_dish(submenu_id: int, dish_id: int, new_name: str = None, new_price: int = None,
                db: Session = Depends(get_db)):
    updated_dish = crud.update_dish(db, submenu_id, dish_id, new_name, new_price)
    return updated_dish
