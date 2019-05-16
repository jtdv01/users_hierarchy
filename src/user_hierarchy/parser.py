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

    roles_input, users_input = json_parser(file_loc)

    # Parse as objects
    roles = [Role(r["Id"], r["Name"], r["Parent"]) for r in roles_input]
    users = [User(u["Id"], u["Name"], u["Role"]) for u in users_input]

    return(roles, users)
