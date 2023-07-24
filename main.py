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


@app.get('/menu', response_model=List[schemas.MenuSchema])
def get_menu(db: Session = Depends(get_db)):
    users = crud.get_menu(db)
    return Response(status_code=status.HTTP_200_OK, content=users)


@app.post('/menu/create_menu', response_model=schemas.MenuSchema)
def create_menu(db: Session = Depends(get_db)):
    new_menu = crud.create_menu(db)
    return Response(status_code=status.HTTP_200_OK, content=new_menu)


@app.put('/menu')
def change_menu(self, menu_id):
    pass


@app.delete('/menu/delete_menu')
def delete_menu(db: Session = Depends(get_db)):
    deleted_menu = crud.delete_menu(db)
    return Response(status_code=status.HTTP_200_OK, content='<h1>Меню удалено успешно</h1> ')


@app.get('/menu/submenu/{submenu_id}', response_model=schemas.SubmenuSchema)
def get_submenu_by_id(submenu_id: int, db: Session = Depends(get_db)):
    submenu = crud.get_submenu_by_id(db, submenu_id)
    return Response(status_code=status.HTTP_200_OK, content=submenu)


@app.get('/menu/submenu', response_model=List[schemas.SubmenuSchema])
def get_submenu(db: Session = Depends(get_db)):
    submenu = crud.get_submenu(db)
    return Response(status_code=status.HTTP_200_OK, content=submenu)


@app.post('/menu/submenu/add_submenu')
def add_submenu(submenu: models.Submenu, db: Session = Depends(get_db)):
    new_submenu = crud.add_submenu(db, submenu)
    submenu = crud.get_submenu(db)
    return Response(status_code=status.HTTP_200_OK, content=submenu)


@app.delete('/menu/submenu/delete_submenu/submenu_id')
def delete_submenu_by_id(submenu_id: int, db: Session = Depends(get_db)):
    deleted_submenu = crud.delete_submenu_by_id(db, submenu_id)
    return Response(status_code=status.HTTP_200_OK, content=f'<h1>Подменю {deleted_submenu.name} удалено успешно</h1>')


@app.delete('/menu/submenu/delete_submenu')
def delete_all_submenu(db: Session = Depends(get_db)):
    deleted_submenu = crud.delete_all_submenu(db)
    return Response(status_code=status.HTTP_200_OK, content='<h1>Все подменю удалено успешны</h1>')


@app.put('/menu/submenu/{submenu_id}/update', response_model=schemas.SubmenuSchema)
def update_submenu(submenu_id, new_name=None, db: Session = Depends(get_db)):
    updated_submenu = crud.update_submenu(db, submenu_id, new_name)
    return Response(status_code=status.HTTP_200_OK, content=updated_submenu)


@app.get('/menu/submenu/{submenu_id}/dishes/{dish_id}', response_model=schemas.DishSchema)
def get_dish_by_id(dish_id: int, db: Session = Depends(get_db)):
    dish = crud.get_dish_by_id(db, dish_id)
    return Response(status_code=status.HTTP_200_OK, content=dish)


@app.get('/menu/submenu/{submenu_id}/dishes', response_model=List[schemas.DishSchema])
def get_dishes(db: Session = Depends(get_db)):
    dishes = crud.get_dishes(db)
    return Response(status_code=status.HTTP_200_OK, content=dishes)


@app.post('/menu/submenu/{submenu_id}/dishes/add_dish')
def add_dish(dish: models.Dishes, db: Session = Depends(get_db)):
    new_dish = crud.add_dish(db, dish)
    dishes = crud.get_dishes(db)
    return Response(status_code=status.HTTP_200_OK, content=dishes)


@app.delete('/menu/submenu/{submenu_id}/delete_dish/dish_id')
def delete_dish_by_id(dish_id: int, db: Session = Depends(get_db)):
    deleted_dish = crud.delete_dish_by_id(db, dish_id)
    return Response(status_code=status.HTTP_200_OK, content=f'<h1>Блюдо {deleted_dish.name} удалено успешно</h1>')


@app.delete('/menu/submenu/{submenu_id}/delete_dish/all')
def delete_all_dishes(db: Session = Depends(get_db)):
    deleted_dishes = crud.delete_all_dishes(db)
    return Response(status_code=status.HTTP_200_OK, content='<h1>Все блюда удалено успешны</h1>')


@app.put('/menu/submenu/{submenu_id}/dishes/{dish_id}/update', response_model=schemas.DishSchema)
def update_dish(dish_id: int, new_name: str = None, new_price: int = None, db: Session = Depends(get_db)):
    updated_dish = crud.update_dish(db, dish_id, new_name, new_price)
    return Response(status_code=status.HTTP_200_OK, content=updated_dish)
