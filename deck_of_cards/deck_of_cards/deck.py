from random import shuffle

from deck_of_cards.card import Card
from deck_of_cards.exceptions import EndOfDeckError

class Deck:
    
    def __init__(self):
        colors = ["red", "yellow", "green"]
        self.cards = [Card(color, rank) for color in colors for rank in range(0, 10)]
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) < 1:
            raise EndOfDeckError
        return self.cards.pop(0)

    def sort(self, colors=["red", "yellow", "green"]):
        if sorted([color.lower() for color in colors]) != ["green", "red", "yellow"]:
            raise ValueError("Must provide an array of the colors 'red', 'yellow' and 'green'.")
        color_sorter = {color: index for index, color in enumerate(colors)}
        self.cards = sorted(self.cards, key=lambda card: (color_sorter[card.color], card.rank))

