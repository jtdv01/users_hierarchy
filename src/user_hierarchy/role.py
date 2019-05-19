class Role():

    def __init__(self, id: int, name: str, parent_id: int):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.children_roles = []

        self.is_root_role = False

    def __repr__(self):
        return f"{{'role_id': {self.id}, 'role_name': '{self.name}'}}"

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

    def find_subordinate_roles(self, found_so_far = set()):
        """
        Recursive do a depth first search of subordinate roles

        :return: subordinate_roles -- A list of role id's under this current role
        :rtype: set
        """

        # Base case
        if len(self.children_roles) == 0:
            return set()

        subordinate_roles = found_so_far
        for r in self.children_roles:
            # Add direct descendants
            subordinate_roles.add(r)

            # Add child's desencdants recursively
            childs_subordinates = r.find_subordinate_roles(subordinate_roles)

            if childs_subordinates != set():
                subordinate_roles = subordinate_roles.union(childs_subordinates)

        return subordinate_roles
