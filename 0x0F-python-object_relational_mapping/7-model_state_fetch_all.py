#!/usr/bin/python3
""" 1 filter states """

from sqlalchemy import create_engine, Session
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
  # Create argument parser


  username = sys.argv[1]
  password = sys.argv[2]
  database = sys.argv[3]
  # Parse arguments

  engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))
  # Call list_all_states function
  Base.metadata.create_all(engine)

  # Create a session using the engine
  SessionLocal = sessionmaker(bind=engine)
  session = SessionLocal()

  states = session.query(State).order_by(State.id)

  # Print state information
  for state in states:
      print(state.id, state.name, sep=": ")
