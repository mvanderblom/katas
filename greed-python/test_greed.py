from unittest import TestCase

from main import greed_instance


class TestGreed(TestCase):

    def test_a_single_one(self):
        self.assertEqual(100, greed_instance.score([1]))

    def test_a_single_five(self):
        self.assertEqual(50, greed_instance.score([5]))

    def test_triple_ones(self):
        self.assertEqual(1000, greed_instance.score([1, 1, 1]))

    def test_triple_twos(self):
        self.assertEqual(200, greed_instance.score([2, 2, 2]))

    def test_triple_threes(self):
        self.assertEqual(300, greed_instance.score([3, 3, 3]))

    def test_triple_fours(self):
        self.assertEqual(400, greed_instance.score([4, 4, 4]))

    def test_triple_fives(self):
        self.assertEqual(500, greed_instance.score([5, 5, 5]))

    def test_triple_sixes(self):
        self.assertEqual(600, greed_instance.score([6, 6, 6]))

    def test_four_of_a_kind(self):
        self.assertEqual(2000, greed_instance.score([1, 1, 1, 1]))

    def test_five_of_a_kind(self):
        self.assertEqual(4000, greed_instance.score([1, 1, 1, 1, 1]))

    def test_six_of_a_kind(self):
        self.assertEqual(8000, greed_instance.score([1, 1, 1, 1, 1, 1]))

    def test_three_pairs(self):
        self.assertEqual(800, greed_instance.score([1, 1, 2, 2, 3, 3]))

    def test_straight(self):
        self.assertEqual(1200, greed_instance.score([1, 2, 3, 4, 5, 6]))

    def test_straight_out_of_order(self):
        self.assertEqual(1200, greed_instance.score([4, 5, 6, 1, 2, 3]))

    def test_too_many_dice(self):
        with self.assertRaises(ValueError):
            greed_instance.score([1, 2, 3, 4, 5, 6, 7])
