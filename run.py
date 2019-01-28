#!/usr/bin/env python3.6
from user import User
from credential import Credential


def new_user(login, password):
    """
    create a new user everytime they login
    """
    return User(login, password)


def add_password(media, username, password):
    """
    Function to add a new password to the passwords array
    """
    new_password = Credential(media, username, password)
    new_password.save_password()


def generate_password(length):
    """
    Generates a random password for the user
    """
    return Credential.generate_password(length) 


def view_passwords():
    """
    Function to view all the passwords
    """
    return Credential.display_passwords()


def delete_password(acc):
    """
    This is a function that will delete the password
    """
    Credential.delete_password()


def main():
    '''
    where all functions are executed
    '''

    print(' ____________________________')
    print('< welcome to password-locker >')
    print('----------------------------')
    print('  \ ')
    print('   \       ___ ')
    print('      oo  // \\ ')
    print('     (_,\/ \_/ \ ')
    print('       \ \_/_\_/> ')
    print('       /_/   \_\ ')
    print('')
    print('      /')
    print('     /')
    print(' ____________________________')
    print('< will help you manage and create passwords >')
    print('----------------------------')

    print('____signup___')

    Name = input("User Name\n")
    password = input('Password:\n')

    print(f"Welcome {Name}\n")

    while True:
         print("Use these codes : create - creates a new password, generate - generates a new password, display - display passwords, exit -exit the password-locker ") 

         code = input().lower()

         if code == 'create':
             print ("Media name ....")
             Media = input()

             print ("User name ....")
             username = input()

             print ("password ....")
             password = input()

             print(f"New password for {Media} added!\n")





 


if __name__ == "__main__":
    main()




    

