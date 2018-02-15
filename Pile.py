from Card import Card
from random import *


class Pile:
    def __init__(self):
        self.pile = []
    

    def generate_pile(self, loaded_objects):
        if not len(loaded_objects) == 4:
            print("ERROR: invalid parameter passed to generate_pile function")
        else:
            length = len(loaded_objects[0])
            for i in range(length):
                self.pile.append(Card(loaded_objects[0][i], \
                                      loaded_objects[1][i], \
                                      loaded_objects[2][i],
                                      loaded_objects[3]))


    def generate_multiple_piles(self, number, loaded_objects):
        for i in range(number):
            self.generate_pile(loaded_objects)
            
                
                
    def get_pile(self):
        return self.pile


    def shuffle_cards(self):
        shuffle(self.get_pile())


    def sort_cards(self):
        self.pile = sorted(self.pile, key=lambda card: card.get_int_value())


    def print_pile(self):
        for card in self.pile:
            card.print_info()


    def get_pile_value(self):
        sum = 0
        for card in self.get_pile():
            sum += int(card.get_worth())
        return sum


    # this function should also be abstract
    def change_cards_position_in_pile(self, h, offset):
        w = 40
        for card in self.get_pile():
            card.get_rectangle().center = [w, h]
            w += offset


    # this function should probably be abstract.
    def change_pile_position(self, w, h):
        for card in self.get_pile():
            card.get_rectangle().center = [w, h]

