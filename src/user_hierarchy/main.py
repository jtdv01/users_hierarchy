#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
import pdb

def main():
    args = arg_parser()
    roles, users = parse_roles_and_users(args.input_file)

    db = {}

    for r in roles:
        id = r.id
        # Initialise a new key
        if id not in db.keys():
            db[id]={
                'users': [],
                'children_roles': []
            }

    for r in roles:
        parent = r.parent
        try:
            db[parent]['children_roles'].append(r.id)
        except KeyError as e:
            pass

    print(db)

if __name__ == '__main__':
    main()
