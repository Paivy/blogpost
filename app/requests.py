import unittest
from app.models import User
import requests,json

# class UserModelTest(unittest.TestCase):

    # def setUp(self):
    #     self.new_user = User(password = '123')

    # def test_password_setter(self):
    #     self.assertTrue(self.new_user.pass_secure is not None)
    # def test_no_access_password(self):
    #         with self.assertRaises(AttributeError):
    #             self.new_user.password

    # def test_password_verification(self):
    #     self.assertTrue(self.new_user.verify_password('123'))

def get_quotes():
        response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
        if response.status_code == 200:
            quote = response.json()
            return quote