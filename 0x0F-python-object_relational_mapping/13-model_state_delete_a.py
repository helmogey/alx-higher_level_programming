#!/usr/bin/python3
""" 1 filter states """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states(username, password, database, state_name='Louisiana'):
    """
    Connects to a MySQL database and lists all states from the 'states' table,
    sorting them by id in ascending order.

    Args:
        username: Username for MySQL authentication.
        password: Password for MySQL authentication.
        database: Name of the database to connect to.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))
    # Call list_all_states function
    Base.metadata.create_all(engine)

    # Create a session using the engine
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    # Create argument parser
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]    # Parse arguments

    list_states(username, password, database)


