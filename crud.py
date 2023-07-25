from sqlalchemy.orm import Session
import models
import schemas


def get_menu(db: Session):
    return db.query(models.Menu).all()


def get_menu_by_id(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def create_menu(db: Session, new_menu: schemas.MenuSchema):
    new_menu = models.Menu(title=new_menu.title)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


def update_menu(db: Session, menu_id: int, title: str):
    db.query(models.Menu).filter(models.Menu.id == menu_id).update({'title': title})
    db.commit()
    updated_menu = get_menu_by_id(db, menu_id)
    return updated_menu


def delete_menu(db: Session):
    db.query(models.Menu).delete()
    db.commit()
    return {"ok": True}


def delete_menu_by_id(db: Session, menu_id: int):
    deleted_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).delete()
    db.commit()
    return {"ok": True}


def get_submenu(db: Session):
    return db.query(models.Submenu).all()


def get_submenu_by_id(db: Session, submenu_id: int):
    return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()


def get_submenu_by_name(db: Session, title: str):
    return db.query(models.Submenu).filter(models.Submenu.title == title).first()


def add_submenu(db: Session, new_submenu: schemas.SubmenuSchema):
    new_submenu = models.Submenu(title=new_submenu.title, menu_id=new_submenu.menu_id,
                                 description=new_submenu.description)
    submenu_count = db.query(models.Submenu).filter(models.Submenu.menu_id == new_submenu.menu_id).count()
    db.add(new_submenu)
    db.query(models.Menu).filter(models.Menu.id == new_submenu.menu_id).update({'submenu_count': submenu_count+1})
    db.commit()
    db.refresh(new_submenu)
    return new_submenu


def update_submenu(db: Session, submenu_id: int, title: str):
    updated_submenu = db.query(models.Submenu).filter(models.Submenu.id == submenu_id)
    if title is not None:
        updated_submenu.update({'title': title})
        db.commit()
    return updated_submenu


def delete_submenu_by_id(db: Session, submenu_id: int):
    menu_id = db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first().menu_id
    submenu_count = db.query(models.Submenu).filter(models.Submenu.menu_id == menu_id).count()
    deleted_submenu = db.query(models.Submenu).filter(models.Submenu.id == submenu_id).delete()
    db.query(models.Menu).filter(models.Menu.id == menu_id).update({'submenu_count': submenu_count-1})
    db.commit()
    return {"ok": True}


def delete_all_submenu(db: Session, menu_id: int):
    del_submenu = db.query(models.Submenu).filter(models.Submenu.menu_id == menu_id).first()
    submenu_dish_count = del_submenu.dish_count
    menu_dish_count = db.query(models.Menu).filter(models.Menu.id == menu_id).first().dish_count
    menu_submenu_count = db.query(models.Menu).filter(models.Menu.id == menu_id).first().submenu_count
    del_submenu.delete()
    db.query(models.Menu).filter(models.Menu.id == menu_id).update({'submenu_count': menu_submenu_count-1})
    db.query(models.Menu).filter(models.Menu.id == menu_id).update({'dish_count': menu_dish_count-submenu_dish_count})

    db.commit()
    return {"ok": True}


def get_dishes(db: Session):
    return db.query(models.Dishes).all()


def get_dish_by_id(db: Session, dish_id: int):
    return db.query(models.Dishes).filter(models.Dishes.id == dish_id).first()


def get_dish_by_name(db: Session, title: str):
    return db.query(models.Dishes).filter(models.Dishes.title == title).first()


def add_dish(db: Session, new_dish: schemas.DishSchema):
    new_dish = models.Dishes(title=new_dish.title, price=new_dish.price, description=new_dish.description,
                             submenu_id=new_dish.submenu_id, menu_id=new_dish.menu_id)
    dish_count = db.query(models.Dishes).filter(models.Dishes.submenu_id == new_dish.submenu_id).count()
    db.add(new_dish)
    db.query(models.Submenu).filter(models.Submenu.id == new_dish.submenu_id).update({'dish_count': dish_count+1})
    db.query(models.Menu).filter(models.Menu.id == new_dish.menu_id).update({'dish_count': dish_count+1})
    db.commit()
    db.refresh(new_dish)
    return new_dish


def update_dish(db: Session, submenu_id: int, dish_id: int, title: str, new_price: float):
    updated_dish = db.query(models.Dishes).filter(models.Dishes.submenu_id == submenu_id, models.Dishes.id == dish_id)
    if title is not None:
        updated_dish.update({'title': title})
    updated_dish.update({'price': new_price})
    db.commit()
    return updated_dish


def delete_dish_by_id(db: Session, dish_id: int):
    deleted_dish = db.query(models.Dishes).filter(models.Dishes.id == dish_id)
    submenu = db.query(models.Submenu).filter(models.Submenu.id == deleted_dish.submenu_id).first()
    menu_id = db.query(models.Submenu).filter(models.Submenu.id == submenu.id).first().menu_id
    dish_count = db.query(models.Dishes).filter(models.Dishes.submenu_id == submenu.id).count()
    deleted_dish.delete()
    db.query(models.Submenu).filter(models.Submenu.id == submenu.id).update({'dish_count': dish_count-1})
    db.query(models.Menu).filter(models.Menu.id == menu_id).update({'dish_count': dish_count-1})
    db.commit()
    return {"ok": True}


def delete_all_dishes(db: Session, submenu_id: int):
    del_dishes = db.query(models.Dishes).filter(models.Dishes.submenu_id == submenu_id).first()
    del_submenu = db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()
    menu = db.query(models.Menu).filter(models.Menu.id == del_submenu.menu_id).first()
    submenu_dish_count = del_submenu.dish_count
    menu_dish_count = menu.dish_count
    dish_count = db.query(models.Submenu).filter(models.Dishes.submenu_id == submenu_id).count()
    del_dishes.delete()
    menu.update({'dish_count': menu_dish_count-dish_count})
    del_submenu.update({'dish_count': submenu_dish_count-dish_count})
    db.commit()
    return {"ok": True}
