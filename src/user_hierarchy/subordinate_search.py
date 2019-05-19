from user import User
import logging

def subordinate_search(db: dict, user_id: int):
    """
    Returns a set of user ids that are under a given parent_user_id

    :return subordinate_roles: 
    :rtype: set
    """

    # Find out the role of the user
    role_id = db['users'][user_id].role_id

    # Find out the subordinate roles of this user
    subordinate_roles = db['roles'][role_id].find_subordinate_roles()
    logging.info(f"The subordinate roles under this user is {subordinate_roles}")

    subordinate_user_ids = set()

    # Lookup the role membership db
    for role in subordinate_roles:
        subordinate_user_ids.update(db['role_membership'][role.id])

    # Lookup the actual users
    subordinate_users = [db['users'][user_id] for user_id in subordinate_user_ids]


    return subordinate_users

