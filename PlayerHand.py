from Pile import Pile
import random
import math


class PlayerHand(Pile):
    def __init__(self):
        self.hand = []
        self.foot = []
        self.dealt = False
        super(PlayerHand, self).__init__()

    def get_current_hand(self):
        return self.pile


    def get_foot(self):
        return self.foot


    def get_hand(self):
        return self.hand


    def deal_hand_and_foot(self, deck):
        pile = deck.get_pile()
        length = len(pile)
        for i in range(15):
            self.hand.append(pile.pop(math.floor(random.random() * length)))
            length -= 1
            self.foot.append(pile.pop(math.floor(random.random() * length)))
            length -= 1

        for card in self.foot:
            card.flip_card_over()

        self.dealt = True
        self.pile = self.hand

