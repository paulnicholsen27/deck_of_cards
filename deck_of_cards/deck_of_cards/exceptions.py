class EndOfDeckError(Exception):

    def __str__(self):
        return "There are no cards left in the deck."