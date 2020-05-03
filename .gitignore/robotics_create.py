from datetime import datetime


class Bin:
    """ Represents a storage bin
    Attrs:
        bin_id(int): shows the id of the bin
        location(str): shows the bin's location
        part_id(str): shows id of a single Part object
        qty_in_bin(int): shows how many of said Part is in the bin
    """
    def __init__(self, bin_id: int, location: str, part_id: str, qty_in_bin: int):
        "Initializes description of the bin"
        self.id = bin_id
        self.location = location
        self.part_id = part_id
        self.qty_in_bin = qty_in_bin


class Part:
    """ Represents a part
    Attrs:
        part_id(int): shows the id of the part
        name(str): shows the part's name
        quantity(int): show how much of that part is in the bin
        bin_id(int): show the id of a single Bin object
    """
    def __init__(self, part_id: int, name: str, quantity: int, bin_id: int):
        "Initializes description of the part"
        self.id = part_id
        self.name = name
        self.quantity = quantity
        self.bin_id = bin_id


class User:
    """ Represents a User's info
    Attrs:
        email(str): shows the student's email
        student_num(int): shows the student's number
    """
    def __init__(self, email: str, student_num: int):
        "Initializes description of the student's information"
        self.email = email
        self.student_num = student_num


class Log:
    """ Represents a user login
    Attrs:
        time(datetime): shows the time of login
        user_id(int): shows the user's id
        part_id(int): show's the id of the part being logged out
        quantity(int): shows how much of a part was logged out
    """
    def __init__(self, time: datetime, user_id: int, part_id: int, quantity: int):
        "Initializes description of the log data"
        self.time = time
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
        self.parts = []
        self.bins = []
        self.logs = []
        self.users = []
