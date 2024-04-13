#!/usr/bin/python3
""" 1 filter states """

from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def fetch_cities_by_state(username, password, database):
    """
    Connects to a MySQL database, creates a session, and retrieves all City objects
    from the 'cities' table, sorted by id, belonging to a specified state.

    Args:
        username: Username for MySQL authentication.
        password: Password for MySQL authentication.
        database: Name of the database to connect to.
    """

    # Create database engine connection URL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))
    Base.metadata.create_all(engine)
    # Create a session using the engine
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        # Query all City objects ordered by id
        cities = (session.query(State.name, City.id, City.name).filter(State.id == City.state_id))

        for city in cities:
            # Get the state name from the relationship
            state_name = city.state.name
            print(f"{state_name}: ({city.id}) {city.name}")
    except:
        pass


if __name__ == "__main__":
    # Create argument parser
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]  # Parse arguments


    # Call fetch_cities_by_state function
    fetch_cities_by_state(username, password, database)
