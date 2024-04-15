#!/usr/bin/python3
""" 1 filter states """

import MySQLdb
import sys

def list_states(username, password, database, state_name):
  """
  Connects to a MySQL database and lists all states from the 'states' table,
  sorting them by id in ascending order.

  Args:
      username: Username for MySQL authentication.
      password: Password for MySQL authentication.
      database: Name of the database to connect to.
  """

  try:
    # Connect to the MySQL server
    connection = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    cursor = connection.cursor()

    # Execute query to select all states ordered by id
    query = "SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name=%s"
    cursor.execute(query, (state_name, ))


    # Fetch results and print them
    for row in cursor.fetchall():
      print(row)

    # Close connection
    cursor.close()
    connection.close()

  except MySQLdb.Error as err:
    print(f"Error connecting to database: {err}")

# Script execution should not happen when imported
if __name__ == "__main__":
  username = sys.argv[1]
  password = sys.argv[2]
  database = sys.argv[3]
  state_name = sys.argv[4]
  list_states(username, password, database, state_name)
