from user import User
from role import Role
import logging

def find_subordinate_roles(role: Role, found_so_far = set()):
    """
    Recursive do a depth first search of subordinate roles

    :return: subordinate_roles -- A list of role id's under this current role
    :rtype: set
    """

    # Base case
    if len(role.children_roles) == 0:
        return set()

    subordinate_roles = found_so_far
    for child_role in role.children_roles:
        # Add direct descendants
        subordinate_roles.add(child_role)

        # Add child's desencdants recursively
        childs_subordinates = find_subordinate_roles(child_role, subordinate_roles)
        subordinate_roles = subordinate_roles.union(childs_subordinates)

    return subordinate_roles

def subordinate_search(db: dict, query_user_id: int):
    """
    Returns a set of user ids that are under a given user_id

    :param user_id: The user id that we want to query
    :type user_id: int

    :return subordinate_users: A set of Users who are under a given user
    :rtype: set
    """

    # Find out the role of the user
    role_id = db['users'][query_user_id].role_id

    # Find out the subordinate roles of this user
    subordinate_roles = find_subordinate_roles(db['roles'][role_id])
    logging.info(f"The subordinate roles under this user is {subordinate_roles}")

    subordinate_user_ids = set()

    # Lookup the role membership db
    for role in subordinate_roles:
        subordinate_user_ids.update(db['role_membership'][role.id])

    # Lookup the actual users, but do not count itself
    subordinate_users = [db['users'][user_id] for user_id in subordinate_user_ids if user_id != query_user_id]

    return subordinate_users

