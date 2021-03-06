import unittest
import pyperclip
from Password import User
from Password import Credential

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


class TestCredential(unittest.TestCase):
    '''
    a class that defines test cases for the credential behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.new_credentials = Credential("twitter", "mykeck", "key33")

    def tearDown(self):
        Credential.credentials_list = []

    def test_init2(self):
        self.assertEqual(self.new_credentials.account_name, "twitter")
        self.assertEqual(self.new_credentials.user_name, "mykeck")
        self.assertEqual(self.new_credentials.password, "key33")

    def test_save_credentials(self): 
        self.new_credentials.save_credentials()

        self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_account(self): 
        self.new_credentials.save_credentials() 

        credential1 = Credential("facebook", "swat", "j876")
        credential1.save_credentials()

        self.assertEqual(len(Credential.credentials_list),2)

    def test_find_account_name(self): 
        self.new_credentials.save_credentials()

        credential2 = Credential("Instagram", "badman", "#2020")
        credential2.save_credentials()

        found_credentials = Credential.find_account_name("Instagram")

        self.assertEqual(found_credentials.password, credential2.password)

    def test_view_credentials(self):
    
        self.assertEqual(Credential.view_credentials(), Credential.credentials_list)

    def test_delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credential("Instagram", "badman","#2020")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credential.credentials_list), 1)
    
            
         
if __name__ == '__main__':
    unittest.main()             