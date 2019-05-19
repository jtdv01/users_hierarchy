#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
import sys
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

    # Start a REPL for querying subordinate users given a user id
    wait_for_user_input = True
    while wait_for_user_input:
        user_input = input("Type in User ID to query >")

        if user_input == "quit":
            wait_for_user_input = False
            print("Bye!")
            sys.exit(0)

        try:

            query_user_id = int(user_input)
            user = db['users'][query_user_id]
            logging.info(f"User {user.id} has a Role ID {user.role.id}. Searching for subordinate users..")
            # Find out the subordinate users for the queried user
            subordinate_users = subordinate_search(db, query_user_id)
            logging.info(subordinate_users)
            print(f"Found {len(subordinate_users)} users under UserID: {user.id} UserName: {user.name}")
            for u in subordinate_users:
                print(u)

        except ValueError as e:
            print("Invalid user input")
        except KeyError as e:
            print("User ID not found")


if __name__ == '__main__':
    main()
