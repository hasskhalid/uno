"""
In this project, I want to create a 2 player uno game, where
the deck is shuffled and then a player can play their desired
card from their hand. If a player cannot play a single card,
then they will pick a card from the deck.

This game should end when someone has only 1 card left on their
hand.
"""
import random

# list of all the cards in an uno deck
deck = [
    "R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9",
    "Y0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9",
    "G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",
    "B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"
]

random.shuffle(deck)

players = []
num_of_players = 2
