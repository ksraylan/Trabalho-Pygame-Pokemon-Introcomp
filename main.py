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

def main():
    itens = Itens()
    category = Category()
    effect = Effect()
    menu = cena.Menu()
    sub_menu = cena.Submenu()
    mensagem = Mensagem("Test")
    escala = arq.escala
    # menu espaçamento:
    menu_espacamento = (200,50)
    # tamanho menu:
    #menu_tamanho = 2*escala
    # tamanho seta:
    tamanho_cursor = 11*escala
    # Pokémon selecionado (tela de seleção de pokémon):
    sel_s = 0
    pos = Pos(2, 2)
    distanciamento = (50*escala,15*escala)
    generos = ["F", "M"]
    clock = pygame.time.Clock()
    condicao = Condicao()
    tipos = Types()
    moves = Moves()
    pk_pikachu = Pokemon("Pikachu",35,55,40,90,50,50,9,random.choice(generos),
    [tipos.normal],[moves.growl, moves.thunder_shock, moves.tail_whip, moves.thunder_wave,
     moves.quick_attack, moves.double_team, moves.slam, moves.thunderbolt, moves.agility,
     moves.thunder, moves.light_screen], arq.carregar_imagem_pokemon(25))
    
    pk_charmander = Pokemon("Charmander",39,52,43,65,60,50,9, random.choice(generos),[tipos.fire],[moves.growl, moves.scratch, moves.ember, moves.mokescreen, moves.rage, moves.scary_face, moves.flamethrower, moves.slash, moves.dragon_rage, moves.fire_spin], arq.carregar_imagem_pokemon(4))
    pk_bulbasaur = Pokemon("Bulbasaur",45,49,49,45,65,65,9, random.choice(generos), [tipos.grass, tipos.poison], [moves.tackle, moves.growl, moves.leech_seed, moves.vine_whip, moves.poison_powder, moves.sleep_powder, moves.razor_leaf, moves.sweet_scent, moves.growth, moves.synthesis, moves.solar_beam],arq.carregar_imagem_pokemon(1))
    pk_squirtle = Pokemon("Squirtle",44,48,65,43,50,64, 9,random.choice(generos),[tipos.water], [moves.tackle, moves.tail_whip, moves.bubble, moves.withdraw, moves.water_gun, moves.bite, moves.rapid_spin, moves.protect, moves.rain_dance, moves.skull_bash, moves.hydro_pump], arq.carregar_imagem_pokemon(7))
    pk_rhydon = Pokemon("Rhydon",105,130,120,40,45,45,9,random.choice(generos), [tipos.ground, tipos.rock],[moves.fury_attack, moves.horn_attack, moves.stomp, moves.tail_whip, moves.scary_face, moves.rock_blast, moves.horn_drill, moves.take_down, moves.earthquake, moves.megahorn], arq.carregar_imagem_pokemon(112))
    pk_gengar = Pokemon("Gengar",60,65,60,110,130,75,9,random.choice(generos), [tipos.ghost, tipos.poison], [moves.hypnosis, moves.lick, moves.spite, moves.curse, moves.night_shade, moves.confuse_ray, moves.shadow_punch, moves.dream_eater, moves.destiny_bond, moves.shadow_ball, moves.nightmare, moves.mean_look], arq.carregar_imagem_pokemon(94))
    pk_dragonite = Pokemon("Dragonite",91,134,95,80,100,100,9, random.choice(generos), [tipos.dragon, tipos.flying], [moves.leer, moves.thunder_wave, moves.twister, moves.wrap, moves.dragon_rage, moves.slam, moves.agility, moves.safeguard, moves.wing_attack, moves.outrage, moves.hyperbeam], arq.carregar_imagem_pokemon(149))
    pk_mewtwo = Pokemon("Mewtwo",106,110,90,130,154,90,9,random.choice(generos), [tipos.psychic], [moves.confusion, moves.disable, moves.barrier, moves.mist, moves.swift, moves.recover, moves.safeguard, moves.psychic, moves.psych_up, moves.future_sight, moves.amnesia], arq.carregar_imagem_pokemon(150))
    
    pokemons_pode_escolher = [pk_pikachu, pk_charmander, pk_bulbasaur, pk_squirtle, pk_rhydon, pk_gengar, pk_dragonite, pk_mewtwo]
    cores_pode_escolher = [cor.AMARELO, cor.LARANJA, cor.VERDE, cor.AZUL, cor.CIANO, cor.ROXO, cor.ROSA, cor.CINZA]

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
        #Musica entrada:
        if menu.atual == menu.escolhendo_pokemon:
            #arq.som_Batalha.stop()
            #arq.som_fire_red_abertura.play()
            pass
        if menu.atual == menu.batalhando:
            #arq.som_fire_red_abertura.stop()
            #arq.som_Batalha.play()
            pass
        if condicao.atual == condicao.vitoria:
            arq.som_vitoria.play()
        if condicao.atual == condicao.derrota:
            arq.som_derrota.play()

    width_dividido = janela.tamanho[0]/2
    # espaçamento x na esquerda da seta:
    e_s_x = 16
    # espacamento entre os nomes:
    e_n = 32

    def desenhar_graficos():
        #limpar a tela:
        janela.tela.fill(cor.PRETO)      
        if menu.no_menu(menu.escolhendo_pokemon):
            # Fonte:
            superf = arq.fonte.render("Escolha o seu pokémon", False, cor.BRANCO)
            superf_rect = superf.get_rect()
            superf_rect.center =(width_dividido, 100)
            janela.tela.blit(superf, superf_rect)

            # posicao do nome que está sendo selecionado:
            
            # posicao y da seta dentro do retangulo:
            #li = 100-e_n + (e_n*sel_s)
            li = menu_espacamento[1] + tamanho_cursor/2 + (e_n*sel_s)

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
            # Cena de batalha:
            #tela.blit(imagem, (x, y))
            janela.tela.blit(arq.img_fundo_pokemon,(0,0))
            
            # (x, y)
            
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
                pygame.draw.rect(janela.tela, cor.VERMELHO, ((janela.tamanho[0] - 107.5*escala + (pos.x*distanciamento[0]), janela.tamanho[1] - 37.5*escala + (pos.y*distanciamento[1])), (50*escala,15*escala)), int(1*escala))
            elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                janela.tela.blit(arq.img_pp_bar, (0, janela.tamanho[1] - 48*escala))
                x = 0
                espac_x = janela.tamanho[0]/2 - janela.tamanho[0]/5
                espac_y = 13*escala
                y = y_pos = -pos.y
                for i in range(len(pokemons[0].movimentos)):
                    nome_movimento = pokemons[0].movimentos[i][1]
                    superf = arq.fonte_escolher_move.render(str(nome_movimento), False, cor.PRETO)
                    superf_rect = superf.get_rect()
                    superf_rect.bottomleft =(10*escala + (espac_x*x), janela.tamanho[1] - (30*escala) + (espac_y * y))
                    if y >= 0:
                        janela.tela.blit(superf, superf_rect)
                    x += 1
                    if x >= 2:
                        x = 0
                        y += 1
                    if y + y_pos > 2 + y_pos:
                        break
                pygame.draw.rect(janela.tela, cor.VERMELHO, ((10*escala + (espac_x*pos.x)), (janela.tamanho[1] - (30*escala) + (espac_y * (y_pos+pos.y -1)) ), (espac_x), (espac_y)), int(1*escala))
            if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                janela.tela.blit(arq.img_barra1, (15*escala, 18*escala))
            if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                janela.tela.blit(arq.img_barra2, (janela.tamanho[0] - 110*escala,janela.tamanho[1] - 88*escala))

            # nomes dos pokemons renderizados na barra:
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

            # Barras de vida:
            
            # Vida amarela:
            
            if pokemons[1].vida_anim <= pokemons[1].vida_maxima/2:
                img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela,
                (int(arq.img_vida_amarela.get_width() + (escala*39)),
                arq.img_vida_vermelha.get_height()))
                
                janela.tela.blit(img_vida_amarela_esticada,(int(55*escala), int(34*escala)))
            
            if pokemons[0].vida_anim <= pokemons[0].vida_maxima/2:
                img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela,
                (int(arq.img_vida_amarela.get_width() + (escala*39)),
                arq.img_vida_vermelha.get_height()))
                
                janela.tela.blit(img_vida_amarela_esticada,(janela.tamanho[0]-62*escala,
                janela.tamanho[1] - 69*escala))
            
            # Vida vermelha:
            
            if pokemons[1].vida_anim <= pokemons[1].vida_maxima/5:
                img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha,
                (int(arq.img_vida_vermelha.get_width() + (escala*39)),
                arq.img_vida_vermelha.get_height()))
                
                janela.tela.blit(img_vida_vermelha_esticada,(55*escala, 34*escala))
            
            if pokemons[0].vida_anim <= pokemons[0].vida_maxima/5:
                img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha,
                (int(arq.img_vida_vermelha.get_width() + (escala*39)),
                arq.img_vida_vermelha.get_height()))
                
                janela.tela.blit(img_vida_vermelha_esticada,(janela.tamanho[0] -
                62*escala,janela.tamanho[1] - 69*escala))
            
            # Barra da parte "sem vida":
            
            if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida,
                (ceil((arq.img_barra_sem_vida.get_width() + (escala*39)) *
                (pokemons[1].vida_maxima - pokemons[1].vida_anim)/pokemons[1].vida_maxima),
                arq.img_barra_sem_vida.get_height()))

                janela.tela.blit(img_barra_sem_vida_esticada,(floor(55*escala +
                barra_width * (pokemons[1].vida_anim/pokemons[1].vida_maxima)), 34*escala))

            if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida,
                (ceil((arq.img_barra_sem_vida.get_width() + (escala*39)) *
                (pokemons[0].vida_maxima - pokemons[0].vida_anim)/pokemons[0].vida_maxima),
                arq.img_barra_sem_vida.get_height()))
                
                janela.tela.blit(img_barra_sem_vida_esticada,(floor(janela.tamanho[0] -
                62*escala + barra_width * (pokemons[0].vida_anim/pokemons[0].vida_maxima)),
                janela.tamanho[1] - 69*escala))
            
            # Mostrando o nível do pokémon:
            nivel = arq.fonte_txt.render(str(pokemons[1].nivel), False, cor.PRETO)
            nivel_rect = nivel.get_rect()
            nivel_rect.left = 96*escala
            nivel_rect.top = 18.5*escala
            if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                janela.tela.blit(nivel, nivel_rect)
            nivel = arq.fonte_txt.render(str(pokemons[0].nivel), False, cor.PRETO)
            nivel_rect = nivel.get_rect()
            nivel_rect.left = janela.tamanho[0] - 21*escala
            nivel_rect.top = janela.tamanho[1] - 84.5*escala
            if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                janela.tela.blit(nivel, nivel_rect)
            if not sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                texto_multilinha(mensagem.texto)
            #janela.tela.blit(batalha_nome, batalha_rect)

        pygame.display.update()


    def escolher_pokemon(menu, sub_menu, mensagem):
        menu.atual = menu.batalhando
        sub_menu.atual = sub_menu.principal
        # seu pokémon:
        pokemons[0] = pokemons_pode_escolher[sel_s].copy()
        # pokémon inimigo:
        pokemons[1] = pokemons_pode_escolher[random.randrange(0,len(pokemons_pode_escolher)-1)].copy()
        mensagem.texto = "O que {} deve fazer?".format(pokemons[0].nome)
        
    def escolher_acao_batalha(pos):
        if pos.i == 0:
            sub_menu.atual = sub_menu.escolhendo_ataque
            pos.width = 2
            pos.height = 6
            pos.i_limit = len(pokemons[0].movimentos)
        elif pos.i == 3:
            fazer_acao(menu, sub_menu, Acao.fugir)
    
    turnos = []

    def fazer_acao(menu, sub_menu, movimento):
        vez = random.randrange(1,2)
        if pokemons[0].velocidade > pokemons[1].velocidade:
            vez = 1
        elif pokemons[0].velocidade < pokemons[1].velocidade:
            vez = 2
        #quick attack priority +1
        #move = movimento[0]
        if vez == 1:
            turnos.append([pokemons[0], pokemons[1], None, category.state_move])
            turnos.append([pokemons[0], pokemons[1], movimento, category.normal_move])
            turnos.append([pokemons[1], pokemons[1], None, category.state_move])
            turnos.append([pokemons[1], pokemons[0], randomizar_acao(pokemons[1]), category.normal_move])
        else:
            
            turnos.append([pokemons[1], pokemons[0], None, category.state_move])

            turnos.append([pokemons[1], pokemons[0], randomizar_acao(pokemons[1]), category.normal_move])
            
            turnos.append([pokemons[0], pokemons[1], None, category.state_move])
            
            turnos.append([pokemons[0], pokemons[1], movimento, category.normal_move])
        sub_menu.atual = sub_menu.principal

    def randomizar_acao(pokemon):
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
                        mensagem.texto = "{} ganhou a batalha!".format(pokemons[1].nome)
                        sub_menu.atual = sub_menu.derrota
                        tocar_musica("Recursos/Sprites/SonsPokemon/derrota.wav", False)

                    elif pokemons[1].foi_derrotado() or pokemons[1].conseguiu_fugir():
                        
                        sub_menu.atual = sub_menu.fazendo_acoes
                        mensagem.texto = "{} ganhou a batalha!".format(pokemons[0].nome)
                        sub_menu.atual = sub_menu.vitoria
                        tocar_musica("Recursos/Sprites/SonsPokemon/vitoria.wav", False)
                    else:
                        if len(turnos) > 0:
                            sub_menu.atual = sub_menu.fazendo_acoes
                            process_turns(turnos, mensagem, tempo)
                        else:
                            if sub_menu.atual == sub_menu.fazendo_acoes:
                                sub_menu.atual = sub_menu.principal
                                mensagem.texto = "O que {} deve fazer?".format(pokemons[0].nome)
                
                else:
                    tempo.fim_de_jogo_tempo += delta

                    if tempo.fim_de_jogo_tempo >= 5000:
                        menu.atual = menu.escolhendo_pokemon
                        sub_menu.atual = sub_menu.principal
                        tocar_musica("Recursos/Sprites/SonsPokemon/fireRedAbertura.wav", True)
                        tempo.fim_de_jogo_tempo = 0
    
    def process_turns(turnos, mensagem, tempo):
        pokemon_a_fazer = turnos[0][0] # pokemon que vai usar a ação
        pokemon_a_tomar = turnos[0][1] # pokémon que vai sofrer da ação
        move = turnos[0][2] # qual movimento vai ser realizado
        turn_category = turnos[0][3] # pega qual categoria é (movimento normal ou de estado)

        if turn_category["id"] == category.state_move["id"]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "texto do state_move deve aparecer aqui"
                pokemon_a_fazer.process_effects(True, pokemon_a_tomar)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        elif turn_category["id"] == category.normal_move["id"]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} usou {}!".format(pokemon_a_fazer.nome, str(move[1]))
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                # animação básica
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                # desativa a animação básica
                pokemon_a_tomar.sumindo = False
                # processa o movimento atual
                process_moves(pokemon_a_fazer, pokemon_a_tomar, move[0])
                tempo.etapa_turno_incrementa()
            # a última etapa é tirar o movimento que acabou de ser feito da lista
            # de movimentos:
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        # resetar o tempo:
        tempo.resetar()  

    def mostrar_texto_ataque_normal(dano):
        errou = True if dano == 0 else False
        if errou:
            mensagem.texto = "Errou o alvo"
        else:
            mensagem.texto = "Fez perder {} HP".format(dano)

    def mostrar_mensagem_errou():
        if not mensagem.texto == "Errou o alvo":
            mensagem.texto = "Errou"


    def usar_item(pokemon_a_usar, pokemon_inimigo, item):
        if item == itens.dire_hit:
            

        elif item == guard_spec: #Um item que impede a redução de estatísticas 
            pokemon_a_usar.protegido = 3
            mensagem.texto = "{} impediu que seus dados mudassem".format(pokemon_a_usar)

        elif item == x_accuracy: #Aumenta a estatística de precisão do Pokémon em batalha
            pokemon_a_usar.precisao += 20 * pokemon_a_usar / 100
            mensagem.texto = "{} aumentou a precisão em 20%".format(pokemon_a_usar)
            
        elif item == x_attack:
            


    def process_moves(pokemon_a_fazer, pokemon_a_tomar, move):
        print("Movimento executado:", move)
        # códigos dos movimentos:
        num = random.randrange(0,101)
        
        if move == Acao.ataque_simples:
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
        if move == moves.growl[0]:
            # Growl lowers the target's Attack by one stage.
            pokemon_a_tomar.ataque -= 1
            mensagem.texto = "O ataque de {} diminuiu".format(pokemon_a_tomar.nome)
        elif move == moves.thunder_shock[0]:
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            if num <= 10 and not tipos.electric in pokemon_a_tomar.tipos: # 10% de chance de ser paralizado:
                pokemon_a_tomar.bloqueado = 1
                pokemon_a_tomar.velocidade -= 50 * pokemon_a_fazer.velocidade / 100 #75%
                mensagem.texto = "e foi paralizado".format(pokemon_a_tomar.nome,dano)
        elif move == moves.tail_whip[0]:
            pokemon_a_tomar.defesa -= 1
            mensagem.texto = "Defesa de {} diminuiu".format(pokemon_a_tomar.nome,dano)

        elif move == moves.thunder_wave[0]: #25% de chance do alvo não atacar
            pokemon_a_tomar.paralisado = True
            # Speed is decreased by 75%
            pokemon_a_tomar.velocidade -= 75 * pokemon_a_fazer.velocidade / 100
            mensagem.texto = "{} ficou paralisado".format(pokemon_a_tomar.nome)

        elif move == moves.quick_attack[0]: #deals damage (IMPLEMENTAR ataque prioritário!)
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
        elif move == moves.double_team[0]: # (IMPLEMENTAR)
            pokemon_a_tomar. -= 1
            pokemon_a_tomar.pode_fugir == False 
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu {} HP e sua chance de fugir diminuiu em um estágio!".format(pokemon_a_tomar.nome)
            
        elif move == moves.slam[0]: 
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            
        elif move == moves.thunderbolt[0]:#25% de chance do alvo não atacar
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            if num <= 10:
                pokemon_a_tomar.paralisado = True
                mensagem.texto = "e foi paralisado".format(pokemon_a_tomar.nome)
                
        elif move == moves.agility[0]: #aumenta velocidade em +2 estágios
            pokemon_a_fazer.velocidade += 2 
            mensagem.texto = "{} teve a velocidade aumentada".format(pokemon_a_fazer.nome)

        elif move == moves.thunder[0]:
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            if num <= 30:
                pokemon_a_tomar.paralisado = True
                mensagem.texto = "e foi paralisado".format(pokemon_a_tomar.nome)
                
        elif move == moves.scratch[0]:
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))

        elif move == moves.smokescreen[0]: #precisão do alvo reduz em 1 estágio
            pokemon_a_tomar.precisao -= 1
            mensagem.texto = "{} teve a precisão reduzida".format(pokemon_a_tomar.nome)

        elif move == moves.rage[0]: #ataque aumenta em 1 estágio
            pokemon_a_fazer.ataque += 1 
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            mensagem.texto += "e ataque aumentado"

        elif move == moves.scary_face[0]: #diminui velocidade do alvo em 2 estágios
            if num <= 90:
                pokemon_a_tomar.velocidade -= 2
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} teve a velocidade diminuida".format(pokemon_a_tomar.nome)
            else:
                mensagem.texto = "Parece que não surgiu efeito"

        elif move == moves.flamethrower[0]: #10% de chance de queimar (IMPLEMENTAR)
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            if num <= 10:
                pokemon_a_tomar.vida -= 1/16
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "e foi queimado" 
                  
        elif move == moves.dragon_rage[0]:
            pokemon_a_tomar.vida -= 40
            mensagem.texto = "{} foi atacado".format(pokemon_a_tomar.nome)
            
        elif move == moves.fire_spin[0]: # (IMPLEMENTAR)
            pokemon_a_tomar.vida -= 1/8
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu 1/8 HP!".format(pokemon_a_tomar.nome)
            
        elif move == moves.tackle[0]: #power of 35 e 95% acerto (IMPLEMENTAR)

            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu x HP!".format(pokemon_a_tomar.nome)
            
        elif move == moves.leech_seed[0]:
            if not tipos.grass in pokemon_a_tomar.tipos:
                pokemon_a_tomar.add_effect(effect.leech_seed)
            else:
                mensagem.texto = "Parece que não surgiu efeito"
                
        elif move == moves.vine_whip[0]:
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            
        elif move == moves.poison_powder[0]: # veneno (IMPLEMENTAR)
            pokemon_a_tomar.vida -= pokemon_a_tomar.vida / 8
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu 1/8 HP!".format(pokemon_a_tomar.nome)

        elif move == moves.sleep_powder[0]: #coloca o alvo para dormir por até 3 turnos
            pokemon_a_tomar.bloqueado = 3 
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} dormindo por {} turnos!".format(pokemon_a_tomar.nome, 3)
            
        elif move == moves.razor_leaf[0]: #taxa de acerto crítico de 1/8 (IMPLEMENTAR)
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            
        elif move == moves.sweet_scent[0]: #diminui a evasão do alvo -1 (IMPLEMENTAR)
            mensagem.texto = "(a ser implementado)"
            
        elif move == moves.growth[0]: #aumenta o ataque especial em um 1 estágio
            pokemon_a_fazer.especial_ataque += 1 
            mensagem.texto = "Ataque especial de {} foi aumentado".format(pokemon_a_fazer.nome)
        elif move == moves.synthesis[0]: #recupera HP (IMPLEMENTAR) (VIDA_CERTA)
            pokemon_a_fazer.vida += 2
            mensagem.texto = "{} recuperou HP".format(pokemon_a_tomar.nome)
            
        elif move == moves.solar_beam[0]: # (IMPLEMENTAR) (EFEITO)
            pokemon_a_tomar.vida -= 3
            mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome,3)
            
        elif move == moves.ember[0]: #10% de chance de queimar  
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            if num <= 10 and not tipos.fire in pokemon_a_tomar.tipos:
                pokemon_a_tomar.vida -= 1/8
                mensagem.texto = "e foi queimado"
                
        elif move == moves.withdraw[0]: #aumenta a defesa em 1 estágio
            pokemon_a_fazer.defesa += 1
            mensagem.texto = "{} teve a defesa aumentada!".format(pokemon_a_fazer.nome)
            
        elif move == moves.water_gun[0]:
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            
        #elif move == moves.bite[0]: #30% de chance do alvo vacilar (IMPLEMENTAR)
        elif move == moves.rapid_spin[0]:
            pokemon_a_fazer.velocidade += 1
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            mensagem.texto = "e sua velocidade aumentou"
        #elif move == moves.protect[0]: #protege o pokemon de quaisquer ataques (IMPLEMENTAR)
        #elif move == moves.rain_dance[0]: #provoca chuva (IMPLEMENTAR)
              
        elif move == moves.skull_bash[0]:#aumenta a defesa em +1 e dar dano segundo turno (IMPLEMENTAR)
            pokemon_a_fazer.defesa += 1
            mensagem.texto = "{} teve a defesa aumentada!".format(pokemon_a_fazer.nome)
            
        elif move == moves.hydro_pump[0]: #damage
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            
        elif move == moves.fury_attack[0]: # (IMPLEMENTAR) (efeito)
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu 1 HP!".format(pokemon_a_tomar.nome)
            
        elif move == moves.horn_attack[0]:#damage
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))

        elif move == moves.stomp[0]: #damage e 30% de chance de fazer o alvo vacilar (IMPLEMENTAR)
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))

        #elif move == moves.rock_blast[0]: #atinge 3 vezes por turno usado. A probabilidade de cada intervalo é mostrada à direita, com a potência total após cada acerto.Cada golpe de Rock Blast é tratado como um ataque separado (IMPLEMENTAR)
        elif move == moves.horn_drill[0]: #fará o oponente desmaiar (IMPLEMENTAR)
            pokemon_a_tomar.bloqueado = 3
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} desmaiou por {} turnos!".format(pokemon_a_tomar.nome,bloqueado)

        elif move == moves.take_down[0]:#perde 25 hp (IMPLEMENTAR)
            pokemon_a_tomar.vida -=25
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu 1 HP!".format(pokemon_a_tomar.nome)
            
        elif move == moves.earthquake[0]: #o dano acertará com o dobro de poder (IMPLEMENTAR)
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            mensagem.texto = "{} perdeu x HP!".format(pokemon_a_tomar.nome)
            
        elif move == moves.megahorn[0]: #deals damage
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
        
        elif move == moves.hypnosis[0]:#o pokemon fica bloqueado por 3 rodadas (IMPLEMENTAR)
            pokemon_a_tomar.bloqueado == 3
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} desmaiou por {} turnos!".format(pokemon_a_tomar.nome, 3)
        
        elif moves == moves.lick[0]: #30% de chance de paralisar o alvo
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
            if num <= 30:              
                pokemon_a_tomar.paralisado = True
                mensagem.texto += "e foi paralisado"
            
        elif move == moves.spite[0]:#perde 2-5 PP (oponente) (IMPLEMENTAR) (PP)
            pass
        
        elif move == moves.curse[0]: # (IMPLEMENTAR) (VER DE NOVO)
            pokemon_a_tomar.vida -= 25/100
            pokemon_a_fazer.vida_maxima -= 50/100
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu 25% HP e 50% HP máximo!".format(pokemon_a_tomar.nome)

        elif move == moves.night_shade[0]: #dano igual ao nivel do usuario
            pokemon_a_tomar.vida -= pokemon_a_fazer.nivel
            mensagem.texto = "{} perdeu {} HP".format(pokemon_a_tomar.nome, pokemon_a_fazer.nivel)

        elif move == moves.confuse_ray[0]:#Pokémon confusos têm 33% de chance de se ferir a cada turno, por 1-4 turnos de ataque (50% de chance nas gerações 1-6 ). O dano recebido é como se o Pokémon atacasse a si mesmo com um ataque físico de 40 base power sem tipo. (IMPLEMENTAR)
            pass

        elif move == moves.shadow_punch[0]: #damage (IMPLEMENTAR)
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar))
        elif move == moves.dream_eater[0]: # (IMPLEMENTAR) melhor.  #caso o pokemon esteja bloqueado o usuario recebe 50% de vida
            if pokemon_a_tomar.bloqueado:
                pokemon_a_fazer.vida += 50/100
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} aumentou o HP em 50%!".format(pokemon_a_fazer.nome)

        elif move == moves.destiny_bond[0]: #se o usuário desmaiar, o oponente também desmaia
            if pokemon_a_fazer.bloqueado == True:
                pokemon_a_tomar.bloqueado = True
                mensagem.texto = "{} desmaiou!".format(pokemon_a_tomar.nome)
            
        elif move == moves.shadow_ball[0]: #diminui a defesa especial do adversario em 20%
            pokemon_a_tomar.especial_defesa -= 20/100
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} teve a defesa especial diminuida em 20%!".format(pokemon_a_tomar.nome)

        elif move == moves.nightmare[0]: #Se o alvo estiver dormindo, faz com que ele perca 1⁄4 de seu HP máximo
            if pokemon_a_tomar.bloqueado == True:
                pokemon_a_tomar.vida_maxima -= 1/4              #   kemon_a_fazer.atacar(pokemon_a_tomar)r)
                mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome,dano)        
        
        elif move == moves.mean_look[0]:#oponente nao pode fugir
            pokemon_a_tomar.pode_fugir = False
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} não pode fugir!".format(pokemon_a_tomar.nome) 


        elif move == moves.leer[0]: #a defesa do alvo diminu em 1 estágio
            pokemon_a_toma.defesa -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} teve sua defesa diminuida!".format(pokemon_a_tomar.nome)

        elif  move == moves.twister[0]:#deals damage e o alvo tem chance de vacilar de 30%
            if num <= 30:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome,dano)

        elif move == moves.wrap[0]: #o alvo perde 1/8 HP
            pokemon_a_tomar.vida -= 1/8
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu {} de HP!".format(pokemon_a_tomar.nome,dano) 

        elif move == moves.safeguard[0]: #damage
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome,dano) 

        elif move == moves.wing_attack[0]: #damage
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome,dano)

        elif move == moves.outrage[0]: 
            pokemon_a_fazer.atacar(pokemon_a_fazer)
            mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome,dano)        
        
        elif move == moves.hyperbeam[0]:#deals damage e o usuario perde 75
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.vida -= 75
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} foi atacado e {} perde {} de HP!".format(pokemon_a_tomar.nome, dano)

        elif move == moves.confusion[0]: #damage e 1% de chance de diminuir a velocidade do alvo
            if num <= 10:
                pokemon_a_tomar.vida -= 1
                pokemon_a_tomar.velocidade -= 75/100
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} tem a velocidade reduzida!".format(pokemon_a_tomar.nome)

        elif move == moves.disable[0]: # bloqueia o movimento anterior por 6 turnos
            pass

        elif move == moves.mist[0]:# os dados do usuario nao mudam
            pokemon_a_fazer.protegido = 4
            mensagem.texto = "{} dados do usuario não mudam!".format(pokemon_a_fazer.nome)

        elif move == moves.swift[0]: #damage
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome, dano)
            
        elif move == moves.psychic[0]: #deals damage e menos 10% da defesa especial
            pokemon_a_tomar.vida -= 1
            pokemon_a_tomar.defesa_especial -= 10/100
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perde 10% da defesa especial!".format(pokemon_a_tomar.nome)

        elif move == moves.psych_up[0]: #Copia as mudanças de estatísticas do oponente incompleto
            pokemon_a_fazer == pokemon_a_fazer.protegido 
            mensagem.texto = "{} fica com as estatísticas igual ao oponente!".format(pokemon_a_fazer.nome)        
    
        elif move == moves.recover[0]:#recupera 50% de hp
            pokemon_a_fazer.vida += 50/100
            mensagem.texto = "{} recuperou 50% do HP!".format(pokemon_a_tomar.nome)
        
        elif move == moves.future_sight[0]:#deals damage
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} perdeu {} HP!".format(pokemon_a_tomar.nome,dano)
        
        elif move == moves.amnesia[0]: #aumeneta a defesa especial do usuário em dois estágios
            pokemon_a_fazer.especial_defesa += 2
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} aumentou a defesa especial!".format(pokemon_a_fazer.nome)       

    rodando_o_jogo = True
    mouse_pos = (0,0)
    # Loop do jogo:
    while rodando_o_jogo:
        # Colocando o jogo para rodar no máximo a 60 fps:
        delta = clock.tick(60)
        # Eventos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando_o_jogo = False
            # Eventos do mouse:
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            # Eventos do teclado:
            if event.type == pygame.KEYDOWN:
                if menu.no_menu(menu.batalhando):
                    if sub_menu.no_submenu(sub_menu.principal) or sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                        if event.key == pygame.K_UP:
                            pos.y -= 1
                        elif event.key == pygame.K_DOWN:
                            pos.y += 1
                        elif event.key == pygame.K_LEFT:
                            pos.x -= 1
                        elif event.key == pygame.K_RIGHT:
                            pos.x += 1
                    if sub_menu.no_submenu(sub_menu.principal):
                        if event.key == pygame.K_ESCAPE:
                            menu.atual = menu.escolhendo_pokemon
                            tocar_musica("Recursos/Sprites/SonsPokemon/fireRedAbertura.wav", True)
                        if event.key == pygame.K_RETURN:
                            escolher_acao_batalha(pos)
                    elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                        if event.key == pygame.K_ESCAPE:
                            sub_menu.atual = sub_menu.principal
                        if event.key == pygame.K_RETURN:
                            fazer_acao(menu, sub_menu, pokemons[0].movimentos[pos.i])
                elif menu.no_menu(menu.escolhendo_pokemon):
                    if event.key == pygame.K_UP:
                        sel_s = sel_s - 1
                        if sel_s < 0:
                            sel_s = len(pokemons_pode_escolher) - 1
                    elif event.key == pygame.K_DOWN:
                        sel_s = sel_s + 1
                        if sel_s > len(pokemons_pode_escolher) - 1:
                            sel_s = 0
                    elif event.key == pygame.K_RETURN:
                        # escolheu o pokémon
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