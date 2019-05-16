#! /usr/bin/python3
from parser import arg_parser, parse_roles_and_users
from user import User
from role import Role

def main():
    args = arg_parser()
    roles, users = parse_roles_and_users(args.input_file)




if __name__ == '__main__':
    main()
