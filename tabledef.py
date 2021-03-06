"""
tabledef.py
Defines the database for SQLalchemy

Created by Duncan Stothers in 2018 at Harvard University for Cabot Cafe
Licensed under MIT License
"""

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///drinks.db', echo=True)
Base = declarative_base()

# Define table with just one row for drink names
class User(Base):

    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

Base.metadata.create_all(engine)
