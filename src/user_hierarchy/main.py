#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
import sys
from db import init_db
import logging
from datetime import datetime
from subordinate_search import find_subordinate_users

def setup_logger():
    FORMAT = "%(asctime)-15s %(levelname)s-%(message)s"
    today = datetime.now().strftime("%Y-%m-%d")
    logfile = f"logs/{today}.log"
    logging.basicConfig(format=FORMAT, filename=logfile, filemode='w+', level=logging.INFO)

def print_welcome():
    print("\nWelcome to UserHierarchyDB! Author: JTY 2019\n")
    print("Type in the user id of interest.")
    print("Information about subordinate users will then be printed out.")
    print("To see the current state of the database type in `db`. WARNING! This can be large!")
    print("\n\nTo quit type in `quit`.")
    print("\n\nTo see this information again, type in `help`.\n\n")

def main():
    setup_logger()
    args = arg_parser()
    roles, users = parse_roles_and_users(args.roles_filepath, args.users_filepath)
    db = init_db(roles, users)

    logging.info(db)

    # Start a REPL for finding out the subordinate users of a given user id
    wait_for_user_input = True
    print_welcome()
    while wait_for_user_input:
        user_input = input("Type in User ID to query > ")

        if user_input == "quit":
            wait_for_user_input = False
            print("Bye!")
            sys.exit(0)

        if user_input == "help":
            print_welcome()
            continue

        if user_input == "db":
            # Print the current database. This can be large!
            print(db)
            continue

        try:
            query_user_id = int(user_input)
            user = db['users'][query_user_id]
            logging.info(f"User {user.id} has a Role ID {user.role.id}. Searching for subordinate users..")
            # Find out the subordinate users for the queried user
            subordinate_users = find_subordinate_users(db, query_user_id)
            logging.info(subordinate_users)
            print(f"Found {len(subordinate_users)} users under UserID: {user.id} UserName: {user.name}")
            for u in subordinate_users:
                print(u)
                logging.info(u)
        except ValueError as e:
            print("Invalid user input")
        except KeyError as e:
            print("User ID not found")


if __name__ == '__main__':
    main()
