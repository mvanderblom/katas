from abc import ABC
from collections import Counter
from typing import List


class Outcome:
    def check(self, dice) -> bool:
        raise NotImplementedError

    def score(self, dice) -> int:
        raise NotImplementedError


class NumberedOutcome(Outcome, ABC):
    def __init__(self, number: int):
        self.number = number


class StraightOutcome(Outcome):
    def check(self, dice: List[int]):
        return dice == [1, 2, 3, 4, 5, 6]

    def score(self, *args):
        return 1200


class SingleOutcome(NumberedOutcome):
    def check(self, dice: List[int]):
        return self.number in dice

    def score(self, *args):
        if self.number == 1:
            return 100
        elif self.number == 5:
            return 50
        return 0


class TripleOutcome(NumberedOutcome):
    def check(self, dice: List[int]):
        return dice.count(self.number) == 3

    def score(self, *args):
        if self.number == 1:
            return 1000
        return self.number * 100


class ThreePairsOutcome(Outcome):
    def check(self, dice: List[int]):
        return list(Counter(dice).values()).count(2) == 3

    def score(self, *args):
        return 800


class NOfAKindOutcome(NumberedOutcome):
    _factors = {6: 8, 5: 4, 4: 2}

    def check(self, dice: List[int]):
        counted_dice = Counter(dice)
        return self.number in counted_dice.values()

    def score(self, dice):
        counted_dice = Counter(dice)
        for (die, count) in counted_dice.items():
            if count == self.number:
                return TripleOutcome(die).score() * self._factors[self.number]
