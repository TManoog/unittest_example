import unittest
import requests
import json
from get_data import GetTestData


class Tests(unittest.TestCase, GetTestData):
    @classmethod
    def setUpClass(cls):
        print('\nA class method called before tests in an individual class are run')
    @classmethod
    def tearDownClass(cls):
        print('\nA class method called after tests in an individual class have run')

    def setUp(self):
        print('\nThis is called immediately before calling the test method')

    def tearDown(self):
        print('\nMethod called immediately after the test method has been called and the result recorded. ')

    def test_get_user_list(self):
        test_data = json.load(open('data/user_list.json', 'r'))
        user_list = self.get_user_list()
        assert test_data == user_list

    def test_get_user_with_wrong_id(self):
        test_data = 'User Not Found. Status Code: 404'
        user_data = self.get_single_user_with(user_id=23)
        assert test_data == user_data

    def test_get_second_user_date(self):
        test_data = json.load(open('data/single_user_id_2_data.json', 'r'))
        user_data = self.get_single_user_with(user_id=2)
        assert test_data == user_data

    @unittest.skip("demonstrating skipping")
    def test_skip_example(self):
        a = 1
        b = 2
        assert a == b