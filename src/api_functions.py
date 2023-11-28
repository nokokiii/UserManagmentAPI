import sqlite_utils

import src.db as db

conn = db.create_conn("users.db")

def get_all_users():
    try:
        conn = db.create_conn("users.db")
        return list(conn["users"].rows), 200
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while getting users."}, 500

    
def get_user(user_id):
    try:
        conn = db.create_conn("users.db")
        
        if not conn["users"].get(user_id):
            return {"error": "Not Found", "message": "User does not exist"}, 404
        return conn["users"].get(user_id), 200
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while getting user."}, 500


def create_user(data):
    if 'name' not in data or 'last_name' not in data:
        return {"error": "Bad Request", "message": "Missing values to create user"}, 400
    try:
        conn = db.create_conn("users.db")
        conn["users"].insert({"name": data["name"], "last_name": data["last_name"]})
        return {"message": "User created successfully"}, 201
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while creating user."}, 500


def edit_user(user_id, data):
    if 'name' not in data or 'last_name' not in data:
        return {"error": "Bad Request", "message": "Missing values to update user"}, 400
    try:
        conn = db.create_conn("users.db")
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while updating user."}, 500

    try:
        conn["users"].get(user_id)
        conn["users"].update({"name": data["name"], "last_name": data["last_name"]}, doc_ids=[user_id])
        return {"message": "User updated successfully"}, 204
    except sqlite_utils.db.NotFoundError:
        return {"error": "Not Found", "message": "User does not exist"}, 404
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while updating user."}, 500


def edit_add_user(user_id, data):
    if 'name' not in data or 'last_name' not in data:
        return {"error": "Bad Request", "message": "Missing values to update user"}, 400
    try:
        conn = db.create_conn("users.db")
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while updating user."}, 500

    try:
        conn["users"].get(user_id)
        conn["users"].update({"name": data["name"], "last_name": data["last_name"]}, doc_ids=[user_id])
        return {"message": "User updated successfully"}, 204
    except sqlite_utils.db.NotFoundError:        
        # Add user with id user_id
        conn["users"].insert({"name": data["name"], "last_name": data["last_name"], "id": user_id})
        return {"message": "User created successfully"}, 201
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while updating user."}, 500


def delete_user(user_id):
    try:
        conn = db.create_conn("users.db")
        conn["users"].delete(doc_ids=[user_id])
        return {"message": "User deleted successfully"}, 204
    except sqlite_utils.db.NotFoundError:
        return {"error": "Not Found", "message": "User does not exist"}, 404
    except Exception as e:
        print(e) # TODO: Change this print to logging
        return {"error": "Internal Error", "message": "There was problem while deleting user."}, 500
