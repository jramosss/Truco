from src.utils import calculate_points
from src.card import Card, CardKind
import pytest


ck = CardKind()


@pytest.mark.parametrize("cards, expected", [
    ([Card(1, ck.SWORD), Card(7, ck.SWORD), Card(3, ck.SWORD)], 30),
    ([Card(6, ck.SWORD), Card(7, ck.SWORD), Card(3, ck.SWORD)], 33),
    ([Card(10, ck.SWORD), Card(11, ck.SWORD), Card(12, ck.SWORD)], 0),
    ([Card(11, ck.SWORD), Card(7, ck.SWORD), Card(2, ck.STICK)], 27),
    ([Card(7, ck.SWORD), Card(2, ck.STICK), Card(1, ck.CUP)], 7),
    ([Card(1, ck.SWORD), Card(1, ck.STICK), Card(1, ck.CUP)], 1)
])
def test_calculate_points(cards, expected):
    points = calculate_points(cards)
    assert points == expected
