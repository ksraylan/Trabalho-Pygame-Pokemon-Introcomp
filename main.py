import pygame

# Cores:
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
LARANJA = (255, 153, 0)
CIANO = (0, 255, 255)
ROXO = (102, 0, 102)
ROSA = (255, 102, 255)
CINZA = (128, 128, 128)
# Iniciar o pygame:
pygame.init()

janela_tamanho = (800, 600)
janela_titulo = "Pokemon"

tela = pygame.display.set_mode(janela_tamanho)

pygame.display.set_caption(janela_titulo)

fonte = pygame.font.Font("Recursos/Fontes/joystix monospace.ttf", 16)

fonte_txt = pygame.font.Font("Recursos/Fontes/joystix monospace.ttf", 25)

# menu espaçamento:
m_e = (200,50)
# tamanho menu:
t_m = 5
# tamanho seta:
t_s = 25

sel_s = 0
pokemons = ["PIKACHU","CHARMANDER","BULBASAUR","SQUIRTLE", "RHYDON","GENGAR", "DRAGONITE", "MEWTWO"]
cores = [AMARELO, LARANJA, VERDE, AZUL, CIANO, ROXO, ROSA, CINZA]

cena_atual = "escolher_pokemon"

# Imagens da Interface:
img_opcoes_batalha = pygame.image.load('Recursos/Sprites/SpritesInterface/fgt_options.png').convert_alpha()
img_barra1 = pygame.image.load('Recursos/Sprites/SpritesInterface/barra_1.png').convert_alpha()
img_barra2 = pygame.image.load('Recursos/Sprites/SpritesInterface/barra_2.png').convert_alpha()
img_barra_sem_vida = pygame.image.load('Recursos/Sprites/SpritesInterface/barra_sem_vida.png').convert_alpha()
img_pp_bar = pygame.image.load('Recursos/Sprites/SpritesInterface/pp_bar.png').convert_alpha()
img_fundo_pokemon = pygame.image.load('Recursos/Sprites/SpritesInterface/FundoPokemon.png').convert_alpha()
img_text_bar = pygame.image.load('Recursos/Sprites/SpritesInterface/text_bar.png').convert_alpha()
img_vida_amarela = pygame.image.load('Recursos/Sprites/SpritesInterface/vida_amarela.png').convert_alpha()
img_vida_vermelha = pygame.image.load('Recursos/Sprites/SpritesInterface/vida_vermelha.png').convert_alpha()

# Imagens dos Pokémons:
img_pokemons = []

i = 1
while i <= 386:
    if i == 34:
        i = 35
    elif i == 152:
        i = 216
    if i != 217:
        img_pokemons.append([pygame.image.load(("Recursos/Sprites/SpritesPokemon/Frente/{}.png".format(i))), pygame.image.load(("Recursos/Sprites/SpritesPokemon/Costas/{}.png".format(i)))])
        i += 1
    else:
        img_pokemons.append([pygame.image.load("Recursos/Sprites/SpritesPokemon/Frente/386.png"), pygame.image.load("Recursos/Sprites/SpritesPokemon/Costas/386.png")])
        img_pokemons.append([pygame.image.load("Recursos/Sprites/SpritesPokemon/Frente/386-attack.png"), pygame.image.load("Recursos/Sprites/SpritesPokemon/Costas/386-attack.png")])
        img_pokemons.append([pygame.image.load("Recursos/Sprites/SpritesPokemon/Frente/386-defense.png"), pygame.image.load("Recursos/Sprites/SpritesPokemon/Costas/386-defense.png")])
        img_pokemons.append([pygame.image.load("Recursos/Sprites/SpritesPokemon/Frente/386-normal.png"), pygame.image.load("Recursos/Sprites/SpritesPokemon/Costas/386-normal.png")])
        break


# Sons dos Pokemons:
som_absorb = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Absorb.wav")
som_fire_red_abertura = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/fireRedAbertura.wav")
som_Batalha = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/batalha.wav")
som_Flamethrower = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Flamethrower.wav")
som_Bite = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Bite.wav")
som_Bubble = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Bubble.wav")
som_Confusion = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Confusion.wav")
som_Dark_Pulse = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Dark_Pulse.wav")
som_derrota = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/derrota.wav")
som_Dual_Chop = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Dual_Chop.wav")
som_Ember = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/Ember.wav")
som_firered0005 = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/firered_0005.wav")
som_firered_0030 = pygame.mixer.Sound("Recursos/Sprites/SonsPokemon/firered_0030.wav")
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

escala = 2.25

img_opcoes_batalha = pygame.transform.scale(img_opcoes_batalha, (int(120*escala), int(48*escala)))
img_text_bar = pygame.transform.scale(img_text_bar, (int(240*escala), int(48*escala)))
img_fundo_pokemon = pygame.transform.scale(img_fundo_pokemon, (int(240*escala*1.5), int(112*escala*2.0)))

pos = [0,0]
distanciamento = (50*escala,15*escala)

