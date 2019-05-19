import unittest
from parser import parse_roles_and_users
from db import init_db
#from subordinate_search import subordinate_search

class TestUserHierarchy(unittest.TestCase):

    def setUp(self):
        roles_filepath = "resources/roles.json"
        users_filepath = "resources/users.json"
        self.roles, self.users = parse_roles_and_users(roles_filepath, users_filepath)
        self.db = init_db(self.roles, self.users)

    def test_who_is_root(self):
        # Assert that the RoleID 1 is the root role
        self.assertTrue(self.db['roles'][1].is_root_role)

        # Assert that only Adam Admin has the root role
        for uid, user in self.db['users'].items():
            if uid == 1:
                self.assertTrue(user.role_id == 1)
                self.assertTrue(user.name == "Adam Admin")
            else:
                self.assertTrue(user.role_id != 1)

        print("Test that only Adam Admin has the only role role: OK")

    def test_find_subordinate_roles(self):
        root_role = self.db['roles'][1]

        x = root_role.find_subordinate_roles(set())
        print(x)




if __name__ == '__main__':
    unittest.main()
