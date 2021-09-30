"""
In this project, I want to create a 2 player uno game, where
the deck is shuffled and then a player can play their desired
card from their hand. If a player cannot play a single card,
then they will pick a card from the deck.

This game should end when someone has only 1 card left on their
hand.
"""
import random
import time
from os import system
from colorama import Fore, Style

"""
this will print the card in its respective color
EXAMPLE: 
R9 will get printed in red to the console
"""


def print_card_in_color(card):
    if card[0] == "R":
        print(Fore.RED + card)
    elif card[0] == "Y":
        print(Fore.YELLOW + card)
    elif card[0] == "G":
        print(Fore.GREEN + card)
    elif card[0] == "B":
        print(Fore.BLUE + card)
    else:
        print(Fore.WHITE + card)


"""
determines if card matches color or number
"""


def validate_card(play, card_to_match):
    if play[0] == card_to_match[0]:
        print("Same color!")
        return True
    elif play[1] == card_to_match[1]:
        print("Same number!")
        return True
    else:
        return False


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

for i in range(num_of_players):
    hand = [deck.pop() for i in range(7)]  # removes and add 7 cards from deck into hand
    hand.insert(0, "Draw")
    players.append(hand)

card_to_match = deck.pop()

running = True  # used to run the game

"""
the actual game, goes through each player then asks
if each player wants to play a card from their hand or
draw one from the deck
"""

while running:
    for count, player in enumerate(players, 1):  # numbers each player
        print("Player " + str(count))
        for card in player:  # loops through each player
            print_card_in_color(card)  # prints player's card
        print(Style.RESET_ALL, end='')  # reverts back to normal font color
        print("Card to match: " + card_to_match)  # prints the card to match from deck
        play = input("What card would yoi like to play?")
        if validate_card(play, card_to_match):  # determines if card is valid to play
            player.remove(play)
            card_to_match = play
            if len(player) == 1:  # if player has uno
                print("Congratulations Player " + str(count) + "!")
                running = False
                break
            else:  # if player needs to draw a card
                player.append(deck.pop())
            time.sleep(1)
            system('clear')
print("Game Over! See you next time!")
