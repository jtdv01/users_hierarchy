import json
from argparse import ArgumentParser
from user import User
from role import Role

def arg_parser():
    parser = ArgumentParser()
    parser.add_argument("--input_file", required=True)
    args = parser.parse_args()
    return args

def json_parser(file_loc: str):
    """
    :param file_loc: The file location of the input file
    :type file_loc: str

    :return: Returns two dictionaries (roles and users)
    :rtype: tuple
    """
    with open(file_loc, 'r') as f:
        obj = json.load(f)
        return (obj['roles'], obj['users'])

def parse_roles_and_users(file_loc: str):
    """
    Parse the input json to Roles and Users
    """

    roles_input, users_input = json_parser(file_loc)

    # Parse as objects
    roles = {r["Id"]:Role(r["Id"], r["Name"], r["Parent"]) for r in roles_input}
    users = {u["Id"]:User(u["Id"], u["Name"], u["Role"]) for u in users_input}

    # Attach parents to roles
    for k, current_role in roles.items():
        parent_role_id = current_role.parent_id

        # Try to fetch the parent role
        try:
            parent_role = roles[parent_role_id]
            # Add child roles
            parent_role.add_child_role(current_role)
            
            # Add parent role. This is redundant with a simpler child role reference
            # current_role.set_parent_role(parent_role)

        except KeyError as e:
            # If parent can't be found, it must be a root role
            current_role.set_as_root_role()

    # Set roles to users
    for k, current_user in users.items():
        role_id = current_user.role_id
        try:
            current_user.set_role(roles[role_id])
        except:
            # TODO: Unable to set a role
            pass

    return(roles, users)
