from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.orm import relationship

from database import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    submenu_id = Column(Integer, ForeignKey('submenu.id', ondelete="CASCADE"), index=True, nullable=True)
    submenu = relationship("Submenu", foreign_keys=[submenu_id], lazy="selectin")


class Submenu(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    menu_id = Column(Integer, ForeignKey('submenu.id', ondelete="CASCADE"), index=True)
    dish_id = Column(Integer, ForeignKey('dishes.id', ondelete="CASCADE"), index=True, nullable=True)
    dish = relationship("Dishes", foreign_keys=[dish_id], lazy="selectin")
    description = Column(String, index=True)


class Dishes(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)
    description = Column(String, index=True)
