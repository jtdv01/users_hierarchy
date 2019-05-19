def empty_db():
    db = {}
    return db

def set_users(db, users):
    """
    Add users to a key-value store db
    :return: db
    """
    db['users'] = users
    return db

def set_roles(db, roles):
    """
    Add roles to a key-value store db
    :return: db
    """
    db['roles'] = roles
    return db

def add_users_to_role_lookup(db, roles, users):
    """
    Add users within the roles for a faster lookup

    :return: db
    """

    # Role membership shows the list of users belonging to a role
    db['role_membership'] = {}

    for user_id, u in users.items():
        user_role_id = u.role_id
        try:
            # Add the user id to a role membership in the db
            db['role_membership'][user_role_id]= db['role_membership'][user_role_id].add(user_role_id)
        except KeyError as e:
            # If not found, init an empty set
            db['role_membership'][user_role_id] = set([user_id])

    return db

def init_db(roles, users):
    """
    Initialise a simple key-value store database

    :return: db
    :rtype: dict
    """
    db = empty_db()
    db = set_roles(db, roles)
    db = set_users(db, users)
    db = add_users_to_role_lookup(db, roles, users)
    return db
