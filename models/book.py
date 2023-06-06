from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .author import Author
from .publisher import Publisher


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
