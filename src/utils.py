from pprint import pprint
from src.card import Card
from itertools import chain, combinations


def calculate_points(cards: list[Card]):
    figures = [10, 11, 12]
    points_list: list[int] = []
    points = 0
    tuples = chain.from_iterable(combinations(cards, r) for r in range(1, len(cards) + 1))
    tuples_list = list(tuples)[3:6]
    for card1, card2 in tuples_list:
        if card1.value in figures and card2.value in figures:
            points = 0
        elif card1.kind == card2.kind:
            points = 20 + card1.value + card2.value
            if card1.value in figures and card2.value not in figures:
                points = 20 + card2.value
            elif card2.value in figures and card1.value not in figures:
                points = 20 + card1.value
        else:
            if not (card1.value in figures and card2.value in figures):
                points = max(card1.value, card2.value)
        points_list.append(points)
    return max(points_list)


