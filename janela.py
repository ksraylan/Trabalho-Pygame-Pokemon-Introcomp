import os
import pygame

# Somente para usar na transmissão de tela no Discord (apagar quando o jogo estiver pronto):
#os.environ['SDL_VIDEO_WINDOW_POS'] = '1920,0'

# Iniciar o pygame:
pygame.init()

tamanho = (800, 600)
titulo = "Pokemon"
pygame.display.set_caption(titulo)
tela = pygame.display.set_mode(tamanho, pygame.NOFRAME)

