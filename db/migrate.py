from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publication_date = Column(Date)
    page_count = Column(Integer)
    file_format = Column(String)
    file_size = Column(Integer)
    file_location = Column(String)
    hash = Column(String)
    resolution = Column(String)
    security = Column(String)
    content_creator = Column(String)
    encoding_software = Column(String)

    author = relationship("Author", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="author")


class Publisher(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="publisher")


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
        back_populates="categories")


Book.categories = relationship(
    "Category",
    secondary=association_table,
    back_populates="books")

if __name__ == "__main__":
    engine = create_engine('postgresql://localhost/arcana_aegis')
    Base.metadata.create_all(engine)
