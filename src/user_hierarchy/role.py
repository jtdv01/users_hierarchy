class Role():

    def __init__(self, id: int, name: str, parent: 'Role'):
        self.id = id
        self.name = name
        self.parent = parent
