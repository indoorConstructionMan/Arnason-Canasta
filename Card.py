class Card:
    def __init__(self, image_face, image_rect, name, image_back):
        self.image_face = image_face
        self.image_back = image_back[0]
        self.rect = image_rect
        self.name = name
        self.value = self.get_value()
        self.worth = self.get_worth()
        self.suit = self.get_suit()
        self.color = self.get_color()
        self.int_value = self.get_int_value()


    def flip_card_over(self):
        tmp = self.image_face 
        self.image_face = self.image_back
        self.image_back = tmp


    def get_value(self):
        return self.name.rstrip('.png\n').split('-')[0]


    def get_suit(self):
        return self.name.rstrip('.png\n').split('-')[1]


    def get_surface(self):
        return self.image_face


    def get_rectangle(self):
        return self.rect


    def get_worth(self):

        val = self.get_value()
        if val == 'ace' or val == 'two':
            return str(20)
        elif val == 'three':
            if self.get_color() == 'red':
                return str(100)
            else:
                return str(5)
        elif val == 'four' or val == 'five' or val == 'six' or val == 'seven':
            return str(5)
        else:
            return str(10)


    def get_color(self):
        if self.get_suit() == 'hearts' or self.get_suit() == 'diamonds':
            return 'red'
        else: 
            return 'black'


    def get_int_value(self):
        return {
            'ace':1,
            'two':2,
            'three':3,
            'four':4,
            'five':5,
            'six':6,
            'seven':7,
            'eight':8,
            'nine':9,
            'ten':10,
            'jack':11,
            'queen':12,
            'king':13,
            'joker':14,
            'card':-1
        }[self.get_value()]


    def print_info(self):
        print("Information for " + self.name + "\nVal: " + self.get_value() \
              + "\nSuit: " + self.get_suit() + "\nWorth: " + self.get_worth() \
              + "\nColor: " + self.get_color() + "\nInt Val: " \
              + str(self.get_int_value()) + "\n")
