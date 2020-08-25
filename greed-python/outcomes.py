from collections import Counter
from typing import List


class Outcome:
    def check(self, dice) -> bool:
        raise NotImplementedError

    def score(self, dice=None) -> int:
        raise NotImplementedError


class StraightOutcome(Outcome):
    def check(self, dice: List[int]):
        return dice == [1, 2, 3, 4, 5, 6]

    def score(self, dice=None):
        return 1200


class NumberedOutcome(Outcome):
    def __init__(self, number):
        self.number = number


class SingleOutcome(NumberedOutcome):
    def check(self, dice: List[int]):
        return self.number in dice

    def score(self, dice=None):
        if self.number == 1:
            return 100
        elif self.number == 5:
            return 50
        return 0


class TripleOutcome(NumberedOutcome):
    def check(self, dice: List[int]):
        return dice.count(self.number) == 3

    def score(self, dice=None):
        if self.number == 1:
            return 1000
        return self.number * 100


class ThreePairsOutcome(Outcome):
    def check(self, dice: List[int]):
        return list(Counter(dice).values()).count(2) == 3

    def score(self, dice=None):
        return 800


class NOfAKindOutcome(NumberedOutcome):
    def check(self, dice: List[int]):
        counted_dice = Counter(dice)
        return self.number in counted_dice.values()

    def score(self, dice=None):
        counted_dice = Counter(dice)
        for (die, count) in counted_dice.items():
            if count == self.number:
                return TripleOutcome(die).score() * self.get_factor()

    def get_factor(self) -> int:
        if self.number == 6:
            return 8
        elif self.number == 5:
            return 4
        elif self.number == 4:
            return 2
