# Importações:
# Importação da biblioteca do pygame:
import pygame

# Iniciar o pygame:
pygame.init()

# Gráfico inicial e nome do display:
tamanho = (800, 600)  # Resolução 800x600.
titulo = "Pokémon: Introcomp"  # Nome do jogo.
pygame.display.set_caption(titulo)  # Coloca o nome do jogo.
tela = pygame.display.set_mode(tamanho)  # Define o tamanho da janela.
