import logging

import sqlite_utils

import src.db as db


def get_all_users():
    try:
        conn = db.create_conn()
        return list(conn.query("select rowid, * from users")), 200
    
    except Exception as e:
        logging.error(e)
        return {"error": "Internal Error", "message": "There was problem while getting users."}, 500

    
def get_user(user_id):
    try:
        conn = db.create_conn()
        return conn["users"].get(user_id), 200
    
    except sqlite_utils.db.NotFoundError:
        return {"error": "Not Found", "message": "User does not exist"}, 404
    
    except Exception as e:
        logging.error(e)
        return {"error": "Internal Error", "message": "There was problem while getting user."}, 500


def create_user(data):
    if 'name' not in data or 'lastname' not in data:
        return {"error": "Bad Request", "message": "Missing values to create user"}, 400
    
    try:
        conn = db.create_conn()
        conn["users"].insert({"name": data["name"], "lastname": data["lastname"]})
        return {"message": "User created successfully"}, 201
    
    except Exception as e:
        logging.error(e)
        return {"error": "Internal Error", "message": "There was problem while creating user."}, 500


def edit_user(user_id, data):
    try:
        conn = db.create_conn()        
        conn["users"].get(user_id)
    except sqlite_utils.db.NotFoundError:
        return {"error": "Not Found", "message": "User does not exist"}, 404
    except Exception as e:
        logging.error(e)
        return {"error": "Internal Error", "message": "There was problem while updating user."}, 500

    if 'name' in data:
        try:
            conn["users"].update(user_id, {"name": data["name"]})
            return {}, 204
        
        except Exception as e:
            logging.error(e)
            return {"error": "Internal Error", "message": "There was problem while updating user."}, 500
    
    elif 'lastname' in data:
        try:
            conn["users"].update(user_id, {"lastname": data["lastname"]})
            return {}, 204
            
        except Exception as e:
            logging.error(e)
            return {"error": "Internal Error", "message": "There was problem while updating user."}, 500
    
    else:
        return {"error": "Bad Request", "message": "Missing values to update user"}, 400


def edit_add_user(user_id, data):
    if 'name' not in data or 'lastname' not in data:
        return {"error": "Bad Request", "message": "Missing values to update user"}, 400
    
    try:
        conn = db.create_conn()
        
    except Exception as e:
        logging.error(e)
        return {"error": "Internal Error", "message": "There was problem while updating user."}, 500

    try:
        conn["users"].get(user_id)
        conn["users"].upsert({"rowid": user_id, "name": data["name"], "lastname": data["lastname"]}, pk="rowid", column_order=["name", "lastname"])
        return {}, 204
    
    except sqlite_utils.db.NotFoundError:
        conn["users"].insert({"name": data["name"], "lastname": data["lastname"], "rowid": user_id})
        return {"message": "User created successfully"}, 201
    
    except Exception as e:
        logging.error(e)
        return {"error": "Internal Error", "message": "There was problem while updating user."}, 500


def delete_user(user_id):
    try:
        conn = db.create_conn()
        conn["users"].delete(user_id)
        return {}, 204
    
    except sqlite_utils.db.NotFoundError:
        return {"error": "Not Found", "message": "User does not exist"}, 404
    
    except Exception as e:
        logging.error(e)
        return {"error": "Internal Error", "message": "There was problem while deleting user."}, 500
