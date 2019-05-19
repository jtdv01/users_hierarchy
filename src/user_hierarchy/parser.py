import json
from argparse import ArgumentParser
from user import User
from role import Role
import logging

def arg_parser():
    parser = ArgumentParser()
    parser.add_argument("--roles_filepath", required=True, help="Filepath of the roles.json input")
    parser.add_argument("--users_filepath", required=True, help="Filepath of the users.json input")
    args = parser.parse_args()
    return args

def json_parser(file_loc: str, key: str):
    """
    :param file_loc: The file location of the input file
    :type file_loc: str

    :return: A dictionary of roles or users
    """
    with open(file_loc, 'r') as f:
        obj = json.load(f)
        return (obj[key])

def parse_roles_and_users(roles_filepath: str, users_filepath: str):
    """
    Parse the input json to Roles and Users

    :param roles_filepath: The file location of the input roles file
    :type roles_filepath: str
    :param users_filepath: The file location of the input users file
    :type users_filepath: str

    :return: A tuple of dictionaries (roles and users)
    """

    roles_input = json_parser(roles_filepath, 'roles')
    users_input = json_parser(users_filepath, 'users')

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
            logging.info(f"RoleID {current_role.id} is the root role")
            current_role.set_as_root_role()

    # Set roles to users
    for k, current_user in users.items():
        role_id = current_user.role_id
        try:
            current_user.set_role(roles[role_id])
        except:
            logging.warning(f"Unable to set role {role_id} to {current_user}")

    return(roles, users)

