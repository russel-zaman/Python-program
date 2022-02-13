
"""
card game project

"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return self.suit + " of " + self.rank


## Creating deck class

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                create_cards = Card(suit,rank)
                self.all_cards.append(create_cards)


    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()


#Creating Player class

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_card(self):

        return self.all_cards.pop(0)

    def add_cards(self,new_card):

        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def __str__(self):

        return f"Player {self.name} has {len(self.all_cards)} card"


# Game setup

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# game logic

game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f"round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One loose !")
        print("Player Two Wins !!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two loose !")
        print("Player One Wins !!")
        game_on = False
        break


    # Starting new round

    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())


    # When war happen

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("WAR !!! ")

            if len(player_one.all_cards) < 3:
                print("Player one is unable to decler war!")
                print("Player Two wins !!")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print("Player two is unable to decler war!")
                print("Player One wins !!")
                game_on = False
                break

            else:
                for num in range(3):

                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())


















###-------------### some check ###-----------###


two_heart = Card("Heart","Two")

print(two_heart)
print(two_heart.suit)
print(two_heart.value)

five_spade = Card("Spade","Five")

print(five_spade)
print(five_spade.value)
print(five_spade.rank)
print(five_spade.suit)


new_deck = Deck()
first_card = new_deck.all_cards[0]
print(first_card)

for cards in new_deck.all_cards:
    print(cards)

new_deck = Deck()
bottom_card = new_deck.all_cards[-1]

new_deck.shuffle()

mycard = new_deck.deal_one()
print(mycard)


new_player = Player("Russel")
new_player.add_cards(mycard)
print(new_player)

new_player.add_cards([mycard,mycard,mycard])
print(new_player)

new_player.remove_card()
print(new_player)










