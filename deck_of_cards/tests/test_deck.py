import pytest
from deck_of_cards.card import Card
from deck_of_cards.deck import Deck
from deck_of_cards.exceptions import EndOfDeckError


def test_construction():
    deck = Deck()
    assert len(deck.cards) == 30 # 3 colors ranked 0-9

def test_shuffle():
    deck = Deck()
    old_order = [card for card in deck.cards]
    deck.shuffle()
    assert deck.cards != old_order

def test_draw_card():
    deck = Deck()
    card = deck.draw()
    assert (type(card).__name__ == "Card")
    assert (len(deck.cards) == 29)
    assert (card not in deck.cards)

def test_end_of_deck():
    deck = Deck()
    for _ in range(30):
        deck.draw()
    with pytest.raises(EndOfDeckError):
        deck.draw()

def test_sort_cards(mocker):
    deck = Deck()
    deck.cards = [Card("red", 7),
                  Card("red", 0),
                  Card("red", 3),
                  Card("yellow", 2),
                  Card("yellow", 1),
                  Card("green", 8)]
    deck.sort(["green", "red", "yellow"])
    correct_order = [('green', 8), ('red', 0), ('red', 3), ('red', 7), ('yellow', 1), ('yellow', 2)]
    sorted_cards = [(card.color, card.rank) for card in deck.cards]
    assert (correct_order == sorted_cards)