# Importações:
import random
from math import ceil, floor
import pygame
import janela
from moves import Moves
from poke_types import Types
from pokemon import Pokemon
import arquivos as arq
import cores as cor
import cena
from mensagem import Mensagem
from condicao import Condicao
from acoes import Acao
from tempo import Tempo
from posicao import Pos
from effect import Effect
from category import Category
from itens import Itens
from processar_movimentos import process_moves

# Aqui 
def main():
    
    itens = Itens()
    category = Category()
    effect = Effect()
    menu = cena.Menu()
    sub_menu = cena.Submenu()
    mensagem = Mensagem()
    escala = arq.escala
    # menu espaçamento:
    menu_espacamento = (200,100)
    # tamanho menu:
    #menu_tamanho = 2*escala
    # tamanho seta:
    tamanho_cursor = 11*escala
    # Pokémon selecionado (na tela de seleção de pokémon):
    #sel_s = 0
    pos = Pos(1, 8)
    distanciamento = (50*escala,15*escala) # distanciamento entre as opções de escolha
    # Os gêneros para cada pokémon:
    generos = ["F", "M"]
    clock = pygame.time.Clock()
    condicao = Condicao()
    tipos = Types()
    moves = Moves()

    # Lista com os itens que cada pokémon irá ter:
    itens_usados = [itens.dire_hit, itens.guard_spec, itens.x_accuracy, itens.x_attack, itens.x_defense,
    itens.x_special, itens.x_speed, itens.berry_juice, itens.elixir, itens.potion]

    pk_pikachu = Pokemon("Pikachu",35,55,40,90,50,50,15,random.choice(generos),
    [tipos.normal],[moves.growl, moves.thunder_shock, moves.tail_whip, moves.thunder_wave],itens_usados.copy(), arq.carregar_imagem_pokemon(25))
    
    pk_charmander = Pokemon("Charmander",39,52,43,65,60,50,15, random.choice(generos),
    [tipos.fire],[moves.growl, moves.scratch, moves.ember, moves.metal_claw],itens_usados.copy(), arq.carregar_imagem_pokemon(4))
    pk_bulbasaur = Pokemon("Bulbasaur",45,49,49,45,65,65,15, random.choice(generos),
    [tipos.grass, tipos.poison],[moves.tackle, moves.growl, moves.leech_seed, moves.vine_whip],itens_usados.copy(),arq.carregar_imagem_pokemon(1))
    pk_squirtle = Pokemon("Squirtle",44,48,65,43,50,64, 15,random.choice(generos),
    [tipos.water], [moves.tackle, moves.tail_whip, moves.bubble, moves.withdraw],itens_usados.copy(), arq.carregar_imagem_pokemon(7))
    pk_rhydon = Pokemon("Rhydon",105,130,120,40,45,45,15,random.choice(generos),
    [tipos.ground, tipos.rock],[moves.fury_attack, moves.horn_attack, moves.stomp, moves.tail_whip],itens_usados.copy(), arq.carregar_imagem_pokemon(112))
    pk_gengar = Pokemon("Gengar",60,65,60,110,130,75,15,random.choice(generos), [tipos.ghost, tipos.poison],
    [moves.hypnosis, moves.lick, moves.spite, moves.curse],itens_usados.copy(), arq.carregar_imagem_pokemon(94))
    pk_dragonite = Pokemon("Dragonite",91,134,95,80,100,100,15, random.choice(generos),
    [tipos.dragon, tipos.flying], [moves.leer, moves.thunder_wave, moves.twister, moves.wrap],itens_usados.copy(), arq.carregar_imagem_pokemon(149))
    pk_mewtwo = Pokemon("Mewtwo",106,110,90,130,154,90,15,random.choice(generos),
    [tipos.psychic], [moves.confusion, moves.disable, moves.barrier, moves.mist],itens_usados.copy(), arq.carregar_imagem_pokemon(150))
    
    # Lista com os pokémons que podem ser escolhidos na tela de seleção de pokémon e suas cores abaixo.
    pokemons_pode_escolher = [pk_pikachu, pk_charmander, pk_bulbasaur, pk_squirtle, pk_rhydon, pk_gengar, pk_dragonite, pk_mewtwo]
    cores_pode_escolher = [cor.AMARELO, cor.LARANJA, cor.VERDE, cor.AZUL, cor.CIANO, cor.ROXO, cor.ROSA, cor.CINZA]

    # Começará com nenhum pokémon selecionado:
    pokemons = [None, None]

    def texto_multilinha(texto):
        x = 0
        y = 0
        # s = onde está o último espaço " " 
        s = 0
        i = 0
        t = []
        while i < mensagem.texto_posicao:
            t_local = arq.fonte_txt.render(texto[i], False, cor.BRANCO)
            t_rect = t_local.get_rect()
            coordenada_x = 0 + 12*escala + t_rect.width*x
            if texto[i] == " ":
                s = i
            if coordenada_x > janela.tamanho[0]/2 - t_rect.width:
                x = 0
                y -= 1
                for _ in range(i, s, -1):
                    if s < len(t):
                        t.pop(s)
                i = s + 1 
                s = 0
                coordenada_x = 0 + 12*escala + t_rect.width*x
                t_local = arq.fonte_txt.render(texto[i], False, cor.BRANCO)
            t_rect.left = coordenada_x
            t_rect.bottom = janela.tamanho[1] - 28*escala - y*t_rect.height
            t.append([t_local, t_rect])
            x += 1
            i += 1
        for i in range(len(t)):
            janela.tela.blit(t[i][0], t[i][1])

    pygame.mixer.music.play(-1)
    
    barra_width = arq.img_vida_vermelha.get_width() * 5.34

    def tocar_musica(caminho, repetir):
        # caminho: qual o caminho que leva até o arquivo da música
        # Para a música (se estiver tocando alguma):
        pygame.mixer.music.stop()
        # Carrega a música pelo caminho
        pygame.mixer.music.load(caminho)
        # Começa a tocar a música:
        if repetir:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()

    def tocar_sons():
        if condicao.atual == condicao.vitoria:
            arq.som_vitoria.play()
        if condicao.atual == condicao.derrota:
            arq.som_derrota.play()

    width_dividido = janela.tamanho[0]/2
    # espaçamento x na esquerda da seta:
    e_s_x = 16
    # espacamento entre os nomes:
    e_n = 32

    def barra_sem_vida_calculo_escala(x, width):
        x = int(x)
        width = int(width)
        if x + width <= ceil(102.6*escala):
            width += 1

        return x, width

    def obter_id_bloqueados(pokemon):
        id_bloqueados = []
        for i in range(len(pokemon.movimentos_bloqueados)):
            # obteremos somente a id do movimento para depois comparar com "in":
            id_bloqueados.append(pokemon.movimentos_bloqueados[i][0])
        return id_bloqueados

    def desenhar_graficos():
        #limpar a tela:
        janela.tela.fill(cor.PRETO)      
        if menu.no_menu(menu.escolhendo_pokemon):
            # Fonte:
            superf = arq.fonte.render("Escolha o seu pokémon", False, cor.BRANCO)
            superf_rect = superf.get_rect()
            superf_rect.center =(width_dividido, 20*escala)
            janela.tela.blit(superf, superf_rect)

            # posicao do nome que está sendo selecionado:
            
            # posicao y da seta dentro do retangulo:
            #li = 100-e_n + (e_n*sel_s)
            li = tamanho_cursor/2 + (e_n*pos.y)

            # seta de seleção:
            pygame.draw.polygon(janela.tela, cor.VERMELHO, ((menu_espacamento[0] + e_s_x,
            menu_espacamento[1] + li), (menu_espacamento[0] + e_s_x,menu_espacamento[1] +
            tamanho_cursor + li), (menu_espacamento[0] + e_s_x+ tamanho_cursor/2,
            menu_espacamento[1] + tamanho_cursor/2 + li)))
            
            # loop que vai percorrer a lista com os nomes dos pokemons:
            for i in range( len(pokemons_pode_escolher) ):
                # aqui vamos criar um texto com o pokemon "i" (o "i" que vai até o range do loop):
                superf = arq.fonte.render(pokemons_pode_escolher[i].nome, False,
                cores_pode_escolher[i])
                # Pegaremos as dimensões do texto que criamos acima:
                superf_rect = superf.get_rect()
                # Colocaremos no centro, e pegamos o espaçamento e multiplicamos por "i",
                # para os nomes dos pokemons irem para baixo e não ficarem um em cima do outro:
                superf_rect.center =(janela.tamanho[0]/2, 100 + e_n + i*e_n)
                # Por fim, mostraremos na tela o texto:
                janela.tela.blit(superf, superf_rect)
            
            
            #pygame.draw.rect(tela, BRANCO, ( m_e , ((m_e[0]-janela.tamanho[0]),(m_e[1]-janela.tamanho[1]) ) ))
            pygame.draw.rect(janela.tela, cor.BRANCO, ((menu_espacamento[0],menu_espacamento[1]),(janela.tamanho[0]-(menu_espacamento[0]*2),janela.tamanho[1]-(menu_espacamento[1]*2))), 5)
        elif menu.no_menu(menu.batalhando):
            
            if sub_menu.no_submenu(sub_menu.itens):
                # Sub menu: itens
                janela.tela.blit(arq.img_bag, (0, (janela.tamanho[1] - arq.img_bag.get_height())/2))

                esp = 16*escala

                # Desenhando os nomes dos itens (temos que limitar a 5, fazer sistema de "páginas"):
                
                limite = 5

                # sistema de descer e subir a "página":
                # Se a seta passou do último item da "página":
                while pos.y >= limite + pos.offset:
                    pos.offset += 1
                # Se a seta está antes do primeiro item da "página":
                while pos.y < pos.offset:
                    pos.offset -= 1
                i = pos.offset
                while i < len(pokemons[0].itens)+1:
                    
                    texto = "Cancel"
                    if not i == 0:
                        texto = pokemons[0].itens[i-1][1]
                    item_txt = arq.fonte.render(texto, False, cor.PRETO)
                    item_txt_rect = item_txt.get_rect()
                    item_txt_rect.bottomleft =(100*escala, 30*escala + ((i-pos.offset)*esp  ))
                    
                    janela.tela.blit(item_txt, item_txt_rect)
                    i +=1
                    if not i < limite + pos.offset:
                        break
                # Desenhando a seta de seleção:
                li = tamanho_cursor/2 + (esp*(pos.y-pos.offset))

                seta_x = 30*escala

                # seta de seleção:
                pygame.draw.polygon(janela.tela, cor.PRETO, ((menu_espacamento[0] + seta_x,
                esp + li), (menu_espacamento[0] + seta_x,esp +
                tamanho_cursor + li), (menu_espacamento[0] + seta_x+ tamanho_cursor/2,
                esp + tamanho_cursor/2 + li)))


            else: 
                # Cena de batalha:
                janela.tela.blit(arq.img_fundo_pokemon,(0,0))
                
                # img_pokemons[n_do_pokemon][0 = frente, 1 = costas]
                # pokemon inimigo:
                if not pokemons[1].sumido:
                    janela.tela.blit(pokemons[1].imagem_frente, (janela.tamanho[0] - 100*escala + pokemons[1].deslocamento[0] * escala,20*escala  + pokemons[1].deslocamento[1] * escala))
                # seu pokemon:
                if not pokemons[0].sumido:
                    janela.tela.blit(pokemons[0].imagem_costas, (25*escala  + pokemons[0].deslocamento[0] * escala,janela.tamanho[1] - 95*escala + pokemons[0].deslocamento[1] * escala))
                
                # Menus:
                janela.tela.blit(arq.img_text_bar, (0, janela.tamanho[1] - 48*escala))
                if sub_menu.no_submenu(sub_menu.principal):
                    janela.tela.blit(arq.img_opcoes_batalha, (janela.tamanho[0] - 120*escala, janela.tamanho[1] - 48*escala))
                    

                    # desenhando a seta
                    ly = (distanciamento[1]*pos.y)
                    lx = (distanciamento[0]*pos.x)

                    pos_inicial = (janela.tamanho[0] - 110*escala, janela.tamanho[1] - 35*escala)
                    
                    pygame.draw.polygon(janela.tela, cor.PRETO, ((pos_inicial[0] + lx,
                    pos_inicial[1] + ly), (pos_inicial[0] + lx,pos_inicial[1] +
                    tamanho_cursor + ly), (pos_inicial[0] + tamanho_cursor/2 + lx,
                    pos_inicial[1] + tamanho_cursor/2 + ly)))

                elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                    janela.tela.blit(arq.img_pp_bar, (0, janela.tamanho[1] - 48*escala))
                    x = 0
                    espac_x = janela.tamanho[0]/2 - janela.tamanho[0]/5
                    espac_y = 13*escala
                    y = 0
                    for i in range(len(pokemons[0].movimentos)):
                        id_movimento = pokemons[0].movimentos[i][0]
                        nome_movimento = pokemons[0].movimentos[i][1]
                        id_bloqueados = obter_id_bloqueados(pokemons[0])
                        if not id_movimento in id_bloqueados:
                            superf = arq.fonte_escolher_move.render(str(nome_movimento), False, cor.PRETO)
                        else:
                            superf = arq.fonte_escolher_move.render(str(nome_movimento), False, cor.VERMELHO)

                        
                        superf_rect = superf.get_rect()
                        superf_rect.topleft =(15*escala + (espac_x*x), janela.tamanho[1] - (36*escala) + (espac_y * y))
                        
                        janela.tela.blit(superf, superf_rect)
                        x += 1
                        if x >= 2:
                            x = 0
                            y += 1
                    #pygame.draw.rect(janela.tela, cor.VERMELHO, ((10*escala + (espac_x*pos.x)), (janela.tamanho[1] - (30*escala) + (espac_y * pos.y) ), (espac_x), (espac_y)), int(1*escala))
                    
                    # desenhando a seta
                    ly = (espac_y*pos.y)
                    lx = (espac_x*pos.x)

                    pos_inicial = (7*escala, janela.tamanho[1] - 35*escala)
                    tam = 7.2*escala                
                    pygame.draw.polygon(janela.tela, cor.PRETO, ((pos_inicial[0] + lx,
                    pos_inicial[1] + ly), (pos_inicial[0] + lx,pos_inicial[1] +
                    tam + ly), (pos_inicial[0] + tam/2 + lx,
                    pos_inicial[1] + tam/2 + ly)))


                    # Mostrando o PP atual:
                    txt_pp = arq.fonte_txt.render(str(pokemons[0].movimentos[pos.i][2]), False, cor.PRETO)
                    txt_pp_rect = txt_pp.get_rect()
                    txt_pp_rect.bottomright =(janela.tamanho[0] - 27.5*escala, janela.tamanho[1] - 27.5*escala)
                    
                    janela.tela.blit(txt_pp, txt_pp_rect)
                    # Mostrando o PP máximo:
                    txt_pp_maximo = arq.fonte_txt.render(str(pokemons[0].movimentos[pos.i][3]), False, cor.PRETO)
                    txt_pp_maximo_rect = txt_pp_maximo.get_rect()
                    txt_pp_maximo_rect.bottomleft =(janela.tamanho[0] - 19*escala, janela.tamanho[1] - 27.5*escala)
                    
                    janela.tela.blit(txt_pp_maximo, txt_pp_maximo_rect)

                    # Mostrando o tipo do movimento:
                    txt_move = arq.fonte_escolher_move.render(str(pokemons[0].movimentos[pos.i][7]), False, cor.PRETO)
                    txt_move_rect = txt_move.get_rect()
                    txt_move_rect.bottomleft =(janela.tamanho[0] - 47.5*escala, janela.tamanho[1] - 10*escala)
                    
                    janela.tela.blit(txt_move, txt_move_rect)
                # Desenhando as barras:
                if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                    janela.tela.blit(arq.img_barra1, (15*escala, 18*escala))
                if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                    janela.tela.blit(arq.img_barra2, (janela.tamanho[0] - 110*escala,janela.tamanho[1] - 88*escala))
                # Nomes dos pokemons renderizados na barra:
                
                poke_2 = arq.fonte.render(pokemons[1].nome, False, cor.PRETO)
                poke_2_rect = poke_2.get_rect()
                poke_2_rect.center =(48.5*escala, 25*escala)
                if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                    janela.tela.blit(poke_2, poke_2_rect)

                poke_1 = arq.fonte.render(pokemons[0].nome, False, cor.PRETO)
                poke_1_rect = poke_1.get_rect()
                poke_1_rect.center =((janela.tamanho[0] - 68*escala), janela.tamanho[1] - 77.5*escala)
                if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                    janela.tela.blit(poke_1, poke_1_rect)

                texto = ""
                a_cor = cor.PRETO

                if pokemons[0].genero == "F":
                    texto, a_cor = "♀", cor.ROSA
                elif pokemons[0].genero == "M":
                    texto, a_cor = "♂", cor.AZUL
                simb_1 = arq.fonte.render(texto, False, a_cor)
                simb_1_rect = simb_1.get_rect()
                simb_1_rect.left = poke_1_rect.width + poke_1_rect.x
                simb_1_rect.top = poke_1_rect.y
                if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                    janela.tela.blit(simb_1, simb_1_rect)

                
                texto = ""
                a_cor = cor.PRETO

                if pokemons[1].genero == "F":
                    texto, a_cor = "♀", cor.ROSA
                elif pokemons[1].genero == "M":
                    texto, a_cor = "♂", cor.AZUL
                simb_2 = arq.fonte.render(texto, False, a_cor)
                simb_2_rect = simb_2.get_rect()
                simb_2_rect.left = poke_2_rect.width + poke_2_rect.x
                simb_2_rect.top = poke_2_rect.y
                if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                    janela.tela.blit(simb_2, simb_2_rect)            

                # Pokémon inimigo:
                if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                    # Barra de vida amarela:
                    if pokemons[1].vida_maxima/5 < pokemons[1].vida_anim <= pokemons[1].vida_maxima/2:
                        img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela,
                        (int(arq.img_vida_amarela.get_width() + (escala*39)),
                        arq.img_vida_vermelha.get_height()))
                        
                        janela.tela.blit(img_vida_amarela_esticada,(55*escala, 34*escala))
                    # Vida vermelha:
                    if pokemons[1].vida_anim <= pokemons[1].vida_maxima/5:
                        img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha,
                        (int(arq.img_vida_vermelha.get_width() + (escala*39)),
                        arq.img_vida_vermelha.get_height()))
                        
                        janela.tela.blit(img_vida_vermelha_esticada,(55*escala, 34*escala))
                    # "Vida vazia":
                    x, width = barra_sem_vida_calculo_escala(55*escala +
                    barra_width * (pokemons[1].vida_anim/pokemons[1].vida_maxima) , (arq.img_barra_sem_vida.get_width() + (escala*39)) *
                    (pokemons[1].vida_maxima - pokemons[1].vida_anim)/pokemons[1].vida_maxima)
                    img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida,
                    (width,
                    arq.img_barra_sem_vida.get_height()))

                    janela.tela.blit(img_barra_sem_vida_esticada,(x, 34*escala))

                    # Mostrando o nível do pokémon:
                    nivel = arq.fonte_escolher_move.render(str(pokemons[1].nivel), False, cor.PRETO)
                    nivel_rect = nivel.get_rect()
                    nivel_rect.topleft = (96*escala,23*escala)
                    janela.tela.blit(nivel, nivel_rect)

                if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                    # Barra de vida amarela:
                    if pokemons[0].vida_anim <= pokemons[0].vida_maxima/2:
                        img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela,
                        (int(arq.img_vida_amarela.get_width() + (escala*39)),
                        arq.img_vida_vermelha.get_height()))
                        
                        janela.tela.blit(img_vida_amarela_esticada,(janela.tamanho[0]-62*escala,
                        janela.tamanho[1] - 69*escala))
                    # Vida vermelha:
                    if pokemons[0].vida_anim <= pokemons[0].vida_maxima/5:
                        img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha,
                        (int(arq.img_vida_vermelha.get_width() + (escala*39)),
                        arq.img_vida_vermelha.get_height()))
                        
                        janela.tela.blit(img_vida_vermelha_esticada,(janela.tamanho[0] -
                        62*escala,janela.tamanho[1] - 69*escala))
                    # "Vida vazia":
                    img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida,
                    (round((arq.img_barra_sem_vida.get_width() + (escala*39)) *
                    (pokemons[0].vida_maxima - pokemons[0].vida_anim)/pokemons[0].vida_maxima),
                    arq.img_barra_sem_vida.get_height()))
                    
                    janela.tela.blit(img_barra_sem_vida_esticada,(floor(janela.tamanho[0] -
                    62*escala + barra_width * (pokemons[0].vida_anim/pokemons[0].vida_maxima)),
                    janela.tamanho[1] - 69*escala))
                    # Mostrando o nível do pokémon:
                    nivel = arq.fonte_escolher_move.render(str(pokemons[0].nivel), False, cor.PRETO)
                    nivel_rect = nivel.get_rect()
                    nivel_rect.left = janela.tamanho[0] - 21*escala
                    nivel_rect.top = janela.tamanho[1] - 80*escala
                    janela.tela.blit(nivel, nivel_rect)

                    # Mostrando o número da vida:
                    txt_vida = arq.fonte.render(str(pokemons[0].vida) + "/" + str(pokemons[0].vida_maxima), False, cor.PRETO)
                    txt_vida_rect = txt_vida.get_rect()
                    txt_vida_rect.bottomright =(janela.tamanho[0] - 20*escala, janela.tamanho[1] - 55*escala)
                    
                    janela.tela.blit(txt_vida, txt_vida_rect)
                
                if not sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                    texto_multilinha(mensagem.texto)
                #janela.tela.blit(batalha_nome, batalha_rect)

        pygame.display.update()


    def escolher_pokemon(menu, sub_menu, mensagem):
        menu.atual = menu.batalhando
        sub_menu.atual = sub_menu.principal
        # seu pokémon:
        pokemons[0] = pokemons_pode_escolher[pos.i].copy()
        # pokémon inimigo aleatório:
        pokemons[1] = pokemons_pode_escolher[random.randrange(0,len(pokemons_pode_escolher))].copy()
        
        mensagem.texto = "O que {} deve fazer?".format(pokemons[0].nome)

        pos_2x2()
        
        

    def pos_2x2():
        pos.i = 0
        pos.width = 2
        pos.height = 2
    def pos_menu_principal():
        pos.i = 0
        pos.width = 1
        pos.height = len(pokemons_pode_escolher)
    
    def escolher_acao_batalha(pos):
        if pos.i == 0:
            pos_2x2()
            sub_menu.atual = sub_menu.escolhendo_ataque
        elif pos.i == 1:
            sub_menu.atual = sub_menu.itens
            pos.i = 0
            pos.width = 1
            pos.height = len(pokemons[0].itens) + 1
        elif pos.i == 3:
            fazer_acao(menu, sub_menu, moves.fugir, category.normal_move)
    
    # Remover turnos que ficaram pendentes quando a partida acaba:
    def remover_todos_turnos():
        for i in range(len(turnos)):
            turnos.pop(0)
    
    turnos = []

    def fazer_acao(menu, sub_menu, movimento, categoria):
        # Aqui primeiro vemos qual pokémon fazerá suas ações primeiro:
        # Primeiro a gente pega um número aleatório
        vez = random.randrange(0,1)
        # Agora, se o pokémon "0" (seu pokémon) tiver maior velocidade que o
        # pokémon "1" (pokémon inimigo), então o seu pokémon será o primeiro:
        if pokemons[0].velocidade > pokemons[1].velocidade:
            # Colocamos como primeiro o pokémon "0":
            vez = 0
        # Mas se seu pokémon tiver menor velocidade que o pokémon inimigo:
        elif pokemons[0].velocidade < pokemons[1].velocidade:
            # O primeiro será o pokémon "1":
            vez = 1
        # Agora, se os dois tiverem a mesma velocidade, então nem o if e o elif serão
        # executados, aí o primeiro será aleatório, pois antes do if colocamos um random
        # de aleatório.

        #quick attack priority +1
        #move = movimento[0]
        
        # Seu pokémon primeiro vai executar os movimentos de estado que acontecem
        # antes dos movimentos dele em si:
        print(vez)

        # [pokemon "0", pokemon "1"]:
        categorias_pokemons = [categoria, category.normal_move]
        movimentos_pokemons = [movimento, randomizar_acao(pokemons[1])]

        turnos.append([pokemons[vez], pokemons[vez-1], True, category.state_move])
        # Agora será adicionado aos turnos o movimento em si:
        turnos.append([pokemons[vez], pokemons[vez-1], movimentos_pokemons[vez], categorias_pokemons[vez]])
        # E agora os movimentos de estado que acontecem depois do movimento do pokémon em si:
        turnos.append([pokemons[vez], pokemons[vez-1], False, category.state_move])

        # Agora a mesma coisa, só que agora com o pokémon inimigo:
        turnos.append([pokemons[vez-1], pokemons[vez], True, category.state_move])
        # Aqui será um movimento aleatório do inimigo:
        turnos.append([pokemons[vez-1], pokemons[vez], movimentos_pokemons[vez-1], categorias_pokemons[vez-1]])
        # E a ação de estado depois do movimento:
        turnos.append([pokemons[vez-1], pokemons[vez], False, category.state_move])

        # Coloca a seta poder se locomover a partir de um espaço 2 de largura e 2 de altura (2 x 2)
        pos_2x2()
        # Coloca o sub menu atual sendo o principal:
        sub_menu.atual = sub_menu.principal

    def randomizar_acao(pokemon):
        # Aqui terá o código da "inteligência artificial":
        a_random = pokemon.movimentos[random.randrange(0, len(pokemon.movimentos))]
        return a_random

    
    tempo = Tempo(1000)

    def processar_logica(delta, tempo, menu, sub_menu):

        if menu.atual == menu.batalhando:

            # animação texto:
            tempo.mensagem_tempo += delta
            
            pokemons[0].atualiza_vida_anim(delta)
            pokemons[1].atualiza_vida_anim(delta)
            
            if tempo.mensagem_tempo > 25:
                tempo.mensagem_tempo -= 25
                if mensagem.texto_posicao < len(mensagem.texto):
                    mensagem.texto_deslocar_uma_posicao()

            tempo.adicionar(delta)
            # animação sumindo:
            if tempo.sumido_tempo >= 75:
                if pokemons[1].sumindo:
                    pokemons[1].inverte_sumido()
                elif pokemons[0].sumindo:
                    pokemons[0].inverte_sumido()
                tempo.sumido_tempo -= 75
            tempo.sumido_tempo += delta

            # animação pokémon aqui

            if pokemons[1].foi_derrotado():
                # deslocamento: [0] = x, [1] = y
                pokemons[1].deslocamento[1] += 0.4 * delta
            if pokemons[1].conseguiu_fugir():
                pokemons[1].deslocamento[0] += 0.4 * delta

            if pokemons[0].foi_derrotado():
                # deslocamento: [0] = x, [1] = y
                pokemons[0].deslocamento[1] += 0.4 * delta
            if pokemons[0].conseguiu_fugir():
                pokemons[0].deslocamento[0] -= 0.4 * delta

            if tempo.milisegundos >= 1000 * 1: # 1000 milisegundos vezes os segundos
                if not sub_menu.no_submenu(sub_menu.derrota) and not sub_menu.no_submenu(sub_menu.vitoria):
                    if pokemons[0].foi_derrotado() or pokemons[0].conseguiu_fugir():
                        sub_menu.atual = sub_menu.fazendo_acoes
                        mensagem.texto = "{} ganhou a batalha".format(pokemons[1].nome)
                        remover_todos_turnos()
                        sub_menu.atual = sub_menu.derrota
                        tocar_musica("Recursos/Sprites/SonsPokemon/derrota.wav", False)

                    elif pokemons[1].foi_derrotado() or pokemons[1].conseguiu_fugir():
                        
                        sub_menu.atual = sub_menu.fazendo_acoes
                        mensagem.texto = "{} ganhou a batalha".format(pokemons[0].nome)
                        remover_todos_turnos()
                        sub_menu.atual = sub_menu.vitoria
                        tocar_musica("Recursos/Sprites/SonsPokemon/vitoria.wav", False)
                    else:
                        if len(turnos) > 0:
                            pos_2x2()
                            sub_menu.atual = sub_menu.fazendo_acoes
                            process_turns(turnos, mensagem, tempo)
                        else:
                            if sub_menu.atual == sub_menu.fazendo_acoes:
                                if pokemons[0].bloqueado:
                                    # Fazer nada se seu pokémon estiver bloqueado:
                                    fazer_acao(menu, sub_menu, None, None)
                                    sub_menu.atual = sub_menu.fazendo_acoes
                                else:
                                    mensagem.texto = "O que {} deve fazer?".format(pokemons[0].nome)
                                    sub_menu.atual = sub_menu.principal
                                    pos_2x2()
                
                else:
                    tempo.fim_de_jogo_tempo += delta

                    if tempo.fim_de_jogo_tempo >= 5000:
                        menu.atual = menu.escolhendo_pokemon
                        
                        sub_menu.atual = sub_menu.principal
                        tocar_musica("Recursos/Sprites/SonsPokemon/fireRedAbertura.wav", True)
                        tempo.fim_de_jogo_tempo = 0
                        pos_menu_principal()
    
    def process_turns(turnos, mensagem, tempo):

        def remover_turno(ir_logo_pro_proximo = False):
            if len(turnos) > 0:
                turnos.pop(0)
            tempo.etapa_turno_reseta()
            # Se quer ir logo pro próximo turno sem atraso:
            if ir_logo_pro_proximo:
                # no final os turnos vão estar vazios, aí vai dar erro se tentar acessar algum
                # item da lista de turnos, então só vamos ir pro próximo turno se ainda estiver
                # turnos pendentes:
                if len(turnos) > 0:
                    process_turns(turnos, mensagem, tempo)

        pokemon_a_fazer = turnos[0][0] # pokemon que vai usar a ação
        pokemon_a_tomar = turnos[0][1] # pokémon que vai sofrer da ação
        move = turnos[0][2] # qual movimento vai ser realizado (id, nome do movimento);
        #Quando for movimento de estado, será True ou false.
        turn_category = turnos[0][3] # pega qual categoria é (movimento normal ou de estado)

        # Só faz o movimento se o pokémon não estiver bloqueado:
        if not move == None and not pokemon_a_fazer.bloqueado:
            if turn_category["id"] == category.state_move["id"]:
                if tempo.etapa_turno == 0:
                    mensagens = pokemon_a_fazer.process_effects(move, pokemon_a_tomar)
                    # Se tiver mensagens significa que aconteceu algum efeito:
                    if len(mensagens) > 0:
                        mensagem.texto = mensagens[0]
                        tempo.etapa_turno_incrementa()
                    else:
                        # Se não, então não teve, então já podemos remover e ir logo pro próximo turno:
                        remover_turno(True)
                elif tempo.etapa_turno == 1:
                    remover_turno()
            elif turn_category["id"] == category.normal_move["id"]:
                # Percorrer toda a lista de movimentos até achar o movimento certo e obter seu pp
                for i in range (len(pokemon_a_fazer.movimentos)):
                    if pokemon_a_fazer.movimentos[i][0] == move[0]:
                        move_pokemon = pokemon_a_fazer.movimentos[i]
                        break
                
                # atualiza qual foi o ultimo movimento usado desse pokémon:
                # move[0]: id
                pokemon_a_fazer.ultimo_movimento_id = move[0] 
                if tempo.etapa_turno == 0:
                    if move == moves.fugir[0]:
                        mensagem.texto = "{} tentou fugir".format(pokemon_a_fazer.nome)
                    mensagem.texto = "{} usou {}".format(pokemon_a_fazer.nome, str(move[1]))
                    tempo.etapa_turno_incrementa()
                elif tempo.etapa_turno == 1:
                    # animação básica
                    pokemon_a_tomar.sumindo = True
                    tempo.etapa_turno_incrementa()
                elif tempo.etapa_turno == 2:
                    # desativa a animação básica
                    pokemon_a_tomar.sumindo = False
                    # processa o movimento atual
                    if not move_pokemon[2] <= 0: 
                        move_pokemon[2] -= 1
                        process_moves(pokemon_a_fazer, pokemon_a_tomar, move[0], mensagem, moves, tipos, effect)
                    else:
                        mensagem.texto = "mas não teve mais pp suficiente"
                    tempo.etapa_turno_incrementa()
                # a última etapa é tirar o movimento que acabou de ser feito da lista
                # de movimentos:
                elif tempo.etapa_turno == 3:
                    remover_turno()
            elif turn_category["id"] == category.item_move["id"]:
                if tempo.etapa_turno == 0:
                    mensagem.texto = "{} usou o item {}".format(pokemon_a_fazer.nome, str(move[1]))
                    tempo.etapa_turno_incrementa()
                elif tempo.etapa_turno == 1:
                    # animação de consumo do item (não sei se vamos fazer)
                    tempo.etapa_turno_incrementa()
                elif tempo.etapa_turno == 2:
                    usar_item(pokemon_a_fazer, pokemon_a_tomar, move[0])
                    tempo.etapa_turno_incrementa()
                else:
                    remover_turno()
            else:
                remover_turno()
        else:
            remover_turno()
        # resetar o tempo:
        tempo.resetar()  

    def usar_item(pokemon_a_usar, pokemon_inimigo, item): # PRONTO
        if item == itens.dire_hit[0]: #Aumenta a proporção de acertos críticos de Pokémon em batalha
            pokemon_a_usar.ataque_critico += 1
            mensagem.texto = "{} aumentou a proporção de ataque crítico".format(pokemon_a_usar.nome)
            
        elif item == itens.guard_spec[0]: #Um item que impede a redução de estatísticas 
            pokemon_a_usar.protegido = 3
            mensagem.texto = "{} tem seus dados protegidos por 3 turnos".format(pokemon_a_usar.nome)

        elif item == itens.x_accuracy[0]: #Aumenta a estatística de precisão do Pokémon em batalha
            pokemon_a_usar.precisao += 1
            mensagem.texto = "{} aumentou a precisão em 1 estágio".format(pokemon_a_usar.nome)

            
        elif item == itens.x_attack[0]: #Aumenta a estatística ataque do Pokémon na batalha
            pokemon_a_usar.ataque += 1
            mensagem.texto = "{} aumentou seu ataque em 1 estágio".format(pokemon_a_usar.nome)

        elif item == itens.x_defense[0]: #Aumenta a estatística DEFESA do Pokémon em batalha
            pokemon_a_usar.defesa += 1
            mensagem.texto = "{} aumentou sua defesa em 1 estágio".format(pokemon_a_usar.nome)
        
        elif item == itens.x_special[0]: #Eleva a estatística do ataque especial
            pokemon_a_usar.especial_ataque += 1
            mensagem.texto = "{} aumentou seu ataque especial em 1 estágio".format(pokemon_a_usar.nome)

        elif item == itens.x_speed[0]: #Aumenta a estatística de VELOCIDADE do Pokémon na batalha
            pokemon_a_usar.velocidade += 1
            mensagem.texto = "{} aumentou sua velocidade em 1 estágio".format(pokemon_a_usar.nome)
        
        elif item == itens.berry_juice[0]: #Um suco 100% puro. Ele restaura o HP de um Pokémon em 20 pontos.
            pokemon_a_usar.vida += 20
            mensagem.texto = "{} teve seu HP restaurado em 20 pontos".format(pokemon_a_usar.nome)

        elif item == itens.elixir[0]: #Restaura o PP de todos os movimentos de um Pokémon em 10 pontos cada.
            # Percorrer todos os movimentos do pokémon e aumentar seus respectivos pp's:
            for i in range(len(pokemon_a_usar.movimentos)):
                
                pp_max = pokemon_a_usar.movimentos[i][3]
                
                # Código que aumenta em 10 o pp atual, lembrando que o máximo de pp atual que pode ter é pp_max.
                # movimentos[i][2]: pp atual
                pokemon_a_usar.movimentos[i][2] += 10
                # Verificar se o pp_atual passou do pp_max, se sim, pp_atual = pp_max (para não passar de pp_max)
                if pokemon_a_usar.movimentos[i][2] > pp_max:
                    pokemon_a_usar.movimentos[i][2] = pp_max
            
            mensagem.texto = "{} recuperou PP".format(pokemon_a_usar.nome)
               
        elif item == itens.potion[0]: #Ele restaura o HP de um Pokémon em 20 pontos.
            pokemon_a_usar.vida += 20
            mensagem.texto = "{} teve seu HP restaurado em 20 pontos".format(pokemon_a_usar.nome)

    
    rodando_o_jogo = True
    # Loop do jogo:
    while rodando_o_jogo:
        # Colocando o jogo para rodar no máximo a 60 quadros por segundo:
        delta = clock.tick(60)
        # Eventos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando_o_jogo = False
            # Eventos do teclado:
            if event.type == pygame.KEYDOWN:
                if menu.no_menu(menu.batalhando):
                    if sub_menu.no_submenu(sub_menu.principal) or sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                        if event.key == pygame.K_UP:
                            arq.som_menu_mudou.play()
                            pos.y -= 1
                        elif event.key == pygame.K_DOWN:
                            arq.som_menu_mudou.play()
                            pos.y += 1
                        elif event.key == pygame.K_LEFT:
                            arq.som_menu_mudou.play()
                            pos.x -= 1
                        elif event.key == pygame.K_RIGHT:
                            arq.som_menu_mudou.play()
                            pos.x += 1
                    if sub_menu.no_submenu(sub_menu.principal):
                        if event.key == pygame.K_ESCAPE:
                            arq.som_menu_mudou.play()
                            menu.atual = menu.escolhendo_pokemon
                            tocar_musica("Recursos/Sprites/SonsPokemon/fireRedAbertura.wav", True)
                            pos_menu_principal()
                        if event.key == pygame.K_RETURN:
                            arq.som_menu_mudou.play()
                            escolher_acao_batalha(pos)
                    elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                        if event.key == pygame.K_ESCAPE:
                            arq.som_menu_mudou.play()
                            pos_2x2()
                            sub_menu.atual = sub_menu.principal
                        if event.key == pygame.K_RETURN:
                            arq.som_menu_mudou.play()
                            # Verificar primeiro se o movimento está bloqueado e se possui pp suficiente
                            if not pokemons[0].movimentos[pos.i][0] in obter_id_bloqueados(pokemons[0]) and pokemons[0].movimentos[pos.i][2] > 0:
                                fazer_acao(menu, sub_menu, pokemons[0].movimentos[pos.i], category.normal_move)
                    elif sub_menu.no_submenu(sub_menu.itens):
                        if event.key == pygame.K_ESCAPE:
                            arq.som_menu_mudou.play()
                            pos_2x2()
                            sub_menu.atual = sub_menu.principal
                        if event.key == pygame.K_UP:
                            arq.som_menu_mudou.play()
                            pos.y -= 1
                        elif event.key == pygame.K_DOWN:
                            arq.som_menu_mudou.play()
                            pos.y += 1
                        if event.key == pygame.K_RETURN:
                            arq.som_menu_mudou.play()
                            if pos.i == 0:
                                pos_2x2()
                                sub_menu.atual = sub_menu.principal
                            else:
                                item_selecionado = pos.i - 1
                                fazer_acao(menu, sub_menu, pokemons[0].itens[item_selecionado], category.item_move)
                                pokemons[0].itens.pop(item_selecionado)
                elif menu.no_menu(menu.escolhendo_pokemon):
                    if event.key == pygame.K_UP:
                        arq.som_menu_mudou.play()
                        pos.y -= 1
                    elif event.key == pygame.K_DOWN:
                        arq.som_menu_mudou.play()
                        pos.y += 1
                    elif event.key == pygame.K_RETURN:
                        # escolheu o pokémon
                        arq.som_menu_mudou.play()
                        tocar_musica("Recursos/Sprites/SonsPokemon/batalha.wav", True)
                        escolher_pokemon(menu, sub_menu, mensagem)
                    elif event.key == pygame.K_ESCAPE:
                        rodando_o_jogo = False
        pygame.event.poll()
        processar_logica(delta, tempo, menu, sub_menu)
        desenhar_graficos()
        tocar_sons()
    # Sair do pygame:
    pygame.quit()
if __name__ == "__main__":
    main()