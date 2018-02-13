import sys, pygame, math, os
import resource_loader
from Card import Card

pygame.init()

size = width, height = 1000, 800
black = 0, 0, 0
felt = 66, 150, 180

game_title = "Arnason's Hand & Foot Canasta"

display = pygame.display
display.set_caption(game_title)
screen = display.set_mode(size) 

cards, cards_rect, names = resource_loader.load_images('load_cards.nsv', pygame.image)

pos = 0
flag = 0
clock = pygame.time.Clock()


c=[]
for i in range(len(cards)):
    c.append(Card(cards[i], cards_rect[i], names[i]))

for ele in c:
    ele.print_info()

#x=Card(cards[0], cards_rect[0], names[0])
#x.print_info()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[27]:
            pygame.quit()
            sys.exit()

        current_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cards_rect)):
                if cards_rect[i].collidepoint(current_pos):
                    pos = i
                    flag = 1

        if event.type == pygame.MOUSEBUTTONUP and flag:
            flag = 0

        if flag:
            cards_rect[pos].center = current_pos

    screen.fill(felt)
    pygame.draw.rect(screen, pygame.Color(255,255,255,255), \
                             pygame.Rect(200,200, 600, 300), 10)
    
    for i in range(len(cards)):
        screen.blit(cards[i], cards_rect[i])

    pygame.display.flip()
    clock.tick(60)
