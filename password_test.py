import unittest
from Password import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Mike", "Collins")

    def tearDown(self):
        User.user_list = []   

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Mike")
        self.assertEqual(self.new_user.password, "#12345")

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

        
        # self.new_user_credential = User("denischom"") 

if __name__ == '__main__':
    unittest.main()             