def desenhar_graficos():
    #menu inicio:
    txt = "Choose your pokémon"
    tela_do_menu = PRETO
    
    
    #limpar a tela:
    tela.fill(PRETO)
    
    if cena_atual == "escolher_pokemon":
        # Fonte:
        superf = fonte.render(txt, True, BRANCO)
        superf_rect = superf.get_rect()
        superf_rect.center =(janela_tamanho[0]/2, 100)
        tela.blit(superf, superf_rect)

        # posicao do nome que está sendo selecionado:
        

        # espacamento entre os nomes:
        e_n = 32
        # posicao y da seta dentro do retangulo:
        li = 100-e_n + (e_n*sel_s)

        # espaçamento x na esquerda da seta:
        e_s_x = 16

        # seta de seleção:
        pygame.draw.polygon(tela, VERMELHO, ( (m_e[0] + e_s_x, m_e[1] + li), (m_e[0] + e_s_x,m_e[1] + t_s + li), (m_e[0] + e_s_x+ t_s/2, m_e[1] + t_s/2 + li) ) )

        # loop que vai percorrer a lista com os nomes dos pokemons:
        for i in range( len(pokemons) ):
            # aqui vamos criar um texto com o pokemon "i" (o "i" que vai até o range do loop):
            superf = fonte.render(pokemons[i], True, cores[i])
            # Pegaremos as dimensões do texto que criamos acima:
            superf_rect = superf.get_rect()
            # Colocaremos no centro, e pegamos o espaçamento e multiplicamos por "i", para os nomes dos pokemons irem para baixo e não ficarem um em cima do outro:
            superf_rect.center =(janela_tamanho[0]/2, 100 + e_n + i*e_n)
            # Por fim, mostraremos na tela o texto:
            tela.blit(superf, superf_rect)
        
        
        #pygame.draw.rect(tela, BRANCO, ( m_e , ((m_e[0]-janela_tamanho[0]),(m_e[1]-janela_tamanho[1]) ) ))
        pygame.draw.rect(tela, BRANCO, ((m_e[0],m_e[1]),(janela_tamanho[0]-(m_e[0]*2),janela_tamanho[1]-(m_e[1]*2))), 5)
    elif cena_atual == "batalha":
        # Cena de batalha:
        #tela.blit(imagem, (x, y))
        tela.blit(img_fundo_pokemon,(0,0))
        
        tela.blit(img_text_bar, (0, janela_tamanho[1] - 48*escala))
        tela.blit(img_opcoes_batalha, (janela_tamanho[0] - 120*escala, janela_tamanho[1] - 48*escala))
        # (x, y)
        
        pygame.draw.rect(tela, VERMELHO, ((janela_tamanho[0] - 107.5*escala + (pos[0]*distanciamento[0]), janela_tamanho[1] - 37.5*escala + (pos[1]*distanciamento[1])), (50*escala,15*escala)), int(1*escala))
        nome_na_batalha = "What should KADABRA do?"
        batalha_nome = fonte_txt.render(nome_na_batalha, True, BRANCO)
        batalha_rect = batalha_nome.get_rect()
        batalha_rect.left = 0 + 16*escala
        batalha_rect.bottom = janela_tamanho[1] - 25*escala

        tela.blit(batalha_nome, batalha_rect)

    pygame.display.update()


def escolher_pokemon():
    global cena_atual
    cena_atual = "batalha"

#características do pokémon:
class Pokemon:
    def __init__(self, nome, vida, força):
        self.__nome = nome
        self.__vida = vida
        self.__força = força
    
    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @property
    def força(self):
        return self.__força

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @vida.setter
    def vida(self,vida):
        self.__vida = vida
        
    @força.setter
    def força(self,força):
        self.__força = força

    def batalha(self,ataque,outro_pokemon):
        outro_pokemon.vida -= ataque
        pass
    
        
    
def processar_logica():
    pass

rodando_o_jogo = True

# Loop do jogo:
while rodando_o_jogo == True:
    # Eventos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando_o_jogo = False
        # Se uma tecla foi pressionada:
        if event.type == pygame.KEYDOWN:
            if cena_atual == "batalha":
                if event.key == pygame.K_UP:
                    pos[1] = 0
                elif event.key == pygame.K_DOWN:
                    pos[1] = 1
                elif event.key == pygame.K_LEFT:
                    pos[0] = 0
                elif event.key == pygame.K_RIGHT:
                    pos[0] = 1
            elif cena_atual == "escolher_pokemon":
                if event.key == pygame.K_UP:
                    sel_s = sel_s - 1
                    if sel_s < 0:
                        sel_s = 0
                elif event.key == pygame.K_DOWN:
                    sel_s = sel_s + 1
                    if sel_s > len(pokemons) - 1:
                        sel_s = len(pokemons) - 1
                elif event.key == pygame.K_RETURN:
                    escolher_pokemon()
        
    desenhar_graficos()
    processar_logica()

# Sair do pygame:
pygame.quit()
