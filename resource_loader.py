import os, pygame

def load_image(name, pyimg):
    fullname = os.path.join('resources/', name)
    try:
        image = pyimg.load(fullname)
    except pygame.error:
        print("Cannot load image: " + name)
        raise SystemExit
    return image


def load_images(name, pyimg):
    cards = []
    cards_rect = []
    card_name = []
    card_back = []
    with open("resources/" + name, 'r+') as f:
        data = f.readlines()
        for line in data:
            if not line=='card-back.png\n':
                card_name.append(line)
                img = load_image(line.rstrip('\n'), pyimg)
                cards.append(img.convert_alpha())
                cards_rect.append(img.get_rect())
            else:
                img = load_image(line.rstrip('\n'), pyimg)
                card_back.append(img.convert_alpha())

    return [cards, cards_rect, card_name, card_back]
