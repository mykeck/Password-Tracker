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
        for user_name in cls.user_list:
            if user_name == user_name and password == password:
                return True 
                          
