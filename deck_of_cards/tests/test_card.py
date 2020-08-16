import pytest

from deck_of_cards.card import Card 

def test_card_properties():
    card = Card("red", 7)
    assert(card.color == "red")
    assert(card.rank == 7)

def test_card_score():
    green_card = Card("green", 5)
    yellow_card = Card("yellow", 4)
    red_card = Card("red", 8)

    assert(green_card.score() == 5) # 1 * 5
    assert(yellow_card.score() == 8) # 2 * 4
    assert(red_card.score() == 24) # 3 * 8

def test_valid_input():
    with pytest.raises(ValueError):
        Card("purple", 7)

    with pytest.raises(ValueError):
        Card("red", 17)