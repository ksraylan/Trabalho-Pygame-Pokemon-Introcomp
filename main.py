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
janela_titulo = "Pokémon"

tela = pygame.display.set_mode(janela_tamanho)

pygame.display.set_caption(janela_titulo)

fonte = pygame.font.Font("Recursos/Fontes/joystix monospace.ttf", 16)

# menu espaçamento:
m_e = (200,50)
# tamanho menu:
t_m = 5
# tamanho seta:
t_s = 25

sel_s = 0
pokemons = ["PIKACHU","CHARMANDER","BULBASAUR","SQUIRTLE", "RHYDON","GENGAR", "DRAGONITE", "MEWTWO"]
cores = [AMARELO, LARANJA, VERDE, AZUL, CIANO, ROXO, ROSA, CINZA]

def desenhar_graficos():
    #menu inicio:
    txt = "Choose your pokémon"
    tela_do_menu = PRETO
    
    
    #limpar a tela:
    tela.fill(PRETO)

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
    """
    pygame.draw.line(tela, BRANCO, m_e, (janela_tamanho[0] - m_e[0], m_e[1]), t_m)
    pygame.draw.line(tela, BRANCO, (), (100,580), 5)
    pygame.draw.line(tela, BRANCO, (100,580), (700,580), 5)
    pygame.draw.line(tela, BRANCO, (700,20), (700,580), 5)
    
    """

    pygame.display.update()


def escolher_pokemon():
    print("funcionou")
    pass

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
        #pygame.K_KP_ENTER
    desenhar_graficos()
    processar_logica()

# Sair do pygame:
pygame.quit()
