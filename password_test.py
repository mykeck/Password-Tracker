import unittest
from Password import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Mike", "Collins")

    def tearDown(self):
        User.user_list = []   

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Mike")
        self.assertEqual(self.new_user.password, "Collins")

if __name__ == '__main__':
    unittest.main()             