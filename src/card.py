from dataclasses import dataclass
from functools import total_ordering


class CardKind:
    SWORD = "Sword"
    CUP = "Cup"
    STICK = "Stick"
    GOLD = "Gold"
    ALL_KINDS = [SWORD, CUP, STICK, GOLD]


@dataclass
@total_ordering
class Card:
    value: int
    kind: str

    def __get_hierarchy_table(self):
        ck = CardKind()
        hierarchy = {
            (1, ck.SWORD): 14,
            (1, ck.STICK): 13,
            (7, ck.SWORD): 12,
            (7, ck.GOLD): 11,
            (1, ck.CUP): 8,
            (1, ck.GOLD): 8,
            (7, ck.CUP): 4,
            (7, ck.STICK): 4,
        }
        hierarchy.update({
            (card, kind): value
            for card, value in zip([3, 2, 12, 11, 10, 6, 5, 4], range(10, 1, -1))
            for kind in ck.ALL_KINDS
        })
        return hierarchy

    def get_hierarchy(self):
        hierarchy_table = self.__get_hierarchy_table()
        return hierarchy_table[(self.value, self.kind)]

    def __eq__(self, other):
        return self.value == other.value and self.kind == other.kind

    def __gt__(self, other):
        return self.get_hierarchy() > other.get_hierarchy()

    def __str__(self):
        return f"{self.value} of {self.kind}"
