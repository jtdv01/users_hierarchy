#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
import pdb

def main():
    args = arg_parser()
    roles, users = parse_roles_and_users(args.input_file)

    db = {}

    for r in roles:
        parent = r.parent
        # Initialise a new key
        if parent not in db.keys():
            db[parent] = []

    print(db)

if __name__ == '__main__':
    main()
