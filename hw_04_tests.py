import unittest
from pathlib import Path

from func.functions import read_file, total_salary, get_cats_info
from hw_04_3 import list_dir_recursive


class TestReadFileFunction(unittest.TestCase):
    def test_read_file_input_no_exists_file(self):
        self.assertEqual(read_file('./fake.text'), [])

    def test_read_file_input_no_parameters(self):
        self.assertEqual(read_file(), [])

    def test_read_file_input_bad_parameters(self):
        self.assertEqual(read_file(path=123), [])

    def test_read_file_valid_parameters(self):
        self.assertTrue(len(read_file(path='./mock_data/company.txt')) >= 0)

    def test_read_file_valid_parameters_path(self):
        self.assertTrue(len(read_file(path=Path('./mock_data/company.txt'))) >= 0)


class TestTotalSalaryFunction(unittest.TestCase):
    def test_total_salary(self):
        self.assertEqual(total_salary(path_to_file="./mock_data/company.txt"), (9001.00, 1800.20))

    def test_total_salary_input_fake_file(self):
        self.assertEqual(total_salary(path_to_file='./fake.text'), None)


class TestCatsInfoFunction(unittest.TestCase):
    def test_cats_info(self):
        self.assertTrue(len(get_cats_info(path_to_file="./mock_data/cats_info.txt")) >= 0)

    def test_cats_info_input_fake_file(self):
        self.assertEqual(get_cats_info(path_to_file='./fake.text'), None)


class TestListDirFunction(unittest.TestCase):
    def test_list_dir_set_path_to_file(self):
        self.assertRaises(ValueError, list_dir_recursive, directory='./mock_data/1.doc')

    def test_list_dir_set_path_to_fake_dir(self):
        self.assertRaises(ValueError, list_dir_recursive, directory='./fake_dir')

    def test_list_dir_success(self):
        self.assertTrue(len(list_dir_recursive(directory='./mock_data')) > 0)
