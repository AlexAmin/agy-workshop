import unittest

from shop.formatting import format_price


class TestFormatting(unittest.TestCase):
    def test_two_decimals(self):
        self.assertEqual(format_price(5), "5.00")

    def test_rounds_to_cents(self):
        self.assertEqual(format_price(1.234), "1.23")


if __name__ == "__main__":
    unittest.main()
