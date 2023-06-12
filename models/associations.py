from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

association_table = Table('items_categories', Base.metadata,
    Column('item_id', Integer, ForeignKey('items.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)
