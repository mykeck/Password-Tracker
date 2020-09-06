import unittest
from Password import User
from Password import credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Mike", "12345")

    def tearDown(self):
        User.user_list = []   

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Mike")
        self.assertEqual(self.new_user.password,  "12345")


    def test_create_account(self):
        self.new_user.create_account()  

        self.assertEqual(len(User.user_list), 1)  
        
    def test_save_multiple_account(self):
        self.new_user.create_account() 

        user1 = User('kimkim', '6rtef')
        user1.create_account()

        self.assertEqual(len(User.user_list), 2)

    def test_account_exist(self):
        self.new_user.create_account()

        user2 = User('sally', '*999')
        user2.create_account()  

        user_exists = User.user_exists('sally', '*999')

        self.assertTrue(user_exists) 


class Testcredentials(unittest.TestCase):
    '''
    a class that defines test cases for the credential behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.new_credentials = credentials("twitter", "mykeck", "key33")

    def tearDown(self):
        credentials.credentials_list = []

    # def test_init(self):
    #     self.assertSetEqual(self.new_credentials.account_name,"twitter")
    #     self.assertSetEqual(self.new_credentials.user_name, "mykeck")
    #     self.assertSetEqual(self.new_credentials.password, "key33")

    def test_save_credentials(self): 
        self.new_credentials.save_credentials()

        self.assertEqual(len(credentials.credentials_list), 1)

    def test_save_multiple_account(self): 
        self.new_credentials.save_credentials() 

        credential1 = credentials("facebook", "swat", "j876")
        credential1.save_credentials()

        self.assertEqual(len(credentials.credentials_list),2)
         

         

                

        
        

if __name__ == '__main__':
    unittest.main()             