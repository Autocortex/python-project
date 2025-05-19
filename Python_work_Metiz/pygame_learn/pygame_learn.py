import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Ooo')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)

        screen.fill((30,30,30))
        pygame.display.flip()
