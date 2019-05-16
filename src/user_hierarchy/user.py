from role import Role

class User():

    def __init__(self, id: int, name: str, role: Role):
        self.id = id
        self.name = name
        self.role = role
