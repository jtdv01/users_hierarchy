import unittest
from parser import parse_roles_and_users
from db import init_db

class TestUserHierarchy(unittest.TestCase):

    def setUp(self):
        roles_filepath = "resources/roles.json"
        users_filepath = "resources/users.json"
        self.roles, self.users = parse_roles_and_users(roles_filepath, users_filepath)
        db = init_db(self.roles, self.users)

    def test_isupper(self):
        self.assertTrue(1 == 1)


if __name__ == '__main__':
    unittest.main()
