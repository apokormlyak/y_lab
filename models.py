from sqlalchemy import ForeignKey, Integer, String, Column, ARRAY
from sqlalchemy.orm import relationship

from database import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    submenu_count = Column(Integer, default=0)
    dish_count = Column(Integer, default=0)
    submenu = relationship("Submenu", back_populates="menu", lazy="selectin")


class Submenu(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)
    menu_id = Column(Integer, ForeignKey('menu.id', ondelete="CASCADE"), index=True)
    description = Column(String, index=True)
    dish_count = Column(Integer, default=0)
    menu = relationship("Menu", foreign_keys=[menu_id], back_populates='submenu', lazy="selectin")
    dishes = relationship("Dishes", back_populates='submenu', lazy="selectin")


class Dishes(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    submenu_id = Column(Integer, ForeignKey('submenu.id', ondelete="CASCADE"), index=True)
    menu_id = Column(Integer, ForeignKey('menu.id', ondelete="CASCADE"), index=True)
    name = Column(String, index=True, unique=True)
    price = Column(Integer, index=True)
    description = Column(String, index=True)
    submenu = relationship("Submenu", back_populates='dishes', foreign_keys=[submenu_id], lazy="selectin")
