import json
from argparse import ArgumentParser

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
