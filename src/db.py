"""
This file contains the functions that are used to interact with the database.
"""

import sqlite3
from typing import Optional

from sqlite_utils import Database

EXAMPLE_USERS = [
    {"name": "John", "last_name": "Doe"},
    {"name": "Alex", "last_name": "Smith"},
    {"name": "Emily", "last_name": "Johnson"},
    {"name": "Chris", "last_name": "Williams"},
    {"name": "Jessica", "last_name": "Brown"},
    {"name": "Michael", "last_name": "Davis"}
]


def create_conn(database: str) -> Optional[sqlite3.Connection]:
    """
    Creates a connection to the database.

    Args:
        database (str): The path to the database file.

    Returns:
        Optional[sqlite3.Connection]: The connection object if successful, None otherwise.
    """
    try:
        return Database(database)
    except sqlite3.Error as e:
        print(f"Error creating connection to database: {e}")
        return None


def add_example_users(database: str) -> None:
    for user in EXAMPLE_USERS:
        try:
            database["users"].insert(user)
        except sqlite3.Error as e:
            print(f"Error adding user to database: {e}")

                
def create_db(database: str, example_users: bool=False) -> None:
    if db := create_conn(database):
        print("Database created successfully.")  # TODO: Change this print to logging
        if example_users:
            add_example_users(db)
    else:
        print("Could not create database.") # TODO: Change this print to logging
        return


if __name__ == '__main__':
    create_db("./users.db", True)
