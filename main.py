from fastapi import FastAPI, status, Depends
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


@app.get('/menu')
def get_menu(db: Session = Depends(get_db)):
    menu = crud.get_menu(db)
    return menu


@app.post('/menu/create_menu', response_model=schemas.MenuSchema)
def create_menu(menu: schemas.MenuSchema, db: Session = Depends(get_db)):
    new_menu = crud.create_menu(db, menu)
    return new_menu


@app.put('/menu/{submenu_id}/update', response_model=schemas.MenuSchema)
def update_menu(menu_id, new_name=None, db: Session = Depends(get_db)):
    updated_menu = crud.update_submenu(db, menu_id, new_name)
    return updated_menu


@app.delete('/menu/delete_menu')
def delete_menu(db: Session = Depends(get_db)):
    deleted_menu = crud.delete_menu(db)
    return Response(status_code=status.HTTP_200_OK, content='<h1>Меню удалено успешно</h1> ')


@app.delete('/menu/delete_menu/menu_id')
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    deleted_menu = crud.delete_submenu_by_id(db, menu_id)
    return Response(status_code=status.HTTP_200_OK, content=f'<h1>Подменю {deleted_menu.name} удалено успешно</h1>')


@app.get('/submenu/{submenu_id}', response_model=schemas.SubmenuSchema)
def get_submenu_by_id(submenu_id: int, db: Session = Depends(get_db)):
    submenu = crud.get_submenu_by_id(db, submenu_id)
    return submenu


@app.get('/submenu', response_model=List[schemas.SubmenuSchema])
def get_submenu(db: Session = Depends(get_db)):
    submenu = crud.get_submenu(db)
    return List[submenu]


@app.post('/submenu/add_submenu', response_model=List[schemas.SubmenuSchema])
def add_submenu(submenu: schemas.SubmenuSchema, db: Session = Depends(get_db)):
    new_submenu = crud.add_submenu(db, submenu)
    submenu = crud.get_submenu(db)
    return List[submenu]


@app.delete('/submenu/delete_submenu/submenu_id')
def delete_submenu_by_id(submenu_id: int, db: Session = Depends(get_db)):
    deleted_submenu = crud.delete_submenu_by_id(db, submenu_id)
    return Response(status_code=status.HTTP_200_OK, content=f'<h1>Подменю {deleted_submenu.name} удалено успешно</h1>')


@app.delete('/submenu/delete_submenu')
def delete_all_submenu(db: Session = Depends(get_db)):
    deleted_submenu = crud.delete_all_submenu(db)
    return Response(status_code=status.HTTP_200_OK, content='<h1>Все подменю удалено успешны</h1>')


@app.put('/submenu/{submenu_id}/update', response_model=schemas.SubmenuSchema)
def update_submenu(submenu_id, new_name=None, db: Session = Depends(get_db)):
    updated_submenu = crud.update_submenu(db, submenu_id, new_name)
    return updated_submenu


@app.get('/submenu/{submenu_id}/dishes/{dish_id}', response_model=schemas.DishSchema)
def get_dish_by_id(dish_id: int, db: Session = Depends(get_db)):
    dish = crud.get_dish_by_id(db, dish_id)
    return dish


@app.get('/submenu/{submenu_id}/dishes', response_model=List[schemas.DishSchema])
def get_dishes(db: Session = Depends(get_db)):
    dishes = crud.get_dishes(db)
    return List[dishes]


@app.post('/submenu/{submenu_id}/dishes/add_dish', response_model=List[schemas.DishSchema])
def add_dish(dish: schemas.DishSchema, db: Session = Depends(get_db)):
    new_dish = crud.add_dish(db, dish)
    dishes = crud.get_dishes(db)
    return List[dishes]


@app.delete('/submenu/{submenu_id}/delete_dish/dish_id')
def delete_dish_by_id(dish_id: int, db: Session = Depends(get_db)):
    deleted_dish = crud.delete_dish_by_id(db, dish_id)
    return Response(status_code=status.HTTP_200_OK, content=f'<h1>Блюдо {deleted_dish.name} удалено успешно</h1>')


@app.delete('/submenu/{submenu_id}/delete_dish/all')
def delete_all_dishes(db: Session = Depends(get_db)):
    deleted_dishes = crud.delete_all_dishes(db)
    return Response(status_code=status.HTTP_200_OK, content='<h1>Все блюда удалено успешны</h1>')


@app.put('/submenu/{submenu_id}/dishes/{dish_id}/update', response_model=schemas.DishSchema)
def update_dish(dish_id: int, new_name: str = None, new_price: int = None, db: Session = Depends(get_db)):
    updated_dish = crud.update_dish(db, dish_id, new_name, new_price)
    return updated_dish
