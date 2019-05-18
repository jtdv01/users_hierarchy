#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
from user import set_users
from role import set_roles


def init_db():
    db = {}
    return db

def main():
    args = arg_parser()
    roles, users = parse_roles_and_users(args.input_file)

    db = init_db()
    db = set_roles(db, roles)
    db = set_users(db, users)

    wait_for_user_input = True
    while wait_for_user_input:
        user_input = input("Type in User ID to query >")
        try:
            query_user_id = int(user_input)
            user = db['users'][query_user_id]
            print(f"User {user.id} has a Role ID {user.role.id}")
        except ValueError as e:
            print("Invalid user input")
        except KeyError as e:
            print("User ID not found")

        if user_input == "quit":
            wait_for_user_input = False
            print("Bye!")

if __name__ == '__main__':
    main()
