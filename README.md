# deck_of_cards

This module contains the files necessary to create and test a `Deck` and `Card` class.  

## Cards

A `Card` is instantiated with a color and a rank.  The color must be `red`, `yellow`, or `green` (case-insensitive) and the rank must be an integer from 0-9, inclusive.  

###
`.score()` returns an integer of the cards score, which is the product of the card's rank and color value.  The values of the colors are:
    * red: 3
    * yellow: 2
    * green: 1

## Deck

A `Deck` is instantiated as a collection of 30 unique `Card` objects, comprising the ranks 0-9 for each of the colors red, yellow, and green.

###
`.cards()` returns the array of `Card` objects

`.shuffle()` randomizes the order of the `.cards` array

`.draw()` returns the first `Card` from the `.cards` array, removing it from the `Deck`.  If there are no `Card`s left in the `Deck`, an `EndOfDeckError` is raised.

`.sort(color_array=["red", "yellow", "green"])` sorts the cards by color in the order provided by the user, and sorts the cards within each color by rank.  Raises `ValueError` if input is provided that does not comprise the strings `"red"`, `"yellow"`, `"green"` in any order.