import unittest


class SpreadsheetTests(unittest.TestCase):
    def test_calculate_checksum(self):
        spreadsheet = Spreadsheet([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])
        self.assertEqual(spreadsheet.checksum(), 18)


class Spreadsheet:
    def __init__(self, values):
        self.values = values

    def checksum(self):
        return 1


if __name__ == '__main__':
    unittest.main()
