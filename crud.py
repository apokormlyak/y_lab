from sqlalchemy.orm import Session
import models
import schemas


def get_menu(db: Session):
    return db.query(models.Menu).all()


def create_menu(db: Session, new_menu: schemas.MenuSchema):
    new_menu = models.Menu(name=new_menu.name)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


def update_menu(db: Session, menu_id: int, new_name: str):
    updated_menu = db.query(models.Menu).filter(models.Menu.id == menu_id)
    if new_name is not None:
        updated_menu.update({'name': new_name})
    db.commit()
    return updated_menu


def delete_menu(db: Session):
    menu = db.query(models.Menu).all()
    db.delete(menu)
    db.commit()
    return 'Меню удалено'


def delete_menu_by_id(db: Session, menu_id: int):
    deleted_menu = db.query(models.Submenu).filter(models.Menu.id == menu_id).first()
    db.commit()
    return f'Подменю {deleted_menu.name} удалено'


def get_submenu(db: Session):
    return db.query(models.Submenu).all()


def get_submenu_by_id(db: Session, submenu_id: int):
    return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()


def add_submenu(db: Session, new_submenu: schemas.SubmenuSchema):
    new_submenu = models.Submenu(name=new_submenu.name, menu_id=new_submenu.menu_id,
                                 description=new_submenu.description)
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
    db.commit()
    return f'Подменю {deleted_submenu.name} удалено'


def delete_all_submenu(db: Session):
    deleted_submenu = db.query(models.Submenu).all()
    db.delete(deleted_submenu)
    db.commit()
    return 'Все подменю удалены'


def get_dishes(db: Session):
    return db.query(models.Dishes).all()


def get_dish_by_id(db: Session, dish_id: int):
    return db.query(models.Dishes).filter(models.Dishes.id == dish_id).first()


def add_dish(db: Session, new_dish: schemas.DishSchema):
    new_dish = models.Dishes(name=new_dish.name, price=new_dish.price, description = new_dish.description)
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish


def update_dish(db: Session, dish_id: int, new_name: str = None, new_price: float = None):
    updated_submenu = db.query(models.Submenu).filter(models.Dishes.id == dish_id)
    if new_name is not None:
        updated_submenu.update({'name': new_name})
    if new_price is not None:
        updated_submenu.update({'price': new_price})
    db.commit()
    return updated_submenu


def delete_dish_by_id(db: Session, dish_id: int):
    deleted_dish = db.query(models.Dishes).filter(models.Dishes.id == dish_id).first()
    db.delete(deleted_dish)
    db.commit()
    return f'Блюдо {deleted_dish.name} удалено'


def delete_all_dishes(db: Session):
    deleted_dish = db.query(models.Dishes).all()
    db.delete(deleted_dish)
    db.commit()
    return 'Все блюда удалены'
