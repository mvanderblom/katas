from greed import Greed
from outcomes import *

greed_instance = Greed([
    StraightOutcome(),
    ThreePairsOutcome(),
    NOfAKindOutcome(6),
    NOfAKindOutcome(5),
    NOfAKindOutcome(4),
    TripleOutcome(6),
    TripleOutcome(5),
    TripleOutcome(4),
    TripleOutcome(3),
    TripleOutcome(2),
    TripleOutcome(1),
    SingleOutcome(5),
    SingleOutcome(1)
])
