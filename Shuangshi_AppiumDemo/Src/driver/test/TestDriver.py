__author__ = 'zenist'

import unittest
from Src.driver.driver import Driver

class TestDriver(unittest.TestCase):

    def test_01_driverInit(self):
        _my_driver = Driver().get_driver()
        _my_driver2 = Driver().get_driver()
        assert _my_driver == _my_driver2