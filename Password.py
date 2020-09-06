class User:
    user_list = []
    
    def __init__ (self, user_name, password):
        self.user_name = user_name
        self.password = password

    def create_account(self):
        User.user_list.append(self)

    @classmethod
    def user_exists(cls, user_name, password):
        '''
        method that checks if a user exists from the users list
        Args:
            user_name: to search if the user name exists
            password: to search if the password exists
        Returns: 
            boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name and user.password == password:
                return True 

        return False 

class credentials:
    credentials_list = []

    def __init__ (self, account_name, user_name, password):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        credentials.credentials_list.append(self)

    @classmethod
    def find_account_name(cls, account_name):
        '''
        method that takes in an account name and returns a credential that matches the account name

        Args:
            account_name: account name to search for
        Returns :
            credentials that matches the account_name
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials 

    @classmethod
    def view_credentials(cls):
        '''
        method that returns the credentials lists
        '''
        return cls.credentials_list

    def delete_credentials(self):
        credentials.credentials_list.remove(self)                                      


     