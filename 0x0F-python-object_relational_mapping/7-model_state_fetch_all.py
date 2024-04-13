#!/usr/bin/python3
""" 1 filter states """

from sqlalchemy import create_engine, Session
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
def list_all_states(username, password, database):
  """
  Connects to a MySQL database, creates a session, and lists all State objects
  from the 'states' table, sorted by id in ascending order.

  Args:
      username: Username for MySQL authentication.
      password: Password for MySQL authentication.
      database: Name of the database to connect to.
  """

  # Create database engine connection URL
  engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')

  # Create a session using the engine
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  session = SessionLocal()

  try:
    # Query all State objects ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print state information
    for state in states:
      print(state)

  except Exception as err:
    pass
  finally:
    # Close the session
    session.close()

if __name__ == "__main__":
  # Create argument parser


  username = sys.argv[1]
  password = sys.argv[2]
  database = sys.argv[3]
  # Parse arguments

  # Call list_all_states function
  list_all_states(username, password, database)
