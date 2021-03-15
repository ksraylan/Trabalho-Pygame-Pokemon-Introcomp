import random
import pygame
import janela
import pokemon
import arquivos as arq
import cores as cor
import cena

def main():
    menu = cena.Menu()
    sub_menu = cena.Submenu()
    

    escala = arq.escala
    # menu espaçamento:
    
    menu_espacamento = (200,50)
    # tamanho menu:
    menu_tamanho = 2*escala
    # tamanho seta:
    tamanho_cursor = 11*escala

    # Pokémon selecionado (tela de seleção de pokémon):
    sel_s = 0
    
    pos = [0,0]
    distanciamento = (50*escala,15*escala)
    generos = ["F", "M"]

    pk_pikachu = pokemon.Pokemon("Pikachu",35,55,40,90,50,50,9,random.choice(generos), arq.carregar_imagem_pokemon(25))
    pk_charmander = pokemon.Pokemon("Charmander",39,52,43,65,60,50,9, random.choice(generos),arq.carregar_imagem_pokemon(4))
    pk_bulbasaur = pokemon.Pokemon("Bulbasaur",45,49,49,45,65,65,9, random.choice(generos),arq.carregar_imagem_pokemon(1))
    pk_squirtle = pokemon.Pokemon("Squirtle",44,48,65,43,50,64, 9,random.choice(generos),arq.carregar_imagem_pokemon(7))
    pk_rhydon = pokemon.Pokemon("Rhydon",105,130,120,40,45,45,9,random.choice(generos),arq.carregar_imagem_pokemon(112))
    pk_gengar = pokemon.Pokemon("Gengar",60,65,60,110,130,75,9,random.choice(generos),arq.carregar_imagem_pokemon(94))
    pk_dragonite = pokemon.Pokemon("Dragonite",91,134,95,80,100,100,9, random.choice(generos),arq.carregar_imagem_pokemon(149))
    pk_mewtwo = pokemon.Pokemon("Mewtwo",106,110,90,130,154,90,9,random.choice(generos),arq.carregar_imagem_pokemon(150))
    
    pokemons_pode_escolher = [pk_pikachu, pk_charmander, pk_bulbasaur, pk_squirtle, pk_rhydon, pk_gengar, pk_dragonite, pk_mewtwo]
    cores_pode_escolher = [cor.AMARELO, cor.LARANJA, cor.VERDE, cor.AZUL, cor.CIANO, cor.ROXO, cor.ROSA, cor.CINZA]


    pokemons = [pk_pikachu, pk_rhydon]
    pk_pikachu.atacar(pk_rhydon)

    def texto_multilinha(texto):
        x = 0
        y = 0
        for i in range(len(texto)):

            t = arq.fonte_txt.render(texto[i], True, cor.BRANCO)
            t_rect = t.get_rect()
            coordenada_x = 0 + 16*escala + t_rect.width*x

            if coordenada_x > janela.tamanho[0]/2:
                x = 0
                y -= 1
                coordenada_x = 0 + 16*escala + t_rect.width*x

            t_rect.left = coordenada_x
            t_rect.bottom = janela.tamanho[1] - 25*escala - y*t_rect.height
            janela.tela.blit(t, t_rect)
            x += 1
            
    def desenhar_graficos():
        #menu inicio:
        txt = "Escolha o seu pokémon"# Choose your pokémon
        
        #limpar a tela:
        janela.tela.fill(cor.PRETO)
        
        if menu.no_menu(menu.escolhendo_pokemon):
            # Fonte:
            superf = arq.fonte.render(txt, True, cor.BRANCO)
            superf_rect = superf.get_rect()
            superf_rect.center =(janela.tamanho[0]/2, 100)
            janela.tela.blit(superf, superf_rect)

            # posicao do nome que está sendo selecionado:
            

            # espacamento entre os nomes:
            e_n = 32
            # posicao y da seta dentro do retangulo:
            li = 100-e_n + (e_n*sel_s)

            # espaçamento x na esquerda da seta:
            e_s_x = 16

            # seta de seleção:
            pygame.draw.polygon(janela.tela, cor.VERMELHO, ( (menu_espacamento[0] + e_s_x, menu_espacamento[1] + li), (menu_espacamento[0] + e_s_x,menu_espacamento[1] + tamanho_cursor + li), (menu_espacamento[0] + e_s_x+ tamanho_cursor/2, menu_espacamento[1] + tamanho_cursor/2 + li) ) )

            # loop que vai percorrer a lista com os nomes dos pokemons:
            for i in range( len(pokemons_pode_escolher) ):
                # aqui vamos criar um texto com o pokemon "i" (o "i" que vai até o range do loop):
                superf = arq.fonte.render(pokemons_pode_escolher[i].nome, True, cores_pode_escolher[i])
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
            janela.tela.blit(pokemons[1].imagem_frente, (janela.tamanho[0] - 100*escala,20*escala))
            # seu pokemon:
            janela.tela.blit(pokemons[0].imagem_costas, (25*escala,janela.tamanho[1] - 95*escala))

            # Menus:
            janela.tela.blit(arq.img_text_bar, (0, janela.tamanho[1] - 48*escala))
            if sub_menu.no_submenu(sub_menu.principal):
                janela.tela.blit(arq.img_opcoes_batalha, (janela.tamanho[0] - 120*escala, janela.tamanho[1] - 48*escala))
            elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                pass
            pygame.draw.rect(janela.tela, cor.VERMELHO, ((janela.tamanho[0] - 107.5*escala + (pos[0]*distanciamento[0]), janela.tamanho[1] - 37.5*escala + (pos[1]*distanciamento[1])), (50*escala,15*escala)), int(1*escala))
            nome_na_batalha = "What should {} do?".format(pokemons[0].nome)
            batalha_nome = arq.fonte_txt.render(nome_na_batalha, True, cor.BRANCO)
            batalha_rect = batalha_nome.get_rect()
            batalha_rect.left = 0 + 16*escala
            batalha_rect.bottom = janela.tamanho[1] - 25*escala

            janela.tela.blit(arq.img_barra1, (15*escala, 18*escala))
            janela.tela.blit(arq.img_barra2, (janela.tamanho[0] - 110*escala,janela.tamanho[1] - 88*escala))

            # nomes dos pokemons renderizados na barra:
            poke_2 = arq.fonte.render(pokemons[1].nome, True, cor.PRETO)
            poke_2_rect = poke_2.get_rect()
            poke_2_rect.center =(48.5*escala, 25*escala)
            janela.tela.blit(poke_2, poke_2_rect)

            poke_1 = arq.fonte.render(pokemons[0].nome, True, cor.PRETO)
            poke_1_rect = poke_1.get_rect()
            poke_1_rect.center =((janela.tamanho[0] - 68*escala), janela.tamanho[1] - 77.5*escala)
            janela.tela.blit(poke_1, poke_1_rect)

            texto = ""
            a_cor = cor.PRETO

            if pokemons[0].genero == "F":
                texto, a_cor = "♀", cor.ROSA
            elif pokemons[1].genero == "M":
                texto, a_cor = "♂", cor.AZUL
            simb_1 = arq.fonte.render(texto, True, a_cor)
            simb_1_rect = simb_1.get_rect()
            simb_1_rect.left = poke_1_rect.width + poke_1_rect.x
            simb_1_rect.top = poke_1_rect.y
            janela.tela.blit(simb_1, simb_1_rect)

            
            texto = ""
            a_cor = cor.PRETO

            if pokemons[1].genero == "F":
                texto, a_cor = "♀", cor.ROSA
            elif pokemons[1].genero == "M":
                texto, a_cor = "♂", cor.AZUL
            simb_2 = arq.fonte.render(texto, True, a_cor)
            simb_2_rect = simb_2.get_rect()
            simb_2_rect.left = poke_2_rect.width + poke_2_rect.x
            simb_2_rect.top = poke_2_rect.y
            janela.tela.blit(simb_2, simb_2_rect)            


            # Mostrando o nível do pokémon
            nivel = arq.fonte_txt.render("9", True, cor.PRETO)
            nivel_rect = nivel.get_rect()
            nivel_rect.left = 96*escala
            nivel_rect.top = 18.5*escala
            janela.tela.blit(nivel, nivel_rect)
            nivel = arq.fonte_txt.render("9", True, cor.PRETO)
            nivel_rect = nivel.get_rect()
            nivel_rect.left = janela.tamanho[0] - 21*escala
            nivel_rect.top = janela.tamanho[1] - 84.5*escala
            janela.tela.blit(nivel, nivel_rect)

            texto_multilinha(nome_na_batalha)
            #janela.tela.blit(batalha_nome, batalha_rect)

        pygame.display.update()


    def escolher_pokemon(menu, sub_menu):
        menu.atual = menu.batalhando
        sub_menu.atual = sub_menu.principal
        # seu pokémon:
        pokemons[0] = pokemons_pode_escolher[sel_s]
        # pokémon inimigo:
        pokemons[1] = pokemons_pode_escolher[random.randrange(0,len(pokemons_pode_escolher)-1)]
        
        



    def escolher_acao_batalha():
        if pos == [0,0]:
            #subcena_atual = cena.SUBMENU_BATALHA_ATAQUE
            vez = random.randrange(1,2)
            if pokemons[0].velocidade > pokemons[1].velocidade:
                vez = 1
            elif pokemons[0].velocidade < pokemons[1].velocidade:
                vez = 2

            while vez <= 2:
                if vez == 1:
                    pokemons[0].atacar(pokemons[1])
                elif vez == 2:
                    pokemons[1].atacar(pokemons[0])

                vez += 1
            #pokemon_2 = pokemon_1.atacar(pokemon_2)
            #pokemon_2.atacar(pokemon_1)
            
    def processar_logica():
        pass

    rodando_o_jogo = True

    # Loop do jogo:
    while rodando_o_jogo:
        # Eventos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando_o_jogo = False
            # Se uma tecla foi pressionada:
            if event.type == pygame.KEYDOWN:
                if menu.no_menu(menu.batalhando):
                    if sub_menu.no_submenu(sub_menu.principal):
                        if event.key == pygame.K_UP:
                            pos[1] = 0
                        elif event.key == pygame.K_DOWN:
                            pos[1] = 1
                        elif event.key == pygame.K_LEFT:
                            pos[0] = 0
                        elif event.key == pygame.K_RIGHT:
                            pos[0] = 1
                        
                        elif event.key == pygame.K_ESCAPE:
                            menu.atual = menu.escolhendo_pokemon
                        

                        if event.key == pygame.K_RETURN:
                            escolher_acao_batalha()


                    elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                        pass
                    
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
                        escolher_pokemon(menu, sub_menu)
                    elif event.key == pygame.K_ESCAPE:
                        rodando_o_jogo = False
            
        desenhar_graficos()
        processar_logica()

    # Sair do pygame:
    pygame.quit()

if __name__ == "__main__":
    main()
