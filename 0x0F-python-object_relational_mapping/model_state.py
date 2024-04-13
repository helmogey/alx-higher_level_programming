#!/usr/bin/python3
""" 1 filter states """

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
# Define declarative base class
Base = declarative_base()

# Define State class
class State(Base):
  __tablename__ = 'states'  # Table name for the model

  id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
  name = Column(String(128), nullable=False)


