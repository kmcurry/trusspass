import unittest
import sys
sys.path.append('./')
from csv_parser import *

class MyFirstTests(unittest.TestCase):

    def test_should_convert_to_iso8601(self):
        convert_to_iso8601("4/1/11 11:00:00 AM")
    
    def test_should_drop_row_for_date_error(self):
        try:
            convert_to_iso8601("4/1/11🍏AM")
        except:
            pass

    def test_should_normalize_zipcode(self):
        normalize_zipcode("0102")

    def test_should_normalize_name(self):
        normalize_name("kevin curry")
    
    def test_should_normalize_addr(self):
        normalize_addr("23 Gangnam, Style Lives Here, Gangnam Town, USA")


if __name__ == '__main__':
    unittest.main()
