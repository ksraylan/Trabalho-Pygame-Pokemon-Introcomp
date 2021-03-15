import os
import pygame

# para testes:
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1920,0)

# Iniciar o pygame:
pygame.init()

tamanho = (800, 600)
titulo = "Pokemon"
pygame.display.set_caption(titulo)
tela = pygame.display.set_mode(tamanho, pygame.NOFRAME)

