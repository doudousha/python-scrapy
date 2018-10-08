from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    # 车主
    name = Column(String(128))
