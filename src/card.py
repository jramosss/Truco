from dataclasses import dataclass


class CardKind:
    SWORD = "Sword"
    CUP = "Cup"
    STICK = "Stick"
    GOLD = "Gold"


@dataclass
class Card:
    value: int
    kind: str

    def __str__(self):
        return f"{self.value} of {self.kind}"

    def get_hierarchy(self):
        ck = CardKind()
        hierarchy = {
            (1, ck.SWORD): 14,
            (1, ck.STICK): 13,
            (7, ck.SWORD): 12,
            (7, ck.GOLD): 11,
            (3, ck.SWORD): 10,
            (3, ck.GOLD): 10,
            (3, ck.CUP): 10,
            (3, ck.STICK): 10,
            (2, ck.SWORD): 9,
            (2, ck.GOLD): 9,
            (2, ck.CUP): 9,
            (2, ck.STICK): 9,
            (1, ck.CUP): 8,
            (1, ck.GOLD): 8,
            (12, ck.SWORD): 7,
            (12, ck.GOLD): 7,
            (12, ck.CUP): 7,
            (12, ck.STICK): 7,
            (11, ck.SWORD): 6,
            (11, ck.GOLD): 6,
            (11, ck.CUP): 6,
            (11, ck.STICK): 6,
            (10, ck.SWORD): 5,
            (10, ck.GOLD): 5,
            (10, ck.CUP): 5,
            (10, ck.STICK): 5,
            (7, ck.CUP): 4,
            (7, ck.STICK): 4,
            (6, ck.SWORD): 3,
            (6, ck.GOLD): 3,
            (6, ck.CUP): 3,
            (6, ck.STICK): 3,
            (5, ck.SWORD): 2,
            (5, ck.GOLD): 2,
            (5, ck.CUP): 2,
            (5, ck.STICK): 2,
            (4, ck.SWORD): 1,
            (4, ck.GOLD): 1,
            (4, ck.CUP): 1,
            (4, ck.STICK): 1,
        }
        return hierarchy[(self.value, self.kind)]

    def __eq__(self, other):
        return self.value == other.value and self.kind == other.kind

    def __gt__(self, other):
        return self.get_hierarchy() > other.get_hierarchy()

    def __lt__(self, other):
        return self.get_hierarchy() < other.get_hierarchy()

    def __ge__(self, other):
        return self.get_hierarchy() >= other.get_hierarchy()

    def __le__(self, other):
        return self.get_hierarchy() <= other.get_hierarchy()
