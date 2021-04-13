# Importações:
# Precisamos importar o pygame para poder carregar as imagens:
import pygame

# E precisamos importar a janela.py para obtermos a largura da janela:
import Dados.janela as janela

# Começamos o jogo tocando a música de abertura:
pygame.mixer.music.load('Dados/Recursos/Sprites/SonsPokemon/fireRedAbertura.wav')

# A escala do jogo será a largura da janela (800) dividido por 240 (largura da resolução
# original do Gameboy Advanced), que dá 3.333...
# Assim, não teremos tamanho de imagens diferentes um do outro e podemos suportar outras
# resoluções como widescreen se quisermos sem muitos esforços:  
escala = janela.tamanho[0] / 240
# Aqui a gente carrega todas as imagens da interface do jogo:
img_opcoes_batalha = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/fgt_options.png').convert_alpha()
img_barra1 = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/barra_1.png').convert_alpha()
img_barra2 = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/barra_2.png').convert_alpha()
img_barra_sem_vida = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/barra_sem_vida.png').convert_alpha()
img_pp_bar = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/pp_bar.png').convert_alpha()
img_fundo_pokemon = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/FundoPokemon_1.png').convert_alpha()
img_fundo_pokemon_circulo1 = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/FundoPokemon_2.png'
                                               ).convert_alpha()
img_fundo_pokemon_circulo2 = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/FundoPokemon_3.png'
                                               ).convert_alpha()
img_text_bar = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/text_bar.png').convert_alpha()
img_vida_amarela = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/vida_amarela.png').convert_alpha()
img_vida_vermelha = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/vida_vermelha.png').convert_alpha()
img_bag = pygame.image.load('Dados/Recursos/Sprites/SpritesInterface/bag_1.png').convert_alpha()

# Depois disso a gente aumenta o tamanho deles de acordo com a escala:
img_pp_bar = pygame.transform.scale(img_pp_bar, (int(240 * escala), int(48 * escala)))
img_vida_amarela = pygame.transform.scale(img_vida_amarela, (int(9 * escala), int(3 * escala)))
img_vida_vermelha = pygame.transform.scale(img_vida_vermelha, (int(9 * escala), int(3 * escala)))
img_barra_sem_vida = pygame.transform.scale(img_barra_sem_vida, (int(9 * escala), int(3 * escala)))
img_bag = pygame.transform.scale(img_bag, (int(240 * escala), int(160 * escala)))
img_barra1 = pygame.transform.scale(img_barra1, (int(101 * escala), int(29 * escala)))
img_barra2 = pygame.transform.scale(img_barra2, (int(104 * escala), int(39 * escala)))
img_opcoes_batalha = pygame.transform.scale(img_opcoes_batalha, (int(120 * escala), int(48 * escala)))
img_text_bar = pygame.transform.scale(img_text_bar, (int(240 * escala), int(48 * escala)))

# Altura para escalar a imagem de fundo:
escala_height = janela.tamanho[1] / 160

# Imagem de fundo:
img_fundo_pokemon = pygame.transform.scale(img_fundo_pokemon, (int(240 * escala), int(112 * escala_height * 1.05)))
# Círculos que ficam em baixo dos pokémons:
img_fundo_pokemon_circulo1 = pygame.transform.scale(img_fundo_pokemon_circulo1, (int(128 * escala), int(32 * escala)))
img_fundo_pokemon_circulo2 = pygame.transform.scale(img_fundo_pokemon_circulo2, (int(120 * escala), int(11 * escala)))


# Essa função carregará duas imagens, uma do pokémon de frente e outra de costas,
# e retornará as mesmas:
def carregar_imagem_pokemon(numero, shiny=False):
    # Se foi pedido shiny:
    nome = str(numero) if not shiny else str(numero) + "_s"
    return [pygame.transform.scale(pygame.image.load("Dados/Recursos/Sprites/SpritesPokemon/Frente/{}.png".format(nome)
                                                     ), (int(64 * escala), int(64 * escala))),
            pygame.transform.scale(pygame.image.load("Dados/Recursos/Sprites/SpritesPokemon/Costas/{}.png".format(nome)
                                                     ), (int(64 * escala), int(64 * escala)))]


# Essa carregará as imagens dos Easter Eggs:
def carregar_imagem_easter_egg(nome):
    return [pygame.transform.scale(pygame.image.load("Dados/Recursos/Sprites/EasterEgg/{}_edit.png".format(nome)),
                                   (int(64 * escala), int(64 * escala))),
            pygame.transform.scale(pygame.image.load("Dados/Recursos/Sprites/EasterEgg/{}_edit.png".format(nome)),
                                   (int(64 * escala), int(64 * escala)))]


# Carregando os efeitos sonoros:
som_Batalha = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/batalha.wav")
som_Bubble = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Bubble.wav")
som_Confusion = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Confusion.wav")
som_derrota = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/derrota.wav")
som_Ember = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Ember.wav")
som_menu_mudou = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/firered_0005.wav")
som_Hypnosis = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Hypnosis.wav")
som_Lick = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Lick.wav")
som_Stomp = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Stomp.wav")
som_Tackle = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Tackle.wav")
som_Thunder_Shock = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Thunder_Shock.wav")
som_Twister = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/Twister.wav")
som_vitoria = pygame.mixer.Sound("Dados/Recursos/Sprites/SonsPokemon/vitoria.wav")


# Também a gente carrega as fontes, aumentando elas também de acordo com a escala, cada fonte
# tem um tamanho diferente de acordo com nossas necessidades:
fonte = pygame.font.Font("Dados/Recursos/Fontes/joystix monospace.ttf", int(7 * escala))
fonte_txt = pygame.font.Font("Dados/Recursos/Fontes/joystix monospace.ttf", int(8 * escala))
fonte_escolher_move = pygame.font.Font("Dados/Recursos/Fontes/joystix monospace.ttf", int(6 * escala))
