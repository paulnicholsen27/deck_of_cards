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
    for n in range(30):
        deck.draw()
    with pytest.raises(EndOfDeckError):
        deck.draw()

def test_sort_cards(mocker):
    deck = Deck()
    mocker.patch.object(
        deck,
        "cards",
        return_value=[Card("red", 7),
                      Card("red", 0),
                      Card("red", 3),
                      Card("yellow", 2),
                      Card("yellow", 1),
                      Card("green", 8)]
    )
    deck.sort(["green", "red", "yellow"])
    assert (deck.cards == [Card("green", 8),
                           Card("red", 0),
                           Card("red", 3),
                           Card("red", 7),
                           Card("yellow", 1),
                           Card("yellow", 2)])

def test_draw_hand():
    deck = Deck()
    hand = deck.draw_three()
    assert (len(hand) == 3)



    