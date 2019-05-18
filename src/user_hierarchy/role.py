class Role():

    def __init__(self, id: int, name: str, parent_id: int):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.children_roles = []

        self.is_root_role = False

    def set_parent_role(self, parent_role: 'Role'):
        self.parent_role = parent_role

    def set_as_root_role(self):
        self.is_root_role = True

    def add_child_role(self, child_role: 'Role'):
        self.children_roles.append(child_role)

