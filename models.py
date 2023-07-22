from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.orm import relationship

from .database import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, index=True)
    submenu_id = Column(Integer, ForeignKey('submenu.id'))


class Submenu(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dish = Column(Integer, ForeignKey('dish.id'), unique=True)


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)


menu = relationship('menu', backref='submenu')
submenu = relationship('submenu', backref='dishes')

