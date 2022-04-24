# Card Lib

This python file library has three classes: Card, Hand, and Deck. An brief example of class calling is shown in the main.py.

## Card(call using "import Card from *")

A Card has two fields: rank (two through Ace) and suit (Club, Diamond, Heart, Spade).

## Hand(call using "import Hand from *")

A Hand has cards as a container of a list of Cards. It has a method Get to add a particular Card to cards and a method Draw to draw the top card from 
a particular Deck.

## Deck(call using "import Deck from *")

A Deck has several fields: 

1) deck: includes all cards currently stored in this deck
2) decknum: the number of usual deck(some cards excluded) used to form this Deck
3) exclude: the cards that are excluded from a usual deck to form this Deck
4) ranking: the ranking of a deck that allows the user to compare which rank is higher, default as two through Ace
5) suiting: the ranking of a suit of a deck that allows the user to compare which suit is higher, default as none (every suit is equal)

It has a method Shuffle that shuffles the deck in random order, a method Deal that deals the card to given players.
