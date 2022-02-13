
"""
Card game War
Milestone project 2


"""

#card
#SUIT, RANK,VALUE

import random
suits = ("Dimond", "Hearts", "Spade", "clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten","Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8,
          "Nine":9, "Ten": 10, "Jack":11, "Queen":12, "King":13, "Ace":14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.suit + " of " + self.rank



class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                create_cards = Card(suit,rank)
                self.all_cards.append(create_cards)

    def shuffel(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


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
        return f"player {self.name} has {len(self.all_cards)} card"


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffel()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player one looses ")
        print("Player Two Wins")
        game_on = False
        break

    elif len(player_two.all_cards) == 0:
        print("Player Two looses ")
        print("Player One Wins")
        game_on = False
        break

    else:
        player_one_cards = []
        player_one_cards.append(player_one.remove_card())

        player_two_cards = []
        player_two_cards.append(player_two.remove_card())


        at_war = True

        while at_war:

            if player_one_cards[-1].values > player_two_cards[-1].values:

                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                at_war = False

            elif player_one_cards[-1].values < player_two_cards[-1].values:

                player_two.add_cards(player_two_cards)
                player_two.add_cards(player_one_cards)

                at_war = False

            else:

                print("WAR !!!")

                if len(player_one.all_cards) < 3:
                    print("Player one is unable to declear war")
                    print("PLAYER TWO WINS")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 3:
                    print("player two is unable to declear the war")
                    print("PLAYER TWO WINS")
                    game_on = False
                    break

                else:
                    for x in range(3):

                        player_one_cards.append(player_one.remove_card())
                        player_two_cards.append(player_two.remove_card())




