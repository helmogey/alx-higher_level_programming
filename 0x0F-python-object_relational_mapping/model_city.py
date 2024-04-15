#!/usr/bin/python3
""" 1 filter states """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
  __tablename__ = 'cities'

  id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
  name = Column(String(128), nullable=False)
  state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

  state = relationship("State", backref="cities")

  def __repr__(self):
    return f"City(id={self.id}, name='{self.name}', state_id={self.state_id})"
