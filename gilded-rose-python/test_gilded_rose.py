# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_quality_degrades_twice_as_fast_after_sell_by_date(self):
        items = [Item("foo", 1, 10), Item("bar", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        self.assertEqual(8, items[1].quality)

    def test_quality_is_never_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_in_quality_with_age(self):
        items = [Item("Aged Brie", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_aged_brie_increases_in_quality_twice_as_fast_after_sell_by_date(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_quality_is_never_higher_than_50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_doesnt_degrade(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(25, items[0].quality)

    def test_sulfuras_doesnt_age(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

        items[0].sell_in = 10
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

        items[0].sell_in = 5
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

        items[0].sell_in = -1
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()