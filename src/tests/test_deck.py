from pprint import pprint
import pytest
from src.deck import Deck


@pytest.mark.parametrize("tens_included", [True, False])
def test_deck_init(tens_included):
    deck = Deck(tens_included=tens_included)
    assert len(deck.cards) == 40 if tens_included else 36

def get_array_of_tuples_len(lst: list):
    sum = 0
    for item in lst:
        sum += len(item)
    return sum

@pytest.mark.parametrize("number_of_players", [2, 4, 6])
def test_give_cards(number_of_players):
    deck = Deck()
    cards = []
    for _ in range(number_of_players):
        cards.append(deck.take_three())
    assert get_array_of_tuples_len(cards) == 3 * number_of_players
