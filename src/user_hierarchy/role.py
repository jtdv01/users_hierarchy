class Role():

    def __init__(self, id: int, name: str, parent: int):
        self.id = id
        self.name = name
        self.parent = parent
        self.children_roles = []

    def add_child_role(self, child_role: 'Role'):
        self.children_roles.append(child_role)

