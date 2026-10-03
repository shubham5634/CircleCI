import unittest
from CircleCI.main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Yash"
        upper = to_upper(name)
        self.assertEqual(upper, "Yash")

if __name__ == '__main__':
    unittest.main()