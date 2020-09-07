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

    print("Sign up  to account")
    print("Enter username")
    User_name = input()
    print("Enter your password:")
    password = input()
    save_account(create_account(user_name, password))
    print("\n")
    print(f"{user_name} account created successfuly")
    print("\n")
    print("Enter username and password to log in")

    print("Enter username")
    User_name = input()
    print("Enter your password:")
    password = input()

    if login(user_name, Password):
        print("You have logged in successfuly")
        login_detail = login(user_name, Password)
    else:
        while login(user_name, Password) == False:
            print("Enter correct username or password")
            print("Enter username")
            User_name = input()
            print("Enter your password:")
            password = input()
            login_detail = login(user_name, Password)

    while login_detail == True:
        print("Use these short codes : sc - save  already existing credentials, cc - create a new credential, vc - view your credentials, fc - find a credential, lo - logout")
        code = input()

        if code == "cc":
            print("Enter the name of the account credential")
            account_name = input()
            print("Enter the account credential username")
            user_name = input()
            print("password:")
            print("Would you like to generate your password? y/n")
            password = input()
            if password == "y":
                print("Enter preffered password length")
                pass_len=int(input())
                password=generate_password(pass_len)
                print(f"your new password for {account_name} is {password}")
            elif password == "n":
                print("Create your own password:")
                password=input()
            else:
                print("Invalid choice!")

        save_credentials(create_credentials(account_name, user_name, password))
        print(f"Account credentials for {account_name} has been saved")
        print("\n")

        elif code == "vc":
            if view_credentials():
                print("Here is a list of all your credentials")
                print("\n")
                for credentials in view_credentials():
                    print(f"Account Name .....{credentials.account_name}")
                    print(f"User Name .....{credentials.user_name}")
                    print(f"Password .....{credentials.password}")
                    print("\n")
            else:
                print("\n")
                print("you dont seem to have any credentials saved yet")
                print("\n")

        elif code == "fc":
            print("Enter the account credentials name you want to search for")
            name=input()
            found_credentials=find_credentials(name)
            if found_credentials:
                print(f"your username for your {found_credentials.account_name} account is {found_credentials.user_name} and the password is {found_credentials.password}")
                print("\n")
            else:
                print("credentials does not exist")

        elif code == "lo":
            print("logging out..")

            


            # break
        else:
            print("Use correct short codes")


if __name__ == "__main__":
    main()
