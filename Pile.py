from Card import Card
from random import *
import resource_loader


class Pile:
    def __init__(self):
        self.pile = []
    
    def generate_multiple_decks(self, path, pyimg, number):
        if number <= 1:
            return 0
        for i in range(number):
            loaded_objects = resource_loader.load_images(path, pyimg)
            self.generate_pile(loaded_objects)


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

    
    def move_card(self, card, w, h):
        card.get_rectangle().center = [w,h]


    # this function should also be abstract
    def change_cards_position_in_pile(self, h, offset):
        w = 40
        for card in self.get_pile():
            card.get_rectangle().center = [w, h]
            w += offset


    # this function should probably be abstract.
    def change_pile_position(self, w, h, visible):

        for card in self.get_pile():
            if visible:
                card.flip_card_over()
            card.get_rectangle().center = [w, h]

