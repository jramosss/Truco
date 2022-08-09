from src.card import Card, CardKind
import pytest


@pytest.mark.parametrize("card1, card2, eq, gt, lt, gte, lte", [
    ((1, CardKind.SWORD), (1, CardKind.STICK), False, True, False, True, False),
    ((1, CardKind.SWORD), (1, CardKind.SWORD), True, False, False, True, False),
    ((1, CardKind.SWORD), (1, CardKind.GOLD), False, True, False, True, False),
    ((7, CardKind.GOLD), (7, CardKind.SWORD), False, False, True, False, True),
])
def test_equality(card1, card2, eq, gt, lt, gte, lte):
    c1 = Card(*card1)
    c2 = Card(*card2)
    assert c1 == c2 if eq else c1 != c2
    if gt:
        assert c1 > c2
    if gte:
        assert c1 >= c2
    if lt:
        assert c1 < c2
    if lte:
        assert c1 <= c2
