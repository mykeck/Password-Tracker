#!/usr/bin/env python3.6
from Password import User
import secrets
import string


def create_account(user_name, Password):
    '''
    function to create a new user account
    '''

    new_user = User(user_name, Password)
    return new_user

def save_account(user):
    '''
    a function to save user account
    '''
    User.create_account(user)

def login(user_name, Password):
    '''
    checks if a user exists with that number and returns a Boolean
    '''
    return User.user_exists(user_name, password)  

def create_credentials(account_name, user_name, password):
    '''
    a function to create new credentials
    '''
    new_credentials = Credential(account_name, user_name, password) 
    return new_credentials

def save_credentials(credentials):
    '''
    function to save credentials
    '''
    return Credential.save_credentials(credentials)

def find_credentials(account_name):
    return Credential.find_by_account_name(account_name)

def view_credentials():
    return Credential.view_credentials()

def delete_credentials():
    return Credential.delete_credential()

def generate_password(pass_len):

    return "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(pass_len))  


def main(): 
    print("Hello! Welcome to password Checker")
    logged_in = False

    
    while True:
        print("Do you want to sign up or login")
        print("Click 's' to sign up or 'l' to login")
        answer = input()
        if answer == "l":
            print("Enter your password:")
            password = input()

            logged_in = login(user_name, password) if answer == 'l' else False

            while logged_in:
                print("Use these short codes : sc - save  already existing credentials, cc - create a new credential, vc - view your credentials, fc - find a credential, lo - logout")
                code =  input()

                if code == "sc":
                    print("Create new credentials")

                    print("Enter the name of the account credential")
                    account_name = input()

                    print("Enter the account credential username")
                    user_name = input()

                    print("Enter the password of the account")
                    password = input()

                    save_credentials(create_credentials(account_name, user_name, password))

                    print(f"Account credentials fo {account_name} has been saved")
                    print("/n")

                elif code == "cc":
                    print("Enter the name of the account credential")
                    account_name = input() 

                    print("Enter the account credential username")
                    user_name = input() 

                    print("password:") 
                    print("Would you like to generate your password? y/n") 
                    password = input()

                    if password == "y":
                        print("Enter preffered password length")
                        pass_len = int(input())
                        password = generate_password(pass_len)
                        print(f"your new password for {account_name} is {password}")

                      


if __name__ == "__main__":
    main()    