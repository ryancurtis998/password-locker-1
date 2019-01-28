class User:
    """
    class that will contain all the details of the user
    """

    def __init__(self, login, password):
        """
        This will create unique details for each instance of the User class
        """
        self.login = login
        self.password = password

    def user_exists(self, password):
        """
        Use the password to confirm user before reviewing the passwords;
        """
        if self.password == password:
            return True
        return False
