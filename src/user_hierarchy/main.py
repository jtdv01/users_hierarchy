#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
from db import init_db
import logging
from datetime import datetime
from subordinate_search import subordinate_search

def setup_logger():
    FORMAT = "%(asctime)-15s %(levelname)s-%(message)s"
    today = datetime.now().strftime("%Y-%m-%d")
    logfile = f"logs/{today}.log"
    logging.basicConfig(format=FORMAT, filename=logfile, filemode='w+', level=logging.INFO)

def main():
    setup_logger()
    args = arg_parser()
    roles, users = parse_roles_and_users(args.roles_filepath, args.users_filepath)
    db = init_db(roles, users)

    logging.info(db)

    wait_for_user_input = True
    while wait_for_user_input:
        user_input = input("Type in User ID to query >")
        try:
            query_user_id = int(user_input)
            user = db['users'][query_user_id]
            logging.info(f"User {user.id} has a Role ID {user.role.id}. Searching for subordinate users..")
            subordinate_users = subordinate_search(db, user)
            print(subordinate_users)
        except ValueError as e:
            print("Invalid user input")
        except KeyError as e:
            print("User ID not found")

        if user_input == "quit":
            wait_for_user_input = False
            print("Bye!")

if __name__ == '__main__':
    main()
