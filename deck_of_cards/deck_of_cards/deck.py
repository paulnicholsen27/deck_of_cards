from random import shuffle

from deck_of_cards.card import Card
from deck_of_cards.exceptions import EndOfDeckError

class Deck:
    
    def __init__(self):
        colors = ["red", "yellow", "green"]
        self.cards = [Card(color, rank) for color in colors for rank in range(0, 10)]
        shuffle(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            raise EndOfDeckError
        return self.cards.pop()

    def sort(self, colors):
        color_sorter = {color: index for index, color in enumerate(colors)}
        self.cards = sorted(self.cards, key=lambda card: (color_sorter[card.color], card.rank))

