import unittest, requests

from report import Report

REPORT = Report()


class TestReport(unittest.TestCase):
    def test_fetchData(self):
        # Test for loaded data
        self.assertEqual(REPORT.loadData(), requests.get(REPORT.api).json())

    def test_convert_tup_to_dic(self):
        """
        Test method to check if list of tuple converts to list of dicts

        :return: test should return list of dicts
        """
        list_of_tup = [("2000", "Petrol", 120), ("2000", "Diesel", 70)]
        list_of_dic = [
            {"year": "2000", "petroleum_product": "Petrol", "sale": 120},
            {"year": "2000", "petroleum_product": "Diesel", "sale": 70}
        ]

        self.assertEqual(REPORT.convert(list_of_tup), list_of_dic)

    def test_addFourYears(self):
        """
        Test method to check if add_four_years(year) adds 4 years.

        :return: test should return 4 years added to input year.
        """
        current_year = 2019
        self.assertEqual(REPORT.add_four_years(current_year), 2023)
