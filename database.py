
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



db_url = "postgresql://<username>:<password>@<host>:<port>/product-crud"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, bind=engine)