def empty_db():
    db = {}
    return db

def set_users(db, users):
    db['users'] = users
    return db

def set_roles(db, roles):
    db['roles'] = roles
    return db

def init_db(roles, users):
    db = empty_db()
    db = set_roles(db, roles)
    db = set_users(db, users)
    return db
