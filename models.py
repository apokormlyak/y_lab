from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.orm import relationship

from .database import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    submenu_id = Column(Integer, ForeignKey('submenu.id'), index=True, ondelete="CASCADE")
    submenu = relationship("Submenu", foreign_keys=[submenu_id], lazy="selectin")


class Submenu(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    dish_id = Column(Integer, ForeignKey('dishes.id'), index=True, ondelete="CASCADE")
    dish = relationship("Dishes", foreign_keys=[dish_id], lazy="selectin")


class Dishes(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)


menu = relationship('menu', backref='submenu')
submenu = relationship('submenu', backref='dishes')

