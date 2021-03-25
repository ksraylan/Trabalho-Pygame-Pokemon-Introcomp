# Importações:
import random
from math import ceil, floor
import pygame
import janela
from pokemon import Pokemon, Tipos, Movimento
import arquivos as arq
import cores as cor
import cena
from mensagem import Mensagem
from condicao import Condicao
from acoes import Acao
from tempo import Tempo
from posicao import Pos
from effect import Effect

def main():
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
    tipos = Tipos()
    moves = Movimento()
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
            superf = arq.fonte.render("Choose your pokémon", False, cor.BRANCO)
            superf_rect = superf.get_rect()
            superf_rect.center =(width_dividido, 100)
            janela.tela.blit(superf, superf_rect)

            # posicao do nome que está sendo selecionado:
            
            # posicao y da seta dentro do retangulo:
            #li = 100-e_n + (e_n*sel_s)
            li = menu_espacamento[1] + tamanho_cursor/2 + (e_n*sel_s)
            

            # seta de seleção:
            pygame.draw.polygon(janela.tela, cor.VERMELHO, ( (menu_espacamento[0] + e_s_x, menu_espacamento[1] + li), (menu_espacamento[0] + e_s_x,menu_espacamento[1] + tamanho_cursor + li), (menu_espacamento[0] + e_s_x+ tamanho_cursor/2, menu_espacamento[1] + tamanho_cursor/2 + li) ) )
            
            # loop que vai percorrer a lista com os nomes dos pokemons:
            for i in range( len(pokemons_pode_escolher) ):
                # aqui vamos criar um texto com o pokemon "i" (o "i" que vai até o range do loop):
                superf = arq.fonte.render(pokemons_pode_escolher[i].nome, False, cores_pode_escolher[i])
                # Pegaremos as dimensões do texto que criamos acima:
                superf_rect = superf.get_rect()
                # Colocaremos no centro, e pegamos o espaçamento e multiplicamos por "i", para os nomes dos pokemons irem para baixo e não ficarem um em cima do outro:
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
            
            #arq.img_vida_vermelha
            
            """
            img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha, (int(arq.img_vida_vermelha.get_width() + (escala*39)), arq.img_vida_vermelha.get_height()))
            janela.tela.blit(img_vida_vermelha_esticada,(55*escala, 34*escala))
            
            img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha, (int(arq.img_vida_vermelha.get_width()  + (escala*39)), arq.img_vida_vermelha.get_height()))
            janela.tela.blit(img_vida_vermelha_esticada,(janela.tamanho[0] - 62*escala,janela.tamanho[1] - 69*escala))
            
            img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela, (int(arq.img_vida_amarela.get_width()  + (escala*39)), arq.img_vida_vermelha.get_height()))
            janela.tela.blit(img_vida_amarela_esticada,(int(55*escala), int(34*escala)))

            img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela, (int(arq.img_vida_amarela.get_width()  + (escala*39)), arq.img_vida_vermelha.get_height()))
            janela.tela.blit(img_vida_amarela_esticada,(janela.tamanho[0] - 62*escala,janela.tamanho[1] - 69*escala))
            """
            img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida, (ceil((arq.img_barra_sem_vida.get_width() + (escala*39)) * (pokemons[1].vida_maxima - pokemons[1].vida)/pokemons[1].vida_maxima), arq.img_barra_sem_vida.get_height()))
            if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                janela.tela.blit(img_barra_sem_vida_esticada,(floor(55*escala + barra_width * (pokemons[1].vida/pokemons[1].vida_maxima)), 34*escala))

            img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida, (ceil((arq.img_barra_sem_vida.get_width() + (escala*39)) * (pokemons[0].vida_maxima - pokemons[0].vida)/pokemons[0].vida_maxima    ), arq.img_barra_sem_vida.get_height()))
            if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                janela.tela.blit(img_barra_sem_vida_esticada,(floor(janela.tamanho[0] - 62*escala + barra_width * (pokemons[0].vida/pokemons[0].vida_maxima)),janela.tamanho[1] - 69*escala))
            
            # Mostrando o nível do pokémon
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
        mensagem.texto = "What should {} do?".format(pokemons[0].nome)
        
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
            turnos.append([pokemons[0], pokemons[1], movimento])
            turnos.append([pokemons[1], pokemons[0], randomizar_acao()])
        else:
            turnos.append([pokemons[1], pokemons[0], randomizar_acao()])
            turnos.append([pokemons[0], pokemons[1], movimento])
        sub_menu.atual = sub_menu.principal

    def randomizar_acao():
        return random.randrange(0,1)

    
    tempo = Tempo(1000)

    def processar_logica(delta, tempo, menu, sub_menu):

        if menu.atual == menu.batalhando:

            # animação texto:
            tempo.mensagem_tempo += delta

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
                        mensagem.texto = "You lost!"
                        sub_menu.atual = sub_menu.derrota
                        tocar_musica("Recursos/Sprites/SonsPokemon/derrota.wav", False)

                    elif pokemons[1].foi_derrotado() or pokemons[1].conseguiu_fugir():
                        
                        sub_menu.atual = sub_menu.fazendo_acoes
                        mensagem.texto = "You won!"
                        sub_menu.atual = sub_menu.vitoria
                        tocar_musica("Recursos/Sprites/SonsPokemon/vitoria.wav", False)
                    else:
                        if len(turnos) > 0:
                            sub_menu.atual = sub_menu.fazendo_acoes
                            process_turns(turnos, mensagem, tempo)
                        else:
                            if sub_menu.atual == sub_menu.fazendo_acoes:
                                sub_menu.atual = sub_menu.principal
                                mensagem.texto = "What should {} do?".format(pokemons[0].nome)
                
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

        if tempo.etapa_turno == 0:
            mensagem.texto = "{} used {}!".format(pokemon_a_fazer, str(move[1]))
            tempo.etapa_turno_incrementa()
        elif tempo.etapa_turno == 1:
            # animação básica
            pokemon_a_tomar.sumindo = True
            tempo.etapa_turno_incrementa()
        elif tempo.etapa_turno == 2:
            # desativa a animação básica
            pokemon_a_tomar.sumindo = False
            # processa o movimento atual
            process_moves(pokemon_a_fazer, pokemon_a_fazer, move)
            tempo.etapa_turno_incrementa()
        # a última etapa é tirar o movimento que acabou de ser feito da lista
        # de movimentos:
        elif tempo.etapa_turno == 3:
            if len(turnos) > 0:
                turnos.pop(0)
            tempo.etapa_turno_reseta()
        
        # resetar o tempo:
        tempo.resetar()  

    def process_moves(pokemon_a_fazer, pokemon_a_tomar, move):
        
        # códigos dos movimentos:
        num = random.randrange(0,50)
        """
        if move == Acao.ataque_simples:
            dano = pokemon_a_fazer.atacar(pokemon_a_tomar)
            errou = True if dano == 0 else False
            if errou:
                mensagem.texto = "Wrong!"
            else:
                mensagem.texto = "Caused {} HP of damage!".format(dano)
        """
        if move == moves.growl[0]:
            pokemon_a_tomar.vida -= 1
            # Growl lowers the target's Attack by one stage.
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.thunder_shock[0]:
            if num <= 30:
                pokemon_a_tomar.vida -= 1                
                pokemon_a_tomar.velocidade -= 75/100
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.tail_whip[0]:
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.thunder_wave[0]: #25% de chance do alvo não atacar
            pokemon_a_tomar.vida -= 1
            pokemon_a_tomar.velocidade -= 75/100
        elif move == moves.quick_attack[0]: #deals damage
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.double_team[0]: 
            pokemon_a_tomar.ataque -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.slam[0]: 
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.thunderbolt[0]:
            if num <= 10:
                pokemon_a_tomar.vida -= 1
                pokemon_a_tomar.velocidade -= 75/100
        elif move == moves.agility[0]: #aumenta velocidade em +2 estágios
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.thunder[0]:
            if num <= 30:
                pokemon_a_tomar.vida -= 1
                pokemon_a_tomar.velocidade -= 75/100
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.scratch[0]:
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            pokemon_a_tomar.especial_ataque -= 10/100
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.smokescreen[0]: #precisão do alvo reduz em 1 estágio
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.rage[0]: #ataque aumenta em 1 estágio
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.scary_face[0]: #diminui velocidade do alvo em 2 estágios
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.flamethrower[0]: #10% de chance de quimar 
            pokemon_a_tomar.vida -= 1/16
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)   
        elif move == moves.dragon_rage[0]:
            pokemon_a_tomar.vida -= 40
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.fire_spin[0]:
            pokemon_a_tomar.vida -= 1/8
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.tackle[0]: #power of 35 e 95% acerto
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.leech_seed[0]:
            # a ação em si
            pokemon_a_tomar.sumindo = False
            if not tipos.grass in pokemon_a_tomar.tipos:
                pokemon_a_tomar.add_effect(effect.leech_seed)
            else:
                mensagem.texto = "It didn't work!"
        elif move == moves.vine_whip[0]:
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.poison_powder[0]:
            pokemon_a_tomar.vida -= 1/8
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.sleep_powder[0]: #coloca o alvo para dormir por até 3 turnos
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.razor_leaf[0]: #taxa de acerto crítico de 1/8
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.ataque_critico += 1/8
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.sweet_scent[0]: #diminui a evasão do alvo -1
            pokemon_a_tomar.vida -= 1
            pokemon_a_tomar.fugir -= 1 
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.growth[0]: #aumenta o ataque e o ataque especial em um 1 estágio
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move == moves.synthesis[0]: #recupera HP
            pokemon_a_fazer.vida += 1
            pokemon_a_fazer.vida(pokemon_a_fazer)
        elif move == moves.solar_beam[0]:
            pokemon_a_tomar.vida -= 1
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
        elif move ==
            










        
    def processar_turnos(turnos, mensagem, tempo):
        #turnos = [pokemon_a_usar_a_acao, pokemon_a_tomar_a_acao, acao]
        pokemon_a_fazer = turnos[0][0] # pokemon que vai usar a ação
        pokemon_a_tomar = turnos[0][1] # pokémon que vai sofrer da ação
        move = turnos[0][2] # qual movimento irá realizar
        
        if move == Acao.ataque_simples:
            tempo.sumido_tempo += tempo.milisegundos
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} attacks!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.sumindo = False
                dano = pokemon_a_fazer.atacar(pokemon_a_tomar)
                errou = True if dano == 0 else False
                if errou:
                    mensagem.texto = "Wrong!"
                else:
                    mensagem.texto = "Caused {} HP of damage!".format(dano)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
       


        elif move == moves.growl[0]:
            tempo.sumido_tempo += tempo.milisegundos
            if tempo.etapa_turno == 0:
                # etapa 0: mostrar mensagem do que o pokémon vai fazer:
                mensagem.texto = "{} used growl!".format(pokemon_a_fazer.nome)
                # incrementar a etapa do turno:
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                # animar o movimento:
                pokemon_a_tomar.sumindo = True
                # incrementar:
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                # agora o código do movimento:
                pokemon_a_tomar.vida -= 1
                # Growl lowers the target's Attack by one stage.
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                # colocar sempre para incrementar cada etapa do turno:
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                # a última etapa remove o turno atual:
                
                if len(turnos) > 0:
                    turnos.pop(0)
                # e em vez de incrementar, reseta (apenas na última etapa do turno!!):
                tempo.etapa_turno_reseta()
                num = random.randrange(0,50)
        #outro movimento:
        # elif move == moves.
        elif move == moves.thunder_shock[0]:#obs:paraliza,fazer depois
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used thunder shock!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                if num <= 30:
                    pokemon_a_tomar.vida -= 1                
                    pokemon_a_tomar.velocidade -= 75/100
                    tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.tail_whip[0]:#igual o growl(normal)
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail whilp!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.thunder_wave[0]:#paraliza o oponente 25%, ver depois
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail whilp!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_tomar.velocidade -= 75/100
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
            pass
        elif move == moves.quick_attack[0]:#deals damage
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail quitk attack!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
            
        elif move == moves.double_team[0]:#==growl(normal)
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail double team!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
            
        elif move == moves.slam[0]:#damage
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail slam!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.thunderbolt[0]:#damage e 10% paralizacao, incompleto
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail thunderbolt!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                if num <= 10:
                    pokemon_a_tomar.vida -= 1
                    pokemon_a_tomar.velocidade -= 75/100
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.agility[0]:#(vai ate o 6 no max)
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail agility!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        
        elif move == moves.thunder[0]:#damage e paraliza 30%
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail thunder!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                if num <= 30:
                    pokemon_a_tomar.vida -= 1
                    pokemon_a_tomar.velocidade -= 75/100
                    pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.light_screen[0]: #damage -50% de ataques especiais  
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail light screen!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                pokemon_a_tomar.especial_ataque -= 50/100
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.scratch[0]:#damage(nao especifica o n) com efeitos adicionais
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail scratch!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                pokemon_a_tomar.especial_ataque -= 10/100
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        # NOME DO MOVIMENTO ESCRITO ERRADO:
        
        #elif move == moves.bebbel:
        #    if tempo.etapa_turno == 0:
        #        mensagem.texto = "{} used tail bebbel!".format(pokemon_a_fazer.nome)
        #        tempo.etapa_turno_incrementa()
        #    elif tempo.etapa_turno == 1:
        #        pokemon_a_tomar.sumindo = True
        #        tempo.etapa_turno_incrementa()
        #    elif tempo.etapa_turno == 2:
        #        pokemon_a_tomar.ataque -= 1
        #        tempo.etapa_turno_incrementa()
        #    elif tempo.etapa_turno == 3:
        #        if len(turnos) > 0:
        #            turnos.pop(0)
        #        tempo.etapa_turno_reseta()
        
        elif move == moves.smokescreen[0]:#procurar na geração 3 depois
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail mokescreen!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.rage[0]:#normal
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail rage!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.scary_face[0]:#procurar na geração 3 depois
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail scary face!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.flamethrower[0]: #damage e 10% de chance de queimar
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail flamethrower!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                if num <= 10:
                    pokemon_a_tomar.vida -= 1/16
                    pokemon_a_tomar.ataque -= 1
                    pokemon_a_fazer.atacar(pokemon_a_tomar)
                    mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                    tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.dragon_rage[0]: #damage de -40HP 
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail dragon rage!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 40
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.fire_spin[0]: 
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail fire spin!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1/8
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()

        elif move == moves.tackle[0]:# power of 35 e 95% acerto
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tackle!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.vida -= 1
                pokemon_a_fazer.atacar(pokemon_a_tomar)
                mensagem.texto = "{} attack feel!".format(pokemon_a_tomar.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.leech_seed[0]:
            # Leech Seed plants a seed on the target that drains 1/8 of its maximum HP
            # at the end of each turn and restores it to the user, or any Pokémon that
            # takes its place. It does not work on Grass-type Pokémon; it does
            # technically work against Pokémon with the Magic Guard ability, but no HP
            #  will be sapped.
            if tempo.etapa_turno == 0:
                # mensagem:
                mensagem.texto = "{} used leech seed!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                # animação
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                # a ação em si
                pokemon_a_tomar.sumindo = False
                if not tipos.grass in pokemon_a_tomar.tipos:
                    pokemon_a_tomar.add_effect(effect.leech_seed)
                else:
                    mensagem.texto = "It didn't work!"
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.vine_whip[0]:# poder com base 35 + damage(numero nao identificado)
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail vine whip!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                pokemon_a_tomar.especial_ataque -= 10/100
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.poison_powder[0]:# o inimigo perde 1/8 de hp
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail poison powder!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1/8
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.sleep_powder[0]:#oponente dorme(não joga) por 3 turnos
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail sleep powder!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
                
        elif move == moves.razor_leaf[0]:#dano e tem uma taxa de acerto crítico aumentada (1⁄8 em vez de 1⁄24) a parte critica precisa ser feita.
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail razor leaf!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1/8
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.sweet_scent[0]:#procurar na 3 geração
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail sweet scent!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()

        elif move == moves.growth[0]:#normal,mas aumenta em estagios, entao quando resolver se vai ter loop rever isso
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail growth!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.synthesis[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail synthesis!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
            
        elif move == moves.solar_beam[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail solar beam!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.ember[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used ember!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
            
        elif move == moves.withdraw[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail withdraw!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
                
        elif move == moves.water_gun[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail water gun!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
            
        elif move == moves.bite:
            if tempo.etapa_turno == [0]:
                mensagem.texto = "{} used tail bite!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.rapid_spin:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail rapid spin!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
                
        elif move == moves.protect:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail protect!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.rain_dance:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail rain dance!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
                    
        elif move == moves.skull_bash:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail skull bash!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
        
        elif move == moves.hydro_pump:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail hydro pump!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()

        elif move == moves.fury_attack:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail fury attack!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()

        elif move == moves.horn_attack:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail horn attack!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()
           
        elif move == moves.stomp:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail stomp!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()

        elif move == moves.rock_blast:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail rock blast!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()

        elif move == moves.horn_drill:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail horn drill!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()

        elif move == moves.take_down:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail take down!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  

        elif move == moves.earthquake[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail earthquake!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
            
        elif move == moves.megahorn[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail take megahorn!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.hypnosis[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail take hypnosis!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.lick[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail lick!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.spite[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail spite!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.curse[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail curse!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.night_shade[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail take night shade!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
   
        elif move == moves.confuse_ray[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail confuse ray!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.shadow_punch[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail shadow punch!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.dream_eater[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail dream eater!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.destiny_bond[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail destiny bond!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.shadow_ball[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail shadow ball!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.nightmare[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail nightmare!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.mean_look[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail mean look!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.leer[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail leer!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.twister[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail twister!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.wrap[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail wrap!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.safeguard[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail safeguard!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.wing_attack[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail wing attack!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.outrage[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail outrage!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.hyperbeam[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail hyperbeam!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.confusion[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail confusion!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.disable[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail disable!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.mist[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail mist!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.swift[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail swift!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.psychic[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail psychic!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.psych_up[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail psych up!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.recover[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail recover!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
            
        elif move == moves.future_sight[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail future sight!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  
        
        elif move == moves.amnesia[0]:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} used tail amnesia!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                pokemon_a_tomar.sumindo = True
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 2:
                pokemon_a_tomar.ataque -= 1
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 3:
                if len(turnos) > 0:
                    turnos.pop(0)
                tempo.etapa_turno_reseta()  

        elif move == Acao.fugir:
            if tempo.etapa_turno == 0:
                mensagem.texto = "{} tries escape!".format(pokemon_a_fazer.nome)
                tempo.etapa_turno_incrementa()
            elif tempo.etapa_turno == 1:
                fugiu = pokemon_a_fazer.fugir_de(pokemon_a_tomar)
                if fugiu:
                    mensagem.texto = "{} escaped sucessful!".format(pokemon_a_fazer.nome)
                    for _ in range(len(turnos)):
                        turnos.pop(0)
                    tempo.etapa_turno_reseta()
                else:
                    mensagem.texto = "{} failed to escape!".format(pokemon_a_fazer.nome)
                    if len(turnos) > 0:
                        turnos.pop(0)
                    tempo.etapa_turno_reseta()
        # resetar o tempo:
        tempo.resetar()  
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
                            fazer_acao(menu, sub_menu, pokemons[0].movimentos[pos.i][0])
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