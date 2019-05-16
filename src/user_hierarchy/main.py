#! /usr/bin/python3
from parser import json_parser, arg_parser

def main():
    args = arg_parser()
    json_parser(args.input_file)

if __name__ == '__main__':
    main()
