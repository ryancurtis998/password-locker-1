from random import randint


class User:
    """
    class that will contain all the details of the user
    """

    password = []  # will store all passwords

    def __init__(self, login, password):
        """
        This will create unique details for each instance of the User class
        """
        self.login = login
        self.password = password

