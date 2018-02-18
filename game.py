import sys, pygame, math, os
from Card import Card
from Pile import Pile
from PlayerHand import PlayerHand
import random

pygame.init()

size = width, height = 1200, 800
black = 0, 0, 0
felt = 66, 150, 180

game_title = "Arnason's Hand & Foot Canasta"

display = pygame.display
display.set_caption(game_title)
screen = display.set_mode(size) 


cards_pile=Pile()
cards_pile.generate_multiple_decks('load_cards.nsv', pygame.image, 6)
card_width = cards_pile.get_pile()[0].get_rectangle().width
cards_pile.change_pile_position(width/2 - card_width/2 - 5, height/2, True)

card = cards_pile.get_pile()[1]
card.flip_card_over()
cards_pile.move_card(card, width/2 + card_width/2 + 5, height/2)

clicked_card = 0
flag = 0
clock = pygame.time.Clock() 


player1_hand = PlayerHand()
player1_hand.deal_hand_and_foot(cards_pile)
player1_hand.change_pile_position(0,0,True)
player1_hand.sort_cards()
player1_hand.change_cards_position_in_pile((7 * height) / 8, 20)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[27]:
            pygame.quit()
            sys.exit()

        current_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #need to fix this inefficient double looping 
            for card in cards_pile.get_pile():
                if card.get_rectangle().collidepoint(current_pos):
                    clicked_card = card
                    flag = 1
            for card in player1_hand.get_pile():
                if card.get_rectangle().collidepoint(current_pos):
                    clicked_card = card
                    flag = 1

        if event.type == pygame.MOUSEBUTTONUP and flag:
            flag = 0

        if flag:
            clicked_card.get_rectangle().center = current_pos

    screen.fill(felt)
    pygame.draw.line(screen, pygame.Color(128,128,128,128), \
                                          [0,(3 * height)/4], [width, (3*height)/4], 10)
    pygame.draw.rect(screen, pygame.Color(255,255,255,255), \
                             pygame.Rect(200,200, 600, 300), 10)
    

    for card in player1_hand.get_pile():
        screen.blit(card.get_surface(), card.get_rectangle())

    for card in cards_pile.get_pile():
        screen.blit(card.get_surface(), card.get_rectangle())

    pygame.display.flip()
    clock.tick(60)
