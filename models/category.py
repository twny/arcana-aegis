from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .associations import association_table


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    items = relationship(
        "Item",
        secondary=association_table,
        back_populates="categories",
        lazy='joined'
    )
