class Role():

    def __init__(self, id: int, name: str, parent_id: int):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.children_roles = []

        self.is_root_role = False

    def set_as_root_role(self):
        """
        If no parent is found on the database, set this as a root role
        """
        self.is_root_role = True

    def add_child_role(self, child_role: 'Role'):
        """
        Add a single role as a child role
        """
        self.children_roles.append(child_role)


def set_roles(db, roles):
    db['roles'] = roles
    return db