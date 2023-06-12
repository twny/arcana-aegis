from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .associations import association_table


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publication_date = Column(Date)
    page_count = Column(Integer)
    item_type = Column(String)  # new field
    file_format = Column(String)
    file_size = Column(Integer)
    file_location = Column(String)
    hash = Column(String)
    resolution = Column(String)
    security = Column(String)
    content_creator = Column(String)
    encoding_software = Column(String)

    author = relationship("Author", back_populates="items")
    publisher = relationship("Publisher", back_populates="items")
    categories = relationship(
        "Category",
        secondary=association_table,
        back_populates="items",
        lazy='joined'
    )
