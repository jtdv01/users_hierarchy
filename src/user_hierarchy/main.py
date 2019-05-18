#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
import pdb


def init_roles(roles):
    """
    :return: db -- A key value database of roles
    """
    db = {
        'roles': {},
        'users': {}
    }

    # Add roles to the database
    # Add as a hash map for a fast lookup
    for r in roles:
        role_id = r.id
        # Initialise a new role if not defined
        if id not in db['roles'].keys():
            db['roles'][role_id] = r

    # Add children nodes to their parents
    for r in roles:
        pdb.set_trace()
        parent_role_id = r.parent.id
        try:
            parent_role = db['roles'][parent_role_id]
            parent_role.add_child_role(r)
        except KeyError as e:
            # Parent wasn't found on the database
            # This must be a root role
            pass

    pdb.set_trace()

    return db

def main():
    args = arg_parser()
    roles, users = parse_roles_and_users(args.input_file)

    db = init_roles(roles)
    print(db)

if __name__ == '__main__':
    main()
