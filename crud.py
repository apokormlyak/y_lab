from sqlalchemy.orm import Session
from . import models, schemas


def get_menu(db: Session):
    return db.query(models.Menu).all()


def create_menu(db: Session):
    new_menu = models.Menu()
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


def update_menu(db: Session):
    pass


def delete_menu(db: Session):
    menu = db.query(models.Menu).all()
    deleted_submenu = db.query(models.Submenu).all()
    dishes = db.query(models.Dish).all()
    db.delete(dishes)
    db.delete(deleted_submenu)
    db.delete(menu)
    db.commit()
    return 'Меню удалено'


def get_submenu(db: Session):
    return db.query(models.Submenu).all()


def get_submenu_by_id(db: Session, submenu_id: int):
    return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()


def add_submenu(db: Session, new_submenu: schemas.Submenu):
    new_submenu = models.Submenu(name=new_submenu.name, dish=new_submenu.dish)
    db.add(new_submenu)
    db.commit()
    db.refresh(new_submenu)
    return new_submenu


def update_submenu(db: Session, submenu_id: int, new_name: str):
    updated_submenu = db.query(models.Submenu).filter(models.Submenu.id == submenu_id)
    if new_name is not None:
        updated_submenu.update({'name': new_name})
        db.commit()
    return updated_submenu


def delete_submenu_by_id(db: Session, submenu_id: int):
    deleted_submenu = db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()
    submenu_dishes = deleted_submenu.dishes
    db.delete(submenu_dishes)
    db.delete(deleted_submenu)
    db.commit()
    return f'Подменю {deleted_submenu.name} удалено'


def delete_all_submenu(db: Session):
    deleted_submenu = db.query(models.Submenu).all()
    dishes = db.query(models.Dish).all()
    db.delete(dishes)
    db.delete(deleted_submenu)
    db.commit()
    return 'Все подменю удалены'


def get_dishes(db: Session):
    return db.query(models.Dish).all()


def get_dish_by_id(db: Session, dish_id: int):
    return db.query(models.Dish).filter(models.Dish.id == dish_id).first()


def add_dish(db: Session, new_dish: schemas.Dish):
    new_dish = models.Dish(**new_dish.dict())
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish


def update_dish(db: Session, dish_id: int, new_name: str = None, new_price: float = None):
    updated_submenu = db.query(models.Submenu).filter(models.Dish.id == dish_id)
    if new_name is not None:
        updated_submenu.update({'name': new_name})
    if new_price is not None:
        updated_submenu.update({'price': new_price})
    db.commit()
    return updated_submenu


def delete_dish_by_id(db: Session, dish_id: int):
    deleted_dish = db.query(models.Dish).filter(models.Dish.id == dish_id).first()
    db.delete(deleted_dish)
    db.commit()
    return f'Блюдо {deleted_dish.name} удалено'


def delete_all_dishes(db: Session):
    deleted_dish = db.query(models.Dish).all()
    db.delete(deleted_dish)
    db.commit()
    return 'Все блюда удалены'
