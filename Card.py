class Card:
    def __init__(self, image_face, image_back, name):
        self.image_face = image_face
        self.image_back = image_back
        self.name = name
        self.value = self.get_value()
        self.worth = self.get_worth()
        self.suit = self.get_suit()
        self.color = self.get_color()


    def get_value(self):
        return self.name.rstrip('.png\n').split('-')[0]


    def get_suit(self):
        return self.name.rstrip('.png\n').split('-')[1]

    
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


    def print_info(self):
        print("Information for " + self.name + "\nVal: " + self.get_value() \
              + "\nSuit: " + self.get_suit() + "\nWorth: " + self.get_worth() \
              + "\nColor: " + self.get_color() + "\n")
