import random

SUITES = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.allcards = [(s, r) for s in SUITES for r in RANKS]
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
        return self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()
        print('{} has placed: {}'.format(self.name, drawn_card))
        print('')
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) >= 3:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
        elif len(self.hand.cards) >= 2 and len(self.hand.cards) < 3:
            for x in range(2):
                war_cards.append(self.hand.cards.pop())
            return war_cards
        else:
            war_cards.append(self.hand.cards.pop())
            return war_cards

    
    def have_cards(self):
        if len(self.hand.cards) != 0:
            return True    

# Game Play #
# Create the deck
deck = Deck()
deck.shuffle()
half1, half2 = deck.split_deck()

# Create both players
computer = Player('computer', Hand(half1))
player = input("Enter your name: ")
user = Player(player, Hand(half2))

ttl_rounds = 0
war_count = 0

while user.have_cards() and computer.have_cards():
    ttl_rounds += 1
    print("Start a new round!")
    print('Current Standings: ')
    print(user.name + 'has hte count: ' + str(len(user.hand.cards)))
    print(computer.name + 'has hte count: ' + str(len(computer.hand.cards)))
    print('Play a card!')
    print('')

    table_cards = []

    comp_card = computer.play_card()
    user_card = user.play_card()

    table_cards.append(comp_card)
    table_cards.append(user_card)

    if comp_card[1] == user_card[1]:
        war_count += 1
        print("WAR!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        if RANKS.index(comp_card[1]) < RANKS.index(user_card[1]):  # Change comparison here
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)
    else:
        if RANKS.index(comp_card[1]) < RANKS.index(user_card[1]):  # Change comparison here
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)
    
print('GAME OVER! Number of rounds: ' + str(ttl_rounds))
print('A war happened ' + str(war_count) + ' times.')

if computer.have_cards() == True:
    print('Computer Wins!')
else:
    print('Player Wins!')