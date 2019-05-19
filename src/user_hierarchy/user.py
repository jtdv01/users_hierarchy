from role import Role

class User():

    def __init__(self, id: int, name: str, role_id: int):
        self.id = id
        self.name = name
        self.role_id = role_id
        self.role = None

    def set_role(self, role: Role):
        self.role = role

    def __repr__(self):
        return f"{{'user_id': {self.id}, 'user_name': '{self.name}', 'user_role': {self.role}}}"
