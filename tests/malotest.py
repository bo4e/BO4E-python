import json
import unittest

from bo4e.bo.marktlokation import Marktlokation


class MaLoTest(unittest.TestCase):
    def test_serializable(self):
        malo = Marktlokation("54321012344")
        json_string = json.dumps(malo, cls=Marktlokation)

if __name__ == '__main__':
    unittest.main()
