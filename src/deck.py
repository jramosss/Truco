from src.card import Card, CardKind
from random import shuffle
from itertools import chain


class Deck:
    def __init__(self, tens_included: bool = False):
        self.cards: list[Card] = []
        self.tens_included = tens_included
        self.build()

    def build(self):
        for kind in CardKind.ALL_KINDS:
            numbers = chain(range(1, 8), [11, 12])
            if self.tens_included:
                numbers = chain(numbers, [10])
            for number in numbers:
                self.cards.append(Card(number, kind))

    def shuffle(self):
        shuffle(self.cards)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def take_three(self):
        return [self.cards.pop(idx) for idx in range(3)]
