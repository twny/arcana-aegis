from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .book import Book


association_table = Table('books_categories', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship(
        "Book",
        secondary=association_table,
        back_populates="categories"
    )


Book.categories = relationship(
    "Category",
    secondary=association_table,
    back_populates="books"
)
