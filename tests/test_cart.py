import unittest

from shop.cart import Cart


class TestCart(unittest.TestCase):
    def test_empty_cart_total_is_zero(self):
        self.assertEqual(Cart().total(), 0)

    def test_single_item(self):
        cart = Cart()
        cart.add("pan", 1.20)
        self.assertAlmostEqual(cart.total(), 1.20)

    def test_two_items_with_quantity_one(self):
        cart = Cart()
        cart.add("pan", 1.20)
        cart.add("leche", 0.80)
        self.assertAlmostEqual(cart.total(), 2.00)

    def test_item_with_quantity_greater_than_one(self):
        cart = Cart()
        cart.add("café", 2.50, quantity=3)
        self.assertAlmostEqual(cart.total(), 7.50)


if __name__ == "__main__":
    unittest.main()
