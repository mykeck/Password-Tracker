#!/usr/bin/env python3.6
from Password import User


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

    
                      


if __name__ == "__main__":
    main()    