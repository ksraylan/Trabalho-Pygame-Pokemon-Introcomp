import janela
import pygame
import pokemon
import arquivos as arq
import cores as cor

cena_atual = "escolher_pokemon"

def main():
    escala = arq.escala
    # menu espaçamento:
    m_e = (200,50)
    # tamanho menu:
    t_m = 2*escala
    # tamanho seta:
    t_s = 11*escala

    sel_s = 0
    pokemons = ["PIKACHU","CHARMANDER","BULBASAUR","SQUIRTLE", "RHYDON","GENGAR", "DRAGONITE", "MEWTWO"]
    cores = [cor.AMARELO, cor.LARANJA, cor.VERDE, cor.AZUL, cor.CIANO, cor.ROXO, cor.ROSA, cor.CINZA]

    pos = [0,0]
    distanciamento = (50*escala,15*escala)

    #debug = True

    # seu pokémon:
    pokemon_1 = pokemon.Pokemon("Pikachu", 100, 20, arq.img_pokemons[24][0], arq.img_pokemons[24][1])
    # pokémon inimigo:
    pokemon_2 = pokemon.Pokemon("Não sei", 100, 20, arq.img_pokemons[120][0], arq.img_pokemons[120][1])

    def texto_multilinha(texto):
        global debug
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
        txt = "Choose your pokémon"
        tela_do_menu = cor.PRETO
        
        
        #limpar a tela:
        janela.tela.fill(cor.PRETO)
        
        if cena_atual == "escolher_pokemon":
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
            pygame.draw.polygon(janela.tela, cor.VERMELHO, ( (m_e[0] + e_s_x, m_e[1] + li), (m_e[0] + e_s_x,m_e[1] + t_s + li), (m_e[0] + e_s_x+ t_s/2, m_e[1] + t_s/2 + li) ) )

            # loop que vai percorrer a lista com os nomes dos pokemons:
            for i in range( len(pokemons) ):
                # aqui vamos criar um texto com o pokemon "i" (o "i" que vai até o range do loop):
                superf = arq.fonte.render(pokemons[i], True, cores[i])
                # Pegaremos as dimensões do texto que criamos acima:
                superf_rect = superf.get_rect()
                # Colocaremos no centro, e pegamos o espaçamento e multiplicamos por "i", para os nomes dos pokemons irem para baixo e não ficarem um em cima do outro:
                superf_rect.center =(janela.tamanho[0]/2, 100 + e_n + i*e_n)
                # Por fim, mostraremos na tela o texto:
                janela.tela.blit(superf, superf_rect)
            
            
            #pygame.draw.rect(tela, BRANCO, ( m_e , ((m_e[0]-janela.tamanho[0]),(m_e[1]-janela.tamanho[1]) ) ))
            pygame.draw.rect(janela.tela, cor.BRANCO, ((m_e[0],m_e[1]),(janela.tamanho[0]-(m_e[0]*2),janela.tamanho[1]-(m_e[1]*2))), 5)
        elif cena_atual == "batalha":
            # Cena de batalha:
            #tela.blit(imagem, (x, y))
            janela.tela.blit(arq.img_fundo_pokemon,(0,0))
            
            
            # (x, y)
            
            # img_pokemons[n_do_pokemon][0 = frente, 1 = costas]
            # pokemon inimigo:
            janela.tela.blit(arq.img_pokemons[24][0], (janela.tamanho[0] - 100*escala,20*escala))
            # seu pokemon:
            janela.tela.blit(arq.img_pokemons[24][1], (25*escala,janela.tamanho[1] - 95*escala))

            janela.tela.blit(arq.img_text_bar, (0, janela.tamanho[1] - 48*escala))
            janela.tela.blit(arq.img_opcoes_batalha, (janela.tamanho[0] - 120*escala, janela.tamanho[1] - 48*escala))

            pygame.draw.rect(janela.tela, cor.VERMELHO, ((janela.tamanho[0] - 107.5*escala + (pos[0]*distanciamento[0]), janela.tamanho[1] - 37.5*escala + (pos[1]*distanciamento[1])), (50*escala,15*escala)), int(1*escala))
            nome_na_batalha = "What should KADABRA do?"
            batalha_nome = arq.fonte_txt.render(nome_na_batalha, True, cor.BRANCO)
            batalha_rect = batalha_nome.get_rect()
            batalha_rect.left = 0 + 16*escala
            batalha_rect.bottom = janela.tamanho[1] - 25*escala

            janela.tela.blit(arq.img_barra1, (15*escala, 18*escala))
            janela.tela.blit(arq.img_barra2, (janela.tamanho[0] - 110*escala,janela.tamanho[1] - 88*escala))

            # nomes dos pokemons renderizados na barra:
            poke_1 = arq.fonte.render(pokemon_2.nome, True, cor.PRETO)
            poke_1_rect = poke_1.get_rect()
            poke_1_rect.center =(48.5*escala, 25*escala)
            janela.tela.blit(poke_1, poke_1_rect)

            simb_1 = arq.fonte.render("♀", True, cor.ROSA)
            simb_1_rect = simb_1.get_rect()
            simb_1_rect.left = poke_1_rect.width + poke_1_rect.x
            simb_1_rect.top = poke_1_rect.y
            janela.tela.blit(simb_1, simb_1_rect)

            poke_2 = arq.fonte.render(pokemon_1.nome, True, cor.PRETO)
            poke_2_rect = poke_2.get_rect()
            poke_2_rect.center =((janela.tamanho[0] - 68*escala), janela.tamanho[1] - 77.5*escala)
            janela.tela.blit(poke_2, poke_2_rect)

            simb_2 = arq.fonte.render("♂", True, cor.AZUL)
            simb_2_rect = simb_2.get_rect()
            simb_2_rect.left = poke_2_rect.width + poke_2_rect.x
            simb_2_rect.top = poke_2_rect.y
            janela.tela.blit(simb_2, simb_2_rect)            

            # renderizando o nível do pokémon:

            # ♀, ♂



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


    def escolher_pokemon():
        global cena_atual
        cena_atual = "batalha"

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
                            sel_s = len(pokemons) - 1
                    elif event.key == pygame.K_DOWN:
                        sel_s = sel_s + 1
                        if sel_s > len(pokemons) - 1:
                            sel_s = 0
                    elif event.key == pygame.K_RETURN:
                        escolher_pokemon()
            
        desenhar_graficos()
        processar_logica()

    # Sair do pygame:
    pygame.quit()

if __name__ == "__main__":
    main()
