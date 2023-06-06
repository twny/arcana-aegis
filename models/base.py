from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# engine_url is a postgres uri postgresql://
# create_all is called from migrate.py
def create_all(engine_url):
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)
