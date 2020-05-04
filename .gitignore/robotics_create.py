import datetime
from typing import List


class BaseRecord:
    def __init__(self, id: int):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = id


class Bin(BaseRecord):
    """ Represents a storage bin
    Attrs:
        bin_id(int): shows the id of the bin
        location(str): shows the bin's location
        part_id(str): shows id of a single Part object
        qty_in_bin(int): shows how many of said Part is in the bin
    """
    def __init__(self, id: int, location: str, part_id: str, qty_in_bin: int):
        "Initializes description of the bin"
        super().__init__(id)
        self.location = location
        self.part_id = part_id
        self.qty_in_bin = qty_in_bin


class Part(BaseRecord):
    """ Represents a part
    Attrs:
        part_id(int): shows the id of the part
        name(str): shows the part's name
        quantity(int): show how much of that part is in the bin
        bin_id(int): show the id of a single Bin object
    """
    def __init__(self, name: str, quantity: int, bin_id: int, id: int):
        "Initializes description of the part"
        super().__init__(id)
        self.name = name
        self.quantity = quantity
        self.bin_id = bin_id


class User(BaseRecord):
    """ Represents a User's info
    Attrs:
        email(str): shows the student's email
        student_num(int): shows the student's number
    """
    def __init__(self, email: str, student_num: int, id: int):
        "Initializes description of the student's information"
        super().__init__(id)
        self.email = email
        self.student_num = student_num


class Log(BaseRecord):
    """ Represents a user login
    Attrs:
        time(datetime): shows the time of login
        user_id(int): shows the user's id
        part_id(int): show's the id of the part being logged out
        quantity(int): shows how much of a part was logged out
    """
    def __init__(self, user_id: int, part_id: int, quantity: int, id: int):
        "Initializes description of the log data"
        super().__init__(id)
        self.user_id = user_id
        self.part_id = part_id
        self.quantity = quantity


class InventoryManager:
    """ Represents an inventory
    parts(List): Shows a list of all parts
    bins(List): Shows a list of all bins
    logs(List): Shows a list of all the logs
    users(List): Shows a list of all users
    """
    def __init__(self):
        "Initializes description of the inventory data"
        self.parts: List[Part] = []
        self.bins: List[Bin] = []
        self.logs: List[Log] = []
        self.users: List[User] = []

    def create_user(self, email: str, student_num: int) -> User:
        user = User(email, student_num, 0)
        self.users.append(user)
        return user

    def find_user_by_student_num(self, student_num: int) -> User:
        for user in self.users:
            if user.student_num == student_num:
                return user

    def find_bin_by_location(self, location: str) -> Bin:
        for bin in self.bins:
            if bin.location == location:
                return bin

    def add_part(self, name: str, quantity: int, bin_id: int) -> Part:
        part = Part(name, quantity, bin_id, 1)
        self.parts.append(part)
        return part
