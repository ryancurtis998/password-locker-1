from random import randint


class Credential:
    """
    Class which we will use to create the passwords
    """
    passwords = []  # store all the user's passwords

    def __init__(self, media, username, password):
        """
        Function allow new instances of the class with unique authentication;
        """
        self.media = media
        self.username = username
        self.password = password

    def save_password(self):
        """
        Function will add the password into the passwords array
        """
        Credential.passwords.append(self)
        
    def generate_password(self, length):
        """
        Function will generate a random password for the user
        """
        items = ["a", "e", "i", "o", "u", "1", "2", "4", "5", "7", "8", "9"]

        new_password = ""
        while(len(new_password) < length):
            item = items[randint(0, len(items) - 1)]
            new_password += item
        return new_password

    @classmethod
    def display_passwords(cls):
        """
        This function will return all the passwords in the array
        """
        return cls.passwords
     
    @classmethod
    def delete_password(cls, media):
        """
        Function to delete user's password from the passwords array
        """
        for password in cls.passwords:
            if password.media.lower() == media.lower():
                cls.passwords.remove(password)
    