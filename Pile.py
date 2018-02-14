from Card import Card
from random import *


class Pile:
    def __init__(self):
        self.pile = []
    

    def generate_pile(self, loaded_objects):
        if not len(loaded_objects) == 3:
            print("ERROR: invalid parameter passed to generate_pile function")
        else:
            length = len(loaded_objects[0])
            for i in range(length):
                self.pile.append(Card(loaded_objects[0][i], \
                                      loaded_objects[1][i], \
                                      loaded_objects[2][i]))


    def get_pile(self):
        return self.pile


    def shuffle_cards(self):
        shuffle(self.get_pile())


    def sort_cards(self):
        self.pile = sorted(self.pile, key=lambda card: card.get_int_value())


    def print_pile(self):
        for card in self.pile:
            card.print_info()

