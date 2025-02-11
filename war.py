import random

SUITES = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.allcards = [(suite, rank) for suite in SUITES for rank in RANKS]
        print("Creating a new deck")
    
    def shuffle(self):
        random.shuffle(self.allcards)
        print("Shuffling the deck")

    def split_deck(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self):
        return 'Contains {} cards'.format(len(self.cards))
    
    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        self.cards.pop()

class Player:
    '''
    This will take in a name and an instance of Hand. The player can 
    then play cards and check if they still have cards.
    '''
    pass

# Game Play #
