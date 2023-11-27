"""
This file contains the functions that are used to interact with the database.
"""

import logging
import os
import sqlite3
from typing import Optional

from sqlite_utils import Database

LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "db.log")

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CREATION_QUERY = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
"""

EXAMPLE_USERS = [
    {"name": "John", "last_name": "Doe"},
    {"name": "Alex", "last_name": "Smith"},
    {"name": "Emily", "last_name": "Johnson"},
    {"name": "Chris", "last_name": "Williams"},
    {"name": "Jessica", "last_name": "Brown"},
    {"name": "Michael", "last_name": "Davis"}
]

logging.basicConfig(level=logging.DEBUG)


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
        logging.error(f"Error creating connection to database: {e}")
        return None


def add_example_users(database: str) -> None:
    for user in EXAMPLE_USERS:
        try:
            database["users"].insert(user)
        except sqlite3.Error as e:
            logging.error(f"Error adding user to database: {e}")
                
def create_db(database: str, example_users: bool=False) -> None:
    if db := create_conn(database):
        db.query(CREATION_QUERY)
        logging.info("Database created successfully.")
        if example_users:
            add_example_users(db)
    else:
        logging.error("Could not create database.")
        return


if __name__ == '__main__':
    create_db("users.db", True)
