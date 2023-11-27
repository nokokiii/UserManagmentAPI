import src.db as db

conn = db.create_conn("users.db")

def get_all_users():
    conn = db.create_conn("users.db")
    return list(conn["users"].rows)

    
def get_user(user_id):
    conn = db.create_conn("users.db")
    return conn["users"].get(user_id)


def create_user(name, last_name):
    try:
        conn = db.create_conn("users.db")
        conn["users"].insert({"name": name, "last_name": last_name})
        return {"message": "User created successfully"}
    except Exception as e:
        return {"message": str(e)}


def edit_user(user_id, name, last_name):
    try:
        conn = db.create_conn("users.db")
        conn["users"].update({"name": name, "last_name": last_name}, doc_ids=[user_id])
        return {"message": "User updated successfully"}
    except Exception as e:
        return {"message": str(e)}
