class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return in_group (True) if user is in the group, False otherwise
    Input: 
        user -> user name(str)     
        group ->  group to verify user group(class)
    Output:
        in_group (True) -> If the user is in the group
    """

    if user == None:
        return 'User arg cannot be None'

    if group == None:
        return "Group arg cannot be None"

    if type(group) != Group:
        return "Group arg must be Group type"

    if user == "":
        return "False"

    if not group or not user is not Group:
        print("Not a valid argument")
        return False

    if user in group.get_users() or user == group.get_name():
        return True
    in_group = False
    for i in group.get_groups():
        in_group = in_group or is_user_in_group(user, i)
        if in_group:
            return True
    return in_group


# Test cases 1
if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    sub_child_user2 = "sub_child_user_2"
    sub_child_2 = Group("subchild2")
    sub_child_2.add_user(sub_child_user2)
    parent.add_group(sub_child_2)

    print(is_user_in_group(sub_child_user, sub_child))  # True
    print(is_user_in_group(sub_child_user, child))  # True
    print(is_user_in_group(sub_child_user, parent))  # True
    print(is_user_in_group("child", child))  # True
    print(is_user_in_group("", child))  # False
    print(is_user_in_group("sub_child_user", parent))  # True

    # Test Case 2
    print(is_user_in_group(sub_child_user, parent))  # True
    print(is_user_in_group(sub_child_user2, parent))  # True
    print(is_user_in_group(None, parent))  # User arg cannot be None
    print(is_user_in_group(sub_child_user2, None))  # Group arg cannot be None
    # Group arg must be Group type

    # Test Case 3
    print(is_user_in_group(sub_child_user2, "None"))
    # Group arg must be Group type
    print(is_user_in_group("", parent))  # Invalid user
