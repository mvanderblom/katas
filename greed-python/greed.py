from typing import List

from outcomes import Outcome


class Greed:
    def __init__(self, outcomes_in_order: List[Outcome]):
        self.outcomes_in_order = outcomes_in_order

    def score(self, dice: List[int]) -> int:
        if len(dice) > 6:
            raise ValueError('Too many arguments')

        dice = sorted(dice)

        for outcome in self.outcomes_in_order:
            if outcome.check(dice):
                return outcome.score(dice)

        return 0
