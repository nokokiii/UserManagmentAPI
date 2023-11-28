"""
This file contains the functions that are used to interact with the database.
"""

import sqlite3
import logging
from typing import Optional

from sqlite_utils import Database

DATABASE = "users.db"

EXAMPLE_USERS = [
    {"name": "John", "lastname": "Doe"},
    {"name": "Alex", "lastname": "Smith"},
    {"name": "Emily", "lastname": "Johnson"},
    {"name": "Chris", "lastname": "Williams"},
    {"name": "Jessica", "lastname": "Brown"},
    {"name": "Michael", "lastname": "Davis"}
]


def create_conn() -> Optional[sqlite3.Connection]:
    """
    Creates a connection to the database.

    Args:
        database (str): The path to the database file.

    Returns:
        Optional[sqlite3.Connection]: The connection object if successful, None otherwise.
    """
    try:
        logging.info("Creating connection to database")
        return Database(DATABASE)
    except sqlite3.Error as e:
        logging.error(e)
        return None


def add_example_users() -> None:
    """
    Adds the example users to the database.
        
    Returns:
        None
    """
    db = create_conn()
    for user in EXAMPLE_USERS:
        try:
            db["users"].insert(user)
        except sqlite3.Error as e:
            print(f"Error adding user to database: {e}")


if __name__ == '__main__':
    add_example_users()
