# Importações:
# Precisamos importar o pygame para poder carregar as imagens:
import pygame
# E precisamos importar a janela.py para obtermos a largura da janela:
import janela

# Começamos o jogo tocando a música de abertura:
pygame.mixer.music.load('Recursos/Sprites/SonsPokemon/fireRedAbertura.wav')

# A escala do jogo será a largura da janela (800) dividido por 240 (largura da resolução
# original do Gameboy Advanced), que dá 3.333...
# Assim, não teremos tamanho de imagens diferentes um do outro e podemos suportar outras
# resoluções como widescreen se quisermos sem muitos esforços:  
escala = janela.tamanho[0] / 240
# Aqui a gente carrega todas as imagens da interface do jogo:
img_opcoes_batalha = pygame.image.load('Recursos/Sprites/SpritesInterface/fgt_options.png').convert_alpha()
img_barra1 = pygame.image.load('Recursos/Sprites/SpritesInterface/barra_1.png').convert_alpha()
img_barra2 = pygame.image.load('Recursos/Sprites/SpritesInterface/barra_2.png').convert_alpha()
img_barra_sem_vida = pygame.image.load('Recursos/Sprites/SpritesInterface/barra_sem_vida.png').convert_alpha()
img_pp_bar = pygame.image.load('Recursos/Sprites/SpritesInterface/pp_bar.png').convert_alpha()
img_fundo_pokemon = pygame.image.load('Recursos/Sprites/SpritesInterface/FundoPokemon.png').convert_alpha()
img_text_bar = pygame.image.load('Recursos/Sprites/SpritesInterface/text_bar.png').convert_alpha()
img_vida_amarela = pygame.image.load('Recursos/Sprites/SpritesInterface/vida_amarela.png').convert_alpha()
img_vida_vermelha = pygame.image.load('Recursos/Sprites/SpritesInterface/vida_vermelha.png').convert_alpha()
img_bag = pygame.image.load('Recursos/Sprites/SpritesInterface/bag_1.png').convert_alpha()
img_bag_arrow = pygame.image.load('Recursos/Sprites/SpritesInterface/bag_arrow.png').convert_alpha()

# Depois disso a gente aumenta o tamanho deles de acordo com a escala:
img_pp_bar = pygame.transform.scale(img_pp_bar, (int(240*escala), int(48*escala)))
img_vida_amarela = pygame.transform.scale(img_vida_amarela, (int(9*escala), int(3*escala)))
img_vida_vermelha = pygame.transform.scale(img_vida_vermelha, (int(9*escala), int(3*escala)))
img_barra_sem_vida = pygame.transform.scale(img_barra_sem_vida, (int(9*escala), int(3*escala)))
img_bag = pygame.transform.scale(img_bag, (int(240*escala), int(160*escala)))
img_bag_arrow = pygame.transform.scale(img_bag_arrow, (int(20*escala), int(20*escala)))
img_barra1 = pygame.transform.scale(img_barra1, (int(101*escala), int(29*escala)))
img_barra2 = pygame.transform.scale(img_barra2, (int(104*escala), int(39*escala)))
img_opcoes_batalha = pygame.transform.scale(img_opcoes_batalha, (int(120*escala), int(48*escala)))
img_text_bar = pygame.transform.scale(img_text_bar, (int(240*escala), int(48*escala)))
img_fundo_pokemon = pygame.transform.scale(img_fundo_pokemon, (int(240*escala*1), int(112*escala*1.25)))

# Essa função carregará duas imagens, uma do pokémon de frente e outra de costas,
# e retornará as mesmas:
def carregar_imagem_pokemon(numero):
    return [pygame.transform.scale(pygame.image.load("Recursos/Sprites/SpritesPokemon/Frente/{}.png".format(numero)), (int(64*escala), int(64*escala))),
    pygame.transform.scale(pygame.image.load("Recursos/Sprites/SpritesPokemon/Costas/{}.png".format(numero)), (int(64*escala), int(64*escala)))]

# Carregando os efeitos sonoros:
#som_absorb = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Absorb.wav")
som_fire_red_abertura = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/fireRedAbertura.wav")
som_Batalha = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/batalha.wav")
som_Flamethrower = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Flamethrower.wav")
som_Bite = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Bite.wav")
#som_Bubble = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Bubble.wav")
som_Confusion = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Confusion.wav")
#som_Dark_Pulse = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Dark_Pulse.wav")
som_derrota = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/derrota.wav")
som_Dual_Chop = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Dual_Chop.wav")
som_Ember = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Ember.wav")
som_menu_mudou = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/firered_0005.wav")
som_menu_escolheu = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/firered_0030.wav")
som_Hydro_Pump = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Hydro_Pump.wav")
som_Hypnosis = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Hypnosis.wav")
som_Lick = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Lick.wav")
som_Megahorn = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Megahorn.wav")
som_Quick_Attack = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Quick_Attack.wav")
som_Razor = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Razor_Leaf.wav")
som_Recover = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Recover.wav")
som_Stomp = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Stomp.wav")
som_Tackle = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Tackle.wav")
som_Thunder_Shock = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Thunder_Shock.wav")
som_Twister = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Twister.wav")
#som_ViridianCity = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/ViridianCity.mp3")
som_vitoria = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/vitoria.wav")
som_Thunder = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Thunder.wav")

# Também a gente carrega as fontes, aumentando elas também de acordo com a escala, cada fonte
# tem um tamanho diferente de acordo com nossas necessidades:
fonte = pygame.font.Font("./Recursos/Fontes/joystix monospace.ttf", int(7*escala))
fonte_txt = pygame.font.Font("./Recursos/Fontes/joystix monospace.ttf", int(8*escala))
fonte_escolher_move = pygame.font.Font("./Recursos/Fontes/joystix monospace.ttf", int(6*escala))