import unittest
from credential import Credential


class TestPass(unittest.TestCase):
    """
    Class to perform credential tests
    """
    def setUp(self):
        """
        This function will create a new instance of Password before each test
        """
        self. new_password = Credential("instagram", "buyu_kah", "0505")
    
    def tearDown(self):
        """
        deletes passwords list after test to avoid interfering with the tests
        """
        Credential.passwords = []

    def test_new_password(self):
        """
        Test whether a new password is instantiated correctly
        """
        self.assertEqual(self.new_password.media, "instagram")
        self.assertEqual(self.new_password.username, "buyu_kah")
        self.assertEqual(self.new_password.password, "0505")

    def test_save_new_password(self): 
        """
        Check whether the new password is added to the passwords array
        """
        self.new_password.save_password()
        self.assertEqual(len(Credential.passwords), 1)

    def test_show_password(self):
        """
        check whether the display_passwords function will return the passwords in the passwords list
        """
        self.new_password.save_password()
        new_password = Credential("instagram", "mck", Credential.show_password(9))
        new_password.save_password()
        self.assertEqual(len(Credential.passwords), len(Credential.show_passwords()))



if __name__ == "__main__":
    unittest.main()