from datetime import datetime


class BaseRecord:
    def __init__(self, created_at: datetime, updated_at: datetime, id: int):
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = id


class Bin(BaseRecord):
    """ Represents a storage bin
    Attrs:
        bin_id(int): shows the id of the bin
        location(str): shows the bin's location
        part_id(str): shows id of a single Part object
        qty_in_bin(int): shows how many of said Part is in the bin
    """
    def __init__(self, id: int, location: str, part_id: str, qty_in_bin: int, created_at, updated_at):
        "Initializes description of the bin"
        super().__init__(created_at, updated_at, id)
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
    def __init__(self, id: int, name: str, quantity: int, bin_id: int, created_at, updated_at):
        "Initializes description of the part"
        super().__init__(created_at, updated_at, id)
        self.name = name
        self.quantity = quantity
        self.bin_id = bin_id


class User(BaseRecord):
    """ Represents a User's info
    Attrs:
        email(str): shows the student's email
        student_num(int): shows the student's number
    """
    def __init__(self, email: str, student_num: int, created_at, updated_at, id):
        "Initializes description of the student's information"
        super().__init__(created_at, updated_at, id)
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
    def __init__(self, user_id: int, part_id: int, quantity: int, created_at, updated_at, id):
        "Initializes description of the log data"
        super().__init__(created_at, updated_at, id)
        self.user_id = user_id
        self.part_id = part_id
        self.quantity = quantity


class InventoryManager(BaseRecord):
    """ Represents an inventory
    parts(List): Shows a list of all parts
    bins(List): Shows a list of all bins
    logs(List): Shows a list of all the logs
    users(List): Shows a list of all users
    """
    def __init__(self, created_at, updated_at, id):
        "Initializes description of the inventory data"
        super().__init__(created_at, updated_at, id)
        self.parts = []
        self.bins = []
        self.logs = []
        self.users = []
