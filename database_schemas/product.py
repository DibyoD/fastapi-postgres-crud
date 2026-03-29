from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, FLOAT

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(FLOAT)
    quantity = Column(INTEGER)


