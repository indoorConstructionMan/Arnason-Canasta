import sys, pygame, math, os
import resource_loader
from Card import Card
from Pile import Pile

pygame.init()

size = width, height = 1000, 800
black = 0, 0, 0
felt = 66, 150, 180

game_title = "Arnason's Hand & Foot Canasta"

display = pygame.display
display.set_caption(game_title)
screen = display.set_mode(size) 


pile=Pile()
pile.generate_pile(resource_loader.load_images('load_cards.nsv', pygame.image))


pos = 0
flag = 0
clock = pygame.time.Clock() 

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[27]:
            pygame.quit()
            sys.exit()

        current_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for card in pile.get_pile():
                if card.get_rectangle().collidepoint(current_pos):
                    pos = card
                    flag = 1

        if event.type == pygame.MOUSEBUTTONUP and flag:
            flag = 0

        if flag:
            pos.get_rectangle().center = current_pos

    screen.fill(felt)
    pygame.draw.rect(screen, pygame.Color(255,255,255,255), \
                             pygame.Rect(200,200, 600, 300), 10)

    for card in pile.get_pile():
        screen.blit(card.get_surface(), card.get_rectangle())

    pygame.display.flip()
    clock.tick(60)
