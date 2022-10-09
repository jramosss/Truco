from itertools import chain
from random import shuffle

from src.card import Card, CardKind


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

    def take_three(self):
        return [self.cards.pop(idx) for idx in range(3)]

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])
