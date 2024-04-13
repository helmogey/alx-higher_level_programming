from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define declarative base class
Base = declarative_base()

# Define State class
class State(Base):
  __tablename__ = 'states'  # Table name for the model

  id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
  name = Column(String(128), nullable=False)

  def __repr__(self):
    return f"State(id={self.id}, name='{self.name}')"

# Connect to MySQL server (replace with your credentials)
engine = create_engine('mysql://username:password@localhost:3306/database_name')

# Create all tables defined from the Base class (uncomment when needed)
# Base.metadata.create_all(engine)
