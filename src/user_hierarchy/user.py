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
        return f"<Id: {self.id}|Name: {self.name}|Role: {self.role}>"
