from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Publisher(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    items = relationship("Item", back_populates="publisher")
