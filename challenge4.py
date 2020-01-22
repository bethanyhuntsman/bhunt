import unittest
from utils import fib
from utils import numToString


class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        print(fib(15))
        print(numToString(fib(15)))



if __name__ == '__main__':
        unittest.main()