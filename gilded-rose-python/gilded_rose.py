# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.age()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgingItem(Item):
    def age(self):
        self._update_sell_in()
        self._update_quality()

    def _update_sell_in(self):
        self.sell_in -= 1

    def _update_quality(self):
        modifier = self._get_quality_modifier()
        if 0 <= self.quality + modifier <= 50:
            self.quality += modifier

    def _get_quality_modifier(self):
        if self.sell_in >= 0:
            return -1
        return -2


class ConjuredItem(AgingItem):
    def _get_quality_modifier(self):
        return super()._get_quality_modifier() * 2


class LegendaryItem(AgingItem):
    def age(self):
        pass


class AgedBrie(AgingItem):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def _get_quality_modifier(self):
        return super()._get_quality_modifier() * -1


class BackstagePass(AgingItem):
    def _get_quality_modifier(self):
        if self.sell_in <= 0:
            return self.quality * -1
        elif self.sell_in < 5:
            return 3
        elif self.sell_in < 10:
            return 2
        return 1