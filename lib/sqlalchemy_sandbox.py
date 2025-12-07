# lib/sqlalchemy_sandbox.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# 1. Create a base class for our models
Base = declarative_base()


# 2. Define a Model/Table using ORM
class Student(Base):
    __tablename__ = "students"  # table name in the database

    id = Column(Integer(), primary_key=True)  # primary key column
    name = Column(String())  # text column


# 3. Persist the schema only when running the file directly
if __name__ == "__main__":
    engine = create_engine("sqlite:///students.db")
    Base.metadata.create_all(engine)
