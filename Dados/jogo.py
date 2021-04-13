# Importações:
# Biblioteca que randomiza números:
import random

# Biblioteca mais importante, sem ela não poderíamos renderizar imagens na tela:
import pygame

# Arquivos com imagens, sons, etc.
import Dados.arquivos as arq
# Cena: menu e sub menu atual:
import Dados.cena as cena
# Importando as cores que temos:
import Dados.cores as cor
# Possui as configurações da janela:
import Dados.janela as janela
# Categoria dos movimentos:
from Dados.category import Category
# Condição irá nos mostrar a condição do jogo:
from Dados.condicao import Condicao
# Importar o Easter Egg:
from Dados.easter_egg import EasterEgg
# Efeitos que os pokémons podem ter:
from Dados.effect import Effect
# Itens usáveis:
from Dados.itens import Itens
# Mensagem é o que mostra o que está acontecendo na tela:
from Dados.mensagem import Mensagem
# Movimentos dos pokémons:
from Dados.moves import Moves
# Tipos de movimentos e pokémons:
from Dados.poke_types import Types
# As propriedades dos Pokémons:
from Dados.pokemon import Pokemon
# Posição é as configurações do cursor:
from Dados.posicao import Pos
# Função que processa cada movimento:
from Dados.processar_movimentos import process_moves
# Tempo irá gerenciar os milisegundos de cada condição:
from Dados.tempo import Tempo


# Função do jogo principal:
def main():
    # Objeto itens que tem os itens usáveis:
    itens = Itens()
    # Objeto category que possui as categorias dos movimentos:
    category = Category()
    # Objeto effect tem os efeitos que são aplicados no pokémon pelo oponente:
    effect = Effect()
    # Objeto menu que vai nos dizer o menu atual, se está em um menu específico
    # e todos os menus existentes:
    menu = cena.Menu()
    # Objeto sub_menu será a mesma lógica do objeto menu:
    sub_menu = cena.Submenu()
    # Objeto mensagem nos passa o texto dela e a posição do caractere atual na animação
    # de "escrevendo" na tela:
    mensagem = Mensagem()
    # Pega a escala do arquivos.py:
    escala = arq.escala
    # Menu espaçamento:
    menu_espacamento = (200, 50)
    # Tamanho seta:
    tamanho_cursor = 11 * escala
    # Objeto pos possui a posição da seta atual, seu item selecionado, e a "grade" que pode
    # se "locomover": 
    pos = Pos(1, 8)
    # Distanciamento entre as opções de escolha:
    distanciamento = (50 * escala, 15 * escala)
    # Relógio do jogo:
    clock = pygame.time.Clock()
    # Objeto condicao possui a condição atual do jogo:
    condicao = Condicao()
    # Objeto tipos possui os tipos dos movimentos:
    tipos = Types()
    # Objeto moves possui todos os movimentos que os pokémons podem fazer nesse jogo:
    moves = Moves()
    # Cria o objeto do Easter Egg:
    easter_egg = EasterEgg()

    # Lista com os itens que cada pokémon irá ter em suas mochilas:
    itens_usados = [itens.dire_hit, itens.guard_spec, itens.x_accuracy, itens.x_attack, itens.x_defense,
                    itens.x_special, itens.x_speed, itens.berry_juice, itens.elixir, itens.potion]

    # Lista dos pokémons e seus movimentos e outras propriedades:
    # Ver a classe Pokémon localizada em pokemon.py para mais informações.
    # Pikachu:
    pk_pikachu = Pokemon("Pikachu", 35, 55, 40, 90, 50, 50, 15, 50,
                         [tipos.normal], [moves.growl, moves.thunder_shock, moves.tail_whip, moves.thunder_wave],
                         itens_usados.copy(),
                         25, False)
    # Charmander:
    pk_charmander = Pokemon("Charmander", 39, 52, 43, 65, 60, 50, 15, 12.5,
                            [tipos.fire], [moves.growl, moves.scratch, moves.ember, moves.metal_claw],
                            itens_usados.copy(),
                            4, False)
    # Bulbasaur:
    pk_bulbasaur = Pokemon("Bulbasaur", 45, 49, 49, 45, 65, 65, 15, 12.5,
                           [tipos.grass, tipos.poison], [moves.tackle, moves.growl, moves.leech_seed, moves.vine_whip],
                           itens_usados.copy(),
                           1, False)
    # Squirtle:
    pk_squirtle = Pokemon("Squirtle", 44, 48, 65, 43, 50, 64, 15, 12.5,
                          [tipos.water], [moves.tackle, moves.tail_whip, moves.bubble, moves.withdraw],
                          itens_usados.copy(),
                          7, False)
    # Rhyhorn:
    pk_rhyhorn = Pokemon("Rhyhorn", 80, 85, 95, 25, 30, 30, 15, 50,
                         [tipos.ground, tipos.rock],
                         [moves.fury_attack, moves.horn_attack, moves.stomp, moves.tail_whip], itens_usados.copy(),
                         111, False)
    # Gastly:
    pk_gastly = Pokemon("Gastly", 30, 35, 30, 80, 100, 35, 15, 50, [tipos.ghost, tipos.poison],
                        [moves.hypnosis, moves.lick, moves.spite, moves.curse], itens_usados.copy(),
                        92, False)
    # Dratini:
    pk_dratini = Pokemon("Dratini", 41, 64, 45, 50, 50, 50, 15, 50,
                         [tipos.dragon, tipos.flying], [moves.leer, moves.thunder_wave, moves.twister, moves.wrap],
                         itens_usados.copy(),
                         147, False)
    # Mewtwo:
    pk_mewtwo = Pokemon("Mewtwo", 106, 110, 90, 130, 154, 90, 22, None,
                        [tipos.psychic], [moves.confusion, moves.disable, moves.barrier, moves.mist],
                        itens_usados.copy(),
                        150, False)

    # Easter egg:
    # Nome, vida, ataque, defesa, velocidade, especial_ataque,
    # especial_defesa, nivel, genero, tipos, movimentos, itens, imagens

    # Marco:
    pk_marco = Pokemon("Marco", 199, 170, 180, 500, 180, 180, 99, "M", [tipos.normal],
                       [moves.tackle, moves.fury_attack, moves.hypnosis, moves.spite], itens_usados, "marco", True)
    # Jorge:
    pk_jorge = Pokemon("Jorge", 200, 180, 190, 200, 205, 530, 99, "M", [tipos.normal],
                       [moves.confusion, moves.fury_attack, moves.curse, moves.twister], itens_usados, "jorge", True)
    # Bea:
    pk_bea = Pokemon("Bea", 201, 190, 170, 300, 150, 190, 99, "F", [tipos.normal],
                     [moves.thunder_wave, moves.disable, moves.twister, moves.mist], itens_usados, "bea", True)
    # André:
    pk_andre = Pokemon("André", 200, 145, 500, 220, 190, 230, 99, "M", [tipos.normal],
                       [moves.bubble, moves.vine_whip, moves.leer, moves.struggle], itens_usados, "andre", True)
    # Thiago:
    pk_thiago = Pokemon("Thiago", 200, 260, 150, 300, 170, 180, 99, "M", [tipos.normal],
                        [moves.ember, moves.withdraw, moves.lick, moves.metal_claw], itens_usados, "thiago", True)

    # Lista com os pokémons que podem ser escolhidos na tela de seleção de pokémon e suas cores abaixo.
    pokemons_pode_escolher = [pk_pikachu, pk_charmander, pk_bulbasaur, pk_squirtle, pk_rhyhorn, pk_gastly, pk_dratini,
                              pk_mewtwo]
    cores_pode_escolher = [cor.AMARELO, cor.LARANJA, cor.VERDE, cor.AZUL, cor.CIANO, cor.ROXO, cor.ROSA, cor.CINZA]

    # Começará com nenhum pokémon selecionado (obs: adicionado padrão):
    pokemons = [pk_pikachu.copy(), pk_bulbasaur.copy()]

    # Para que o texto possua mais de uma linha na quantidade que quiser e
    # que tenha animações:
    def texto_multilinha(texto):
        # Começaremos na posição x 0 e y 0:
        x = 0
        y = 0
        # s = onde está o último espaço processado (" "): 
        s = 0
        # Qual caractere do texto está atualmente:
        i = 0
        # Lista com os caracteres que vão ser renderizados:
        t = []
        # Caso a mensagem for maior que o espaço, o texto utilizará outra linha.
        # Percorreremos os caracteres até a posição máxima dele, para ser criado
        # uma "animação" de texto escrevendo:
        while i < mensagem.texto_posicao:
            # Pega o caractere atual que está sendo percorrido:
            t_local = arq.fonte_txt.render(texto[i], False, cor.BRANCO)
            # Pega também o tamanho dele:
            t_rect = t_local.get_rect()
            # E processa em que posição x vai ficar ele:
            # 12*escala: posição onde começará o texto.
            # t_rect.width*x: largura do caractere atual vezes a posição x:
            coordenada_x = 12 * escala + t_rect.width * x
            # Se o caractere atual for um espaço:
            if texto[i] == " ":
                # Armazena no "s" o último espaço encontrado.
                # Isso servirá para fazer quebra de linha sem "desmontar" as palavras.
                s = i
            # Se a coordenada x atual do texto for maior que a metade da largura da tela
            # menos a largura do caractere atual:
            if coordenada_x > janela.tamanho[0] / 2 - t_rect.width:
                # A gente faz a quebra de linha, resetando a posição x:
                x = 0
                # E pulando para a próxima linha:
                y -= 1
                # E remove os caracteres da palavra atual para não dar quebra de linha "quebrando"
                # as palavras:
                # Percorrendo do caractere atual até o último espaço:
                for _ in range(i, s, -1):
                    # Para ter certeza que não ocorrerá erros, verificamos se último caractere de espaço
                    # encontrado é menor que o tamanho da lista dos caracteres que vão ser renderizados:
                    if s < len(t):
                        # Remove ele, ai quando remover vai "reorganizar" a lista, ou seja, não vai ter
                        # "espaços vazios":
                        t.pop(s)
                # Agora a gente avança para o próximo caractere de novo a partir do espaço, ou seja, começaremos
                # do primeiro caractere da palavra:
                i = s + 1
                # E resetamos o último espaço:
                # s = 0
                # Recalcular a coordenada x onde ficará o caractere atual:
                coordenada_x = 12 * escala + t_rect.width * x
                # E colocar ele para ser renderizado depois:
                t_local = arq.fonte_txt.render(texto[i], False, cor.BRANCO)
            # A posição x:
            t_rect.left = coordenada_x
            # E a posição y:
            # 28*escala: posição y inicial
            # y*t_rect.height: posição y vezes a altura do caractere
            t_rect.bottom = janela.tamanho[1] - 28 * escala - y * t_rect.height
            # Adiciona ele na lista de caracteres para ser renderizados depois:
            t.append([t_local, t_rect])
            # Próxima posição x:
            x += 1
            # E próximo caractere:
            i += 1
        # No final, depois de calcular as posições de cada caractere, apenas renderizar eles:
        for i in range(len(t)):
            # Colocando caractere por caractere na tela:
            janela.tela.blit(t[i][0], t[i][1])

    # Função que toca uma música:
    def tocar_musica(caminho, repetir):
        # Caminho: qual o caminho que leva até o arquivo da música.
        # Para a música (se estiver tocando alguma):
        pygame.mixer.music.stop()
        # Carrega a música pelo caminho.
        pygame.mixer.music.load(caminho)
        # Começa a tocar a música,
        # se pediu para repetir:
        if repetir:
            pygame.mixer.music.play(-1)
        # Caso contrário, não repetir:
        else:
            pygame.mixer.music.play()

    # Coloca para tocar a música de abertura:
    tocar_musica("Dados/Recursos/Sprites/SonsPokemon/fireRedAbertura.wav", True)

    # Tamanho da barra de vida:
    barra_width = arq.img_vida_vermelha.get_width() * 5.34

    # Função que permite que o som toque:
    def tocar_sons():
        # Condição para que a música da vitória toque:
        if condicao.atual == condicao.vitoria:
            arq.som_vitoria.play()
        # Condição para que a música da derrota toque:
        if condicao.atual == condicao.derrota:
            arq.som_derrota.play()

    # Metade da tela na horizontal:
    width_dividido = janela.tamanho[0] / 2
    # Espaçamento x na esquerda da seta:
    e_s_x = 16
    # Espaçamento entre os nomes:
    e_n = 32

    # Determina a posição e o tamanho da barra sem vida:
    def barra_sem_vida_calculo_escala(x, width, qual_vida=1):
        # Pega a posição x e converte para int:
        x = int(x)
        # E a largura em int:
        width = int(width)
        formula = x + width
        # Posição máxima que o x + width deve ter:
        # Se for a vida do pokémons[1]:
        if qual_vida == 1:
            pos_x_maximo = 102.6 * escala
        # Se for a vida do pokémons[0]:
        else:
            pos_x_maximo = 225.6 * escala
        if formula <= pos_x_maximo:
            # Aumenta em + 1:
            width += 1
            # Isso porque às vezes acontece da barra sem vida ser um pouco menor
            # do que devia, ai mostraria um pixel verde do lado direito dessa barra,
            # ai não seria agradável, então a solução que conseguimos foi essa, ou melhor
            # dizendo, a barra sem vida fica "tremendo" quando animada.
        # No final, retorna o x e width "corrigidos":
        return int(x), int(width)

    # Confere se o pokemon teve um movimento bloqueado:
    def obter_id_bloqueados(pokemon):
        id_bloqueados = []
        # Percorre toda a lista de bloqueados:
        for i in range(len(pokemon.movimentos_bloqueados)):
            # Obteremos somente a id do movimento para depois comparar com "in":
            """
            index = -1
            for a in range(len(pokemon.movimentos)):
                # Procura o movimento bloqueado na lista de movimentos:
                if pokemon.movimentos_bloqueados[i][0] == pokemon.movimentos[a][0]:
                    # Obter o index:
                    index = a
                    # Não precisa continuar a procura:
                    break
            """
            id_bloqueados.append(pokemon.movimentos[i][0])

        # Retorna somente os bloqueados:
        return id_bloqueados

    def movimentos_sem_pp_index(pokemon):
        movimentos = []
        # Percorre a lista de movimentos:
        for i in range(len(pokemon.movimentos)):
            if not pokemon.movimentos[i][2] > 0:  # se não tiver pp:
                # Coloca na lista:
                movimentos.append(i)

        # Retorna os movimentos sem pp:
        return movimentos

    def somente_movimentos_disponiveis(pokemon):
        # Pega os id's dos movimentos bloqueados:
        id_bloqueados = obter_id_bloqueados(pokemon)
        # Obtém o index na lista onde está o id bloqueado:
        id_bloqueados_index = []
        for i in range(len(pokemon.movimentos)):
            if pokemon.movimentos[i][0] in id_bloqueados:
                id_bloqueados_index.append(i)

        # E dos movimentos sem pp:
        sem_pp_index = movimentos_sem_pp_index(pokemon)

        id_movimentos_index = []
        # Pega somente os índices dos movimentos do pokémon:
        for i in range(len(pokemon.movimentos)):
            id_movimentos_index.append(i)
        nao_pode_usar = []
        nao_pode_usar.extend(id_bloqueados_index)
        nao_pode_usar.extend(sem_pp_index)

        for i in range(len(nao_pode_usar)):
            # Remove todos os items de id_movimentos_index que estão na lista
            # nao_pode_usar:
            while nao_pode_usar[i] in id_movimentos_index:
                id_movimentos_index.remove(nao_pode_usar[i])

                # E retorna só os que podem ser usados:
        return id_movimentos_index

    # Função que desenha os gráficos:
    def desenhar_graficos():
        # Limpa a tela de preto:
        janela.tela.fill(cor.PRETO)
        # Se estiver no menu de escolha de pokémons:      
        if menu.no_menu(menu.escolhendo_pokemon):
            # Renderiza a fonte:
            superficie = arq.fonte.render("Escolha o seu pokémon", False, cor.BRANCO)
            # Obtém o tamanho:
            superficie_rect = superficie.get_rect()
            # Centraliza ela no meio horizontal (x, y):
            superficie_rect.center = (width_dividido, 10 * escala)
            # Coloca na tela a mesma:
            janela.tela.blit(superficie, superficie_rect)

            # Posição y da seta dentro do retângulo:
            li = (e_n * pos.y) + e_n

            # Renderizando a seta de seleção de acordo:
            pygame.draw.polygon(janela.tela, cor.VERMELHO, ((menu_espacamento[0] + e_s_x,
                                                             menu_espacamento[1] + li),
                                                            (menu_espacamento[0] + e_s_x, menu_espacamento[1] +
                                                             tamanho_cursor + li),
                                                            (menu_espacamento[0] + e_s_x + tamanho_cursor / 2,
                                                             menu_espacamento[1] + tamanho_cursor / 2 + li)))

            # Loop que vai percorrer a lista com os nomes dos pokémons:
            for i in range(len(pokemons_pode_escolher)):
                # Aqui vamos criar um texto com o pokémon "i" (o "i" que vai até o range do loop):
                superficie = arq.fonte.render(pokemons_pode_escolher[i].nome, False,
                                              cores_pode_escolher[i])
                # Pegaremos as dimensões do texto que criamos acima:
                superficie_rect = superficie.get_rect()
                # Colocaremos no centro, e pegamos o espaçamento e multiplicamos por "i",
                # para os nomes dos pokémons irem para baixo e não ficarem um em cima do outro:
                superficie_rect.center = (janela.tamanho[0] / 2, 20 * escala + e_n + i * e_n)
                # Por fim, mostraremos na tela o texto:
                janela.tela.blit(superficie, superficie_rect)

            # Desenharemos na tela o retângulo branco que fica em volta dos nomes:
            pygame.draw.rect(janela.tela, cor.BRANCO, ((menu_espacamento[0], menu_espacamento[1]), (
                janela.tamanho[0] - (menu_espacamento[0] * 2), janela.tamanho[1] - (menu_espacamento[1] * 2))), 5)
        # Se estiver no menu de batalha:
        elif menu.no_menu(menu.batalhando):
            # Se for no menu da mochila, ou seja, de itens:
            if sub_menu.no_submenu(sub_menu.itens):
                # Desenha a imagem de fundo da tela de itens:
                janela.tela.blit(arq.img_bag, (0, (janela.tamanho[1] - arq.img_bag.get_height()) / 2))

                # Espaçamento entre os itens:
                esp = 16 * escala

                # Desenhando os nomes dos itens (temos que limitar a 5, pois é um sistema
                # de "páginas"):
                limite = 5

                # Sistema de descer e subir a "página":
                # Se a seta passou do último item da "página":
                while pos.y >= limite + pos.offset:
                    # pos.offset: deslocamento da página
                    pos.offset += 1
                # Se a seta está antes do primeiro item da "página":
                while pos.y < pos.offset:
                    pos.offset -= 1
                # O "i" é de qual item vai começar, ou seja, qual será o primeiro item que vai ser mostrado,
                # de acordo com a rolagem da "página":
                i = pos.offset
                # Será de "i" até o limite de quantidade de itens na tela mais o deslocamento da página:
                while i < limite + pos.offset:
                    # Por padrão, o item será o botão cancelar:
                    texto = "Cancelar"
                    # Se o item não for o primeiro da lista, então não é o botão "Cancelar":
                    if not i == 0:
                        # Obterá o nome do item de acordo com o i, mas a gente subtrai 1, pois temos fora da lista
                        # o botão "Cancelar":
                        texto = pokemons[0].itens[i - 1][1]
                    # Renderizaremos a fonte do item atual:
                    item_txt = arq.fonte.render(texto, False, cor.PRETO)
                    # Obteremos o tamanho do texto:
                    item_txt_rect = item_txt.get_rect()
                    # Colocaremos nessa posição:
                    # 100*escala: posição x dos nomes dos itens
                    # 30*escala: posição y inicial dos itens
                    # (i-pos.offset)*esp: (item atual menos o deslocamento da página) vezes o
                    # espaçamento entre os itens.
                    item_txt_rect.bottomleft = (100 * escala, 30 * escala + ((i - pos.offset) * esp))
                    # Mostrar na tela o texto:
                    janela.tela.blit(item_txt, item_txt_rect)
                    # Próximo item:
                    i += 1
                # Obtendo a posição y em que a seta vai ficar:
                li = tamanho_cursor / 2 + (esp * (pos.y - pos.offset))

                # Posição x que vai ficar o cursor:
                seta_x = 30 * escala

                # Desenhando a seta de seleção:
                pygame.draw.polygon(janela.tela, cor.PRETO, ((menu_espacamento[0] + seta_x,
                                                              esp + li), (menu_espacamento[0] + seta_x, esp +
                                                                          tamanho_cursor + li),
                                                             (menu_espacamento[0] + seta_x + tamanho_cursor / 2,
                                                              esp + tamanho_cursor / 2 + li)))
            else:
                # Estamos ou no sub menu principal, ou no sub menu de escolha do movimento,
                # ou o que mostra a ação, ou o de vitória, ou o de derrota.
                # Imagem de fundo da batalha:
                janela.tela.blit(arq.img_fundo_pokemon, (0, 0))

                # Desenhando os "círculos" que ficam em baixo de cada pokémon:
                janela.tela.blit(arq.img_fundo_pokemon_circulo1, (janela.tamanho[0] - 128 * escala +
                                                                  pokemons[1].circulo_offset * janela.tamanho[0],
                                                                  48 * escala))
                janela.tela.blit(arq.img_fundo_pokemon_circulo2, (4 * escala - pokemons[0].circulo_offset *
                                                                  janela.tamanho[0], janela.tamanho[1] - 59 * escala))

                # img_pokemons[n_do_pokemon][0 = frente, 1 = costas]
                # Pokémon inimigo:
                # Se ele não sumiu da tela (para a animação de sumir):
                if not pokemons[1].sumido:
                    # Desenha ele nas posições certas:
                    janela.tela.blit(pokemons[1].imagem_frente, (janela.tamanho[0] - 96 * escala +
                                                                 pokemons[1].deslocamento[0] * escala +
                                                                 pokemons[1].circulo_offset * janela.tamanho[0],
                                                                 72 * escala - pokemons[1].imagem_frente.get_height() +
                                                                 pokemons[1].deslocamento[1] * escala))
                # Mesma coisa com o seu pokémon:
                if not pokemons[0].sumido:
                    janela.tela.blit(pokemons[0].imagem_costas, (40 * escala + pokemons[0].deslocamento[0] *
                                                                 escala - pokemons[1].circulo_offset *
                                                                 janela.tamanho[0],
                                                                 janela.tamanho[1] - 48 * escala - pokemons[
                                                                     0].imagem_costas.get_height() +
                                                                 pokemons[0].deslocamento[1] * escala +
                                                                 pokemons[1].pos_offset * escala))

                # Desenhando a barra onde fica o texto que mostra o que está acontecendo:
                janela.tela.blit(arq.img_text_bar, (0, janela.tamanho[1] - 48 * escala))
                # Se está no sub menu principal, ou seja, aquele que você escolhe se quer lutar,
                # fugir, etc.
                if sub_menu.no_submenu(sub_menu.principal):
                    # Desenha a imagem que mostra as opções de batalha citadas no comentário
                    # anterior:
                    janela.tela.blit(arq.img_opcoes_batalha, (janela.tamanho[0] - 120 * escala,
                                                              janela.tamanho[1] - 48 * escala))

                    # Obtendo a posição x e y da seta de seleção:
                    ly = (distanciamento[1] * pos.y)
                    lx = (distanciamento[0] * pos.x)

                    # Pega a posição inicial que ficará a seta:
                    pos_inicial = (janela.tamanho[0] - 110 * escala, janela.tamanho[1] - 35 * escala)

                    # Desenha a mesma:
                    pygame.draw.polygon(janela.tela, cor.PRETO, ((pos_inicial[0] + lx,
                                                                  pos_inicial[1] + ly),
                                                                 (pos_inicial[0] + lx, pos_inicial[1] +
                                                                  tamanho_cursor + ly),
                                                                 (pos_inicial[0] + tamanho_cursor / 2 + lx,
                                                                  pos_inicial[1] + tamanho_cursor / 2 + ly)))
                # Se estiver no sub menu que escolhe o movimento:
                elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                    # Desenha a imagem que mostra o pp, tipo do movimento e o espaço vazio
                    # que ficará os movimentos:
                    janela.tela.blit(arq.img_pp_bar, (0, janela.tamanho[1] - 48 * escala))
                    # Agora desenhará os movimentos em si:
                    # Começa na posição x = 0 e y = 0:
                    x = 0
                    y = 0
                    # Esse será o espaçamento x e y entre cada movimento:
                    espacamento_x = janela.tamanho[0] / 2 - janela.tamanho[0] / 5
                    espacamento_y = 13 * escala
                    # Percorre cada movimento:
                    for i in range(len(pokemons[0].movimentos)):
                        # Pega o id dele:
                        id_movimento = pokemons[0].movimentos[i][0]
                        # Pega o nome:
                        nome_movimento = pokemons[0].movimentos[i][1]
                        # Vê se ele está na lista dos movimentos bloqueados:
                        id_bloqueados = obter_id_bloqueados(pokemons[0])
                        # Se ele não estiver na lista de movimentos bloqueados:
                        if id_movimento not in id_bloqueados:
                            # Desenha o nome do movimento com a cor preta:
                            superficie = arq.fonte_escolher_move.render(str(nome_movimento), False, cor.PRETO)
                        # Caso esteja:
                        else:
                            # Desenha com a cor vermelha:
                            superficie = arq.fonte_escolher_move.render(str(nome_movimento), False, cor.VERMELHO)

                        # Pega o tamanho do nome do movimento:
                        superficie_rect = superficie.get_rect()
                        # Posiciona na posição certa:
                        superficie_rect.topleft = (
                            15 * escala + (espacamento_x * x), janela.tamanho[1] - (36 * escala) + (espacamento_y * y))
                        # Mostra ele na tela
                        janela.tela.blit(superficie, superficie_rect)
                        # Agora o próximo item vai começar na próxima posição x:
                        x += 1
                        # Mas se a próxima posição x for maior que 2:
                        if x >= 2:
                            # Vai resetar para 0:
                            x = 0
                            # Pois agora o próximo nome do item será mostrado em baixo:
                            y += 1
                    # Posição x e y da seta:
                    ly = (espacamento_y * pos.y)
                    lx = (espacamento_x * pos.x)

                    # Posição inicial da seta:
                    pos_inicial = (7 * escala, janela.tamanho[1] - 35 * escala)
                    # Tamanho da seta:
                    tam = 7.2 * escala
                    # Desenhando a seta:              
                    pygame.draw.polygon(janela.tela, cor.PRETO, ((pos_inicial[0] + lx,
                                                                  pos_inicial[1] + ly),
                                                                 (pos_inicial[0] + lx, pos_inicial[1] +
                                                                  tam + ly), (pos_inicial[0] + tam / 2 + lx,
                                                                              pos_inicial[1] + tam / 2 + ly)))

                    # Mostrando o PP atual do movimento selecionado:
                    # Renderizando a fonte:
                    txt_pp = arq.fonte_txt.render(str(pokemons[0].movimentos[pos.i][2]), False, cor.PRETO)
                    # Obtendo o tamanho dela:
                    txt_pp_rect = txt_pp.get_rect()
                    # Posicionando na posição correta da tela:
                    txt_pp_rect.bottomright = (janela.tamanho[0] - 27.5 * escala, janela.tamanho[1] - 27.5 * escala)
                    # Mostrando o texto:
                    janela.tela.blit(txt_pp, txt_pp_rect)

                    # Mostrando o PP máximo:
                    # Fonte:
                    txt_pp_maximo = arq.fonte_txt.render(str(pokemons[0].movimentos[pos.i][3]), False, cor.PRETO)
                    # Tamanho:
                    txt_pp_maximo_rect = txt_pp_maximo.get_rect()
                    # Posição
                    txt_pp_maximo_rect.bottomleft = (janela.tamanho[0] - 19 * escala, janela.tamanho[1] - 27.5 * escala)
                    # Mostrando:
                    janela.tela.blit(txt_pp_maximo, txt_pp_maximo_rect)

                    # Mostrando o tipo do movimento:
                    # Fonte:
                    txt_move = arq.fonte_escolher_move.render(str(pokemons[0].movimentos[pos.i][7]), False, cor.PRETO)
                    # Tamanho:
                    txt_move_rect = txt_move.get_rect()
                    # Posição:
                    txt_move_rect.bottomleft = (janela.tamanho[0] - 47.5 * escala, janela.tamanho[1] - 10 * escala)
                    # Mostrando:
                    janela.tela.blit(txt_move, txt_move_rect)
                # Desenhando as barras onde ficam a vida, nome do pokémon, etc.:
                # Só iremos mostrar se o pokémon ainda está no jogo:
                if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                    # Desenhando a barra:
                    janela.tela.blit(arq.img_barra1, (15 * escala - pokemons[1].circulo_offset * janela.tamanho[0], 18 *
                                                      escala))
                # Verificamos se ele está no jogo novamente:
                if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                    # Desenhando:
                    janela.tela.blit(arq.img_barra2,
                                     (janela.tamanho[0] - 110 * escala + pokemons[0].circulo_offset * janela.tamanho[0],
                                      janela.tamanho[1] - 88 * escala +
                                      pokemons[1].pos_offset * -1 * escala))
                # Nomes dos pokémons renderizados na barra:
                # Pokémon inimigo:
                # Só mostraremos se ele ainda está no jogo
                if not pokemons[1].conseguiu_fugir() and not pokemons[1].foi_derrotado():
                    # Fonte:
                    poke_2 = arq.fonte.render(pokemons[1].nome, False, cor.PRETO)
                    # Tamanho:
                    poke_2_rect = poke_2.get_rect()
                    # Posição:
                    poke_2_rect.center = (48.5 * escala - pokemons[1].circulo_offset * janela.tamanho[0], 25 * escala)
                    # Mostrando:
                    janela.tela.blit(poke_2, poke_2_rect)

                    # Texto do símbolo (se não tiver ficará vazio)
                    texto = ""
                    # Cor dele (se não tiver é preto):
                    a_cor = cor.PRETO
                    # Se o gênero for masculino:
                    if pokemons[1].genero == "F":
                        # Texto será o símbolo de feminino e a cor rosa:
                        texto, a_cor = "♀", cor.ROSA
                    # Se for masculino:
                    elif pokemons[1].genero == "M":
                        # Texto será o símbolo de masculino e a cor azul:
                        texto, a_cor = "♂", cor.AZUL
                    # Fonte do símbolo:
                    simbolo_2 = arq.fonte.render(texto, False, a_cor)
                    # Tamanho:
                    simbolo_2_rect = simbolo_2.get_rect()
                    # Posição:
                    simbolo_2_rect.left = poke_2_rect.width + poke_2_rect.x
                    simbolo_2_rect.top = poke_2_rect.y
                    # Mostrando na tela:
                    janela.tela.blit(simbolo_2, simbolo_2_rect)

                    # Barras de vida:

                    # Barra de vida amarela só se estiver entre 1/5 e 1/2 de sua vida máxima:
                    if pokemons[1].vida_maxima / 5 < pokemons[1].vida_anim <= pokemons[1].vida_maxima / 2:
                        # A imagem:
                        img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela,
                                                                           (int(arq.img_vida_amarela.get_width() + (
                                                                                   escala * 39)),
                                                                            arq.img_vida_vermelha.get_height()))
                        # Mostrando:
                        janela.tela.blit(img_vida_amarela_esticada,
                                         (55 * escala - pokemons[1].circulo_offset * janela.tamanho[0], 34 * escala))
                    # Vida vermelha só se for menor que 1/5 de sua vida máxima:
                    if pokemons[1].vida_anim <= pokemons[1].vida_maxima / 5:
                        # Imagem:
                        img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha,
                                                                            (int(arq.img_vida_vermelha.get_width() + (
                                                                                    escala * 39)),
                                                                             arq.img_vida_vermelha.get_height()))
                        # Mostrando:
                        janela.tela.blit(img_vida_vermelha_esticada,
                                         (55 * escala - pokemons[1].circulo_offset * janela.tamanho[0], 34 * escala))
                    # "Vida vazia":
                    # Pegaremos a posição da barra x e a largura (de acordo com a vida) através da função
                    # "barra_sem_vida_calculo_escala":
                    x, width = barra_sem_vida_calculo_escala(55 * escala +
                                                             barra_width * (pokemons[1].vida_anim /
                                                                            pokemons[1].vida_maxima),
                                                             (arq.img_barra_sem_vida.get_width() + (escala * 39)) *
                                                             (pokemons[1].vida_maxima - pokemons[1].vida_anim) /
                                                             pokemons[1].vida_maxima, 1)
                    # Desenharemos na tela a imagem de barra da parte sem vida:
                    img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida,
                                                                         (width,
                                                                          arq.img_barra_sem_vida.get_height()))
                    # Mostrando a barra na tela:
                    janela.tela.blit(img_barra_sem_vida_esticada,
                                     (x - pokemons[1].circulo_offset * janela.tamanho[0], 34 * escala))

                    # Mostrando o nível do pokémon:
                    # Fonte:
                    nivel = arq.fonte_escolher_move.render(str(pokemons[1].nivel), False, cor.PRETO)
                    # Tamanho:
                    nivel_rect = nivel.get_rect()
                    # Posição:
                    nivel_rect.topleft = (96 * escala - pokemons[1].circulo_offset * janela.tamanho[0], 23 * escala)
                    # Mostrando:
                    janela.tela.blit(nivel, nivel_rect)

                # Seu pokémon:
                # Novamente só mostrando se ele ainda está no jogo:
                if not pokemons[0].conseguiu_fugir() and not pokemons[0].foi_derrotado():
                    # Fonte:
                    poke_1 = arq.fonte.render(pokemons[0].nome, False, cor.PRETO)
                    # Tamanho:
                    poke_1_rect = poke_1.get_rect()
                    # Posição:
                    poke_1_rect.center = (
                        (janela.tamanho[0] - 68 * escala + pokemons[1].circulo_offset * janela.tamanho[0]),
                        janela.tamanho[1] - 77.5 * escala +
                        pokemons[1].pos_offset * -1 * escala)
                    # Mostrando:
                    janela.tela.blit(poke_1, poke_1_rect)

                    # Texto que mostrará o gênero do pokémon (se não tiver é vazio):
                    texto = ""
                    # Cor do gênero (se não tiver é preto)
                    a_cor = cor.PRETO

                    # Se o gênero for feminino:
                    if pokemons[0].genero == "F":
                        # Texto será o símbolo de feminino e a cor rosa:
                        texto, a_cor = "♀", cor.ROSA
                    # Se for masculino:
                    elif pokemons[0].genero == "M":
                        # Texto será o símbolo de masculino e a cor azul:
                        texto, a_cor = "♂", cor.AZUL
                    # Fonte do símbolo do gênero do seu pokémon
                    simbolo_1 = arq.fonte.render(texto, False, a_cor)
                    # Obtendo o tamanho do símbolo:
                    simbolo_1_rect = simbolo_1.get_rect()
                    # Colocando na posição certa (ao lado do nome dele):
                    simbolo_1_rect.left = poke_1_rect.width + poke_1_rect.x
                    simbolo_1_rect.top = poke_1_rect.y
                    # Mostrando na tela o símbolo:
                    janela.tela.blit(simbolo_1, simbolo_1_rect)

                    # Barra de vida amarela:
                    if pokemons[0].vida_anim <= pokemons[0].vida_maxima / 2:
                        img_vida_amarela_esticada = pygame.transform.scale(arq.img_vida_amarela,
                                                                           (int(arq.img_vida_amarela.get_width() + (
                                                                                   escala * 39)),
                                                                            arq.img_vida_vermelha.get_height()))
                        # Mostrando:
                        janela.tela.blit(img_vida_amarela_esticada, (janela.tamanho[0] - 62 * escala +
                                                                     pokemons[1].circulo_offset * janela.tamanho[0],
                                                                     janela.tamanho[1] - 69 * escala +
                                                                     pokemons[1].pos_offset * -1 * escala))
                    # Vida vermelha:
                    if pokemons[0].vida_anim <= pokemons[0].vida_maxima / 5:
                        img_vida_vermelha_esticada = pygame.transform.scale(arq.img_vida_vermelha,
                                                                            (int(arq.img_vida_vermelha.get_width() + (
                                                                                    escala * 39)),
                                                                             arq.img_vida_vermelha.get_height()))
                        # Mostrando:
                        janela.tela.blit(img_vida_vermelha_esticada, (janela.tamanho[0] -
                                                                      62 * escala + pokemons[1].circulo_offset *
                                                                      janela.tamanho[0],
                                                                      janela.tamanho[1] - 69 * escala +
                                                                      pokemons[1].pos_offset * -1 * escala))
                    # "Vida vazia":
                    x, width = barra_sem_vida_calculo_escala(janela.tamanho[0] - 62 * escala +
                                                             barra_width * (pokemons[0].vida_anim /
                                                                            pokemons[0].vida_maxima),
                                                             (arq.img_barra_sem_vida.get_width() + (escala * 39)) *
                                                             (pokemons[0].vida_maxima - pokemons[0].vida_anim) /
                                                             pokemons[0].vida_maxima, 0)
                    # Desenharemos na tela a imagem de barra da parte sem vida:
                    img_barra_sem_vida_esticada = pygame.transform.scale(arq.img_barra_sem_vida,
                                                                         (width,
                                                                          arq.img_barra_sem_vida.get_height()))
                    # Mostrando a "vida vazia":
                    janela.tela.blit(img_barra_sem_vida_esticada, (
                        x + pokemons[1].circulo_offset * janela.tamanho[0], janela.tamanho[1] - 69 * escala +
                        pokemons[1].pos_offset * -1 * escala))
                    # Mostrando o nível do pokémon:
                    nivel = arq.fonte_escolher_move.render(str(pokemons[0].nivel), False, cor.PRETO)
                    nivel_rect = nivel.get_rect()
                    nivel_rect.left = janela.tamanho[0] - 21 * escala + pokemons[1].circulo_offset * janela.tamanho[0]
                    nivel_rect.top = janela.tamanho[1] - 80 * escala + pokemons[1].pos_offset * -1 * escala
                    janela.tela.blit(nivel, nivel_rect)

                    # Mostrando o número da vida:
                    txt_vida = arq.fonte.render(str(pokemons[0].vida) + "/" + str(pokemons[0].vida_maxima), False,
                                                cor.PRETO)
                    txt_vida_rect = txt_vida.get_rect()
                    txt_vida_rect.bottomright = (
                        janela.tamanho[0] - 20 * escala + pokemons[1].circulo_offset * janela.tamanho[0],
                        janela.tamanho[1] - 55 * escala + pokemons[1].pos_offset * -1 * escala)

                    janela.tela.blit(txt_vida, txt_vida_rect)

                # Se não está no sub menu de escolha de ataque, então mostrar o texto que fala o que
                # está acontecendo:
                if not sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                    texto_multilinha(mensagem.texto)
        # Atualiza o display:
        pygame.display.update()

    # Função que escolhe um pokémon:
    def escolher_pokemon(menu_funcao, sub_menu_funcao, mensagem_funcao):
        # Muda o menu para o de batalha:
        menu_funcao.atual = menu_funcao.batalhando
        # Muda também o sub menu para ser o principal:
        sub_menu_funcao.atual = sub_menu_funcao.principal
        # Obtém através da posição do cursor o pokémon que foi escolhido pelo usuário:
        pokemons[0] = pokemons_pode_escolher[pos.i].copy()
        # Pokémon inimigo aleatório:
        pokemons[1] = pokemons_pode_escolher[random.randrange(0, len(pokemons_pode_escolher))].copy()

        # Mostra a mensagem do que seu pokémon deve fazer:
        mensagem_funcao.texto = "O que {} deve fazer?".format(pokemons[0].nome)
        # Reseta o cursor:
        pos_2x2()

    # Função que reseta o cursor para uma "grade" 2x2:
    def pos_2x2():
        # Reseta a posição do cursor:
        pos.i = 0
        # 2 de largura:
        pos.width = 2
        # 2 de altura:
        pos.height = 2
        # Ou seja, o espaço em que o cursor pode se mover.

    # Reseta o cursor para uma grande 1 x (tamanho da lista de pokémons que pode escolher):
    def pos_menu_principal():
        # Reseta a posição:
        pos.i = 0
        # 1 de largura:
        pos.width = 1
        # (tamanho da lista dos pokémons que podem ser escolhidos) de altura:
        pos.height = len(pokemons_pode_escolher)

    # Checa se possui pelo menos 1 pp em algum movimento dele:
    def possui_algum_pp(pokemon):
        possui = False
        # Percorre a lista de movimentos:
        for i in range(len(pokemon.movimentos)):
            if pokemon.movimentos[i][2] > 0:  # se pp do movimento for maior que 0:
                # Então possui:
                possui = True
                # E não precisa mais procurar:
                break
        # Retorna se possui:
        return possui

    # Escolha da ação que o pokemon irá fazer:
    def escolher_acao_batalha(pos_funcao):
        # Se for o de lutar (primeira posição do cursor):
        if pos_funcao.i == 0:
            # Reseta o cursor:
            pos_2x2()

            if possui_algum_pp(pokemons[0]):
                # Muda a tela para a que mostra os movimentos disponíveis:
                sub_menu.atual = sub_menu.escolhendo_ataque
            else:
                # Faz o movimento padrão:
                fazer_acao(sub_menu, moves.struggle, category.normal_move)
        # Se for o que abre os itens (mochila, segunda posição):
        elif pos_funcao.i == 1:
            # Muda para a tela de mochila
            sub_menu.atual = sub_menu.itens
            # Reseta a posição do cursor:
            pos_funcao.i = 0
            # Coloca para que o cursor só possa percorrer uma grade 1 x (quantidade de itens + 1)
            pos_funcao.width = 1
            # Somaremos mais um pois tem o botão de cancelar:
            pos_funcao.height = len(pokemons[0].itens) + 1
        # E se for o botão de fugir:
        elif pos_funcao.i == 3:
            # Executa a função que faz o pokémon tentar fugir:
            fazer_acao(sub_menu, moves.fugir, category.normal_move)

    # Remover turnos que ficaram pendentes quando a partida acaba:
    def remover_todos_turnos():
        # Percorre a lista de turnos:
        for i in range(len(turnos)):
            # Removendo sempre o primeiro, pois a lista é "reorganizada" ao remover
            # um item dela, ou seja, não sobra "espaços vazios".
            turnos.pop(0)
        # E reseta as etapas:
        tempo.etapa_turno_reseta()

    # Cria a lista de turnos que começa em branco:
    turnos = []

    # Função que processa as ações que acontecem:
    def fazer_acao(sub_menu_funcao, movimento, categoria):
        # Para a animação:
        pokemons[0].pos_offset_parar()

        def aleatorio(pokemons_funcao):
            # Aleatório pela velocidade
            # Primeiro a gente pega um número aleatório
            vez_funcao = random.randrange(0, 1)
            # Agora, se o pokémon "0" (seu pokémon) tiver maior velocidade que o
            # pokémon "1" (pokémon inimigo), então o seu pokémon será o primeiro:
            if pokemons_funcao[0].velocidade > pokemons_funcao[1].velocidade:
                # Colocamos como primeiro o pokémon "0":
                vez_funcao = 0
            # Mas se seu pokémon tiver menor velocidade que o pokémon inimigo:
            elif pokemons_funcao[0].velocidade < pokemons_funcao[1].velocidade:
                # O primeiro será o pokémon "1":
                vez_funcao = 1
            return vez_funcao
            # Agora, se os dois tiverem a mesma velocidade, então nem o if e o elif serão
            # executados, aí o primeiro será aleatório, pois antes do if colocamos um random
            # de aleatório.
            # vez = random.randrange(0,1)

        # [pokémon "0", pokémon "1"]:
        # A gente pega a categoria que o usuário escolheu, a outra é a categoria do "computador":
        movimento_ia, categoria_ia, = randomizar_acao(pokemons[1])

        # Aqui primeiro vemos qual pokémon vai fazer suas ações primeiro:
        # Pela prioridade de item:
        if category.item_move == categoria_ia and not categoria == category.item_move:
            # Primeiro o computador:
            vez = 1
        elif category.item_move == categoria and not categoria_ia == category.item_move:
            # Primeiro seu pokémon:
            vez = 0
        else:
            # Prioridade do movimento:
            if not categoria == categoria_ia:
                # [4]: prioridade
                if movimento[4] > movimento_ia[4]:
                    vez = 0
                elif movimento_ia[4] > movimento[4]:
                    vez = 1
                else:
                    vez = aleatorio(pokemons)
            else:
                vez = aleatorio(pokemons)

        categorias_pokemons = [categoria, categoria_ia]
        # E o movimento do usuário, e a ação aleatória do pokémon inimigo:
        movimentos_pokemons = [movimento, movimento_ia]

        # O primeiro pokémon vai executar os movimentos de estado que acontecem
        # antes dos movimentos dele em si:
        turnos.append([pokemons[vez], pokemons[vez - 1], True, category.state_move])
        # Agora será adicionado aos turnos o movimento em si:
        turnos.append([pokemons[vez], pokemons[vez - 1], movimentos_pokemons[vez], categorias_pokemons[vez]])
        # E agora os movimentos de estado que acontecem depois do movimento do pokémon em si:
        turnos.append([pokemons[vez], pokemons[vez - 1], False, category.state_move])

        # Agora a mesma coisa, só que agora com o segundo pokémon:
        # A ação que acontece antes do movimento em si:
        turnos.append([pokemons[vez - 1], pokemons[vez], True, category.state_move])
        # O movimento em si:
        turnos.append([pokemons[vez - 1], pokemons[vez], movimentos_pokemons[vez - 1], categorias_pokemons[vez - 1]])
        # E a ação de estado depois do movimento:
        turnos.append([pokemons[vez - 1], pokemons[vez], False, category.state_move])

        # Coloca a seta poder se locomover somente a partir de um espaço
        # 2 de largura e 2 de altura (2 x 2)
        pos_2x2()
        # Coloca o sub menu atual sendo o principal:
        sub_menu_funcao.atual = sub_menu_funcao.principal

    def randomizar_acao(pokemon):

        # Primeiro tenta recuperar sua vida se necessário e possível:
        if pokemon.vida < pokemon.vida_maxima / 3:
            if itens.potion in pokemon.itens:
                # Tem a poção, então use:
                pokemon.itens.remove(itens.potion)
                return itens.potion, category.item_move
            elif itens.berry_juice in pokemon.itens:
                # Use também:
                pokemon.itens.remove(itens.berry_juice)
                return itens.berry_juice, category.item_move
            else:
                # Tenta fugir então se não tem:
                return moves.fugir, category.normal_move
        else:
            # Verificar se tem algum movimento que pode ser utilizado:
            movimentos = somente_movimentos_disponiveis(pokemon)
            if len(movimentos) > 0:
                # Aqui a gente faz com que o pokémon inimigo faça um movimento aleatório:
                a_random = pokemon.movimentos[random.choice(movimentos)]
                if a_random == moves.curse and pokemon.vida < pokemon.vida_maxima / 2:
                    if len(movimentos) > 1:
                        # Pega outro movimento:
                        a_random -= movimentos[a_random - 1]
            else:
                # Movimento padrão:
                a_random = moves.struggle
            # E retornamos qual o movimento foi escolhido:
            return a_random, category.normal_move

    # Criamos o objeto tempo, ele começará com 1000 milisegundos, pois se colocarmos 0,
    # se o usuário for rápido o suficiente de entrar na partida e já fazer o movimento, ele
    # verá que o mesmo não será executado imediatamente de acordo com a quantidade de milisegundos
    # que faltariam para chegar 1000:
    tempo = Tempo(1000)

    # Parte lógica do jogo:
    def processar_logica(delta_funcao, tempo_funcao, menu_funcao, sub_menu_funcao):
        # Se o menu atual for o de batalha:
        if menu_funcao.atual == menu_funcao.batalhando:
            # Faz a animação texto passando quantos milisegundos passaram (delta):
            tempo_funcao.mensagem_tempo += delta_funcao

            # Aqui serão executados as funções que atualizam o tamanho da animação da
            # barra de vida dos dois pokémons:
            pokemons[0].atualiza_vida_anim(delta_funcao)
            pokemons[1].atualiza_vida_anim(delta_funcao)

            pokemons[0].processar_circulo_anim(delta_funcao)
            pokemons[1].processar_circulo_anim(delta_funcao)

            # Aqui é a animação do texto:
            # Se passou mais de 25 milisegundos:
            if tempo_funcao.mensagem_tempo > 25:
                # A gente subtrai 25 milisegundos para resetar esse tempo:
                tempo_funcao.mensagem_tempo -= 25
                # E se a última posição do texto (quantidade de caracteres exibidos) for menor do que
                # o tamanho do texto que aparecerá na tela:
                if mensagem.texto_posicao < len(mensagem.texto):
                    # Então a gente executa a função que vai colocar + 1 de quantidade de caracteres
                    # que vão aparecer na tela:
                    mensagem.texto_deslocar_uma_posicao()
            # Aqui a gente adiciona ao tempo os milisegundos que passaram:
            tempo_funcao.adicionar(delta_funcao)
            # Essa é a animação do pokémon "sumindo" ao tomar algum "golpe":
            # Verificaremos se passou 75 milisegundos:
            if tempo_funcao.sumido_tempo >= 75:
                # Se sim, então a gente verifica se a animação está ativada:
                if pokemons[1].sumindo:
                    # E executa a função que inverte o estado de estar "invisível" ou "visível": 
                    pokemons[1].inverte_sumido()
                elif pokemons[0].sumindo:
                    # A mesma coisa para esse pokémon:
                    pokemons[0].inverte_sumido()
                # E resetaremos o tempo diminuindo 75 milisegundos correspondentes:
                tempo_funcao.sumido_tempo -= 75
            # Adiciona a quantidade de milisegundos passados ao tempo que está "sumido" ou "visível":
            tempo_funcao.sumido_tempo += delta_funcao

            # Animação do pokémon quando ele foi derrotado:
            if pokemons[1].foi_derrotado():
                # Deslocamento: [0] = x, [1] = y
                # Desloca a posição y do sprite de acordo com o delta: 
                pokemons[1].deslocamento[1] += 0.4 * delta_funcao
            # Animação quando ele consegue fugir:
            if pokemons[1].conseguiu_fugir():
                # Só que agora com a posição x:
                pokemons[1].deslocamento[0] += 0.4 * delta_funcao

            # E as mesmas coisas com o outro pokémon:
            if pokemons[0].foi_derrotado():
                # deslocamento: [0] = x, [1] = y
                pokemons[0].deslocamento[1] += 0.4 * delta_funcao
            if pokemons[0].conseguiu_fugir():
                pokemons[0].deslocamento[0] -= 0.4 * delta_funcao

            if sub_menu.no_submenu(sub_menu.principal) or sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                # Animação de deslocamento no pokémon e barra:
                pokemons[0].processar_pos_offset(delta_funcao)
                pokemons[1].processar_pos_offset(delta_funcao)

            # Processa o tempo:
            # Colocamos 1 segundo para cada etapa dos movimentos (ver a função process_turns
            # para mais informações):
            if tempo_funcao.milisegundos >= 1000:  # 1000 milisegundos = 1 segundo
                # Se não estiver no sub menu de derrota ou vitória:
                if not sub_menu_funcao.no_submenu(sub_menu_funcao.derrota) and not sub_menu_funcao.no_submenu(
                        sub_menu_funcao.vitoria):
                    # Verificamos se o seu pokémon foi derrotado ou fugiu:
                    if pokemons[0].foi_derrotado() or pokemons[0].conseguiu_fugir():
                        # Mostra na tela o pokémon que ganhou:
                        mensagem.texto = "{} ganhou a batalha".format(pokemons[1].nome)
                        # Executa a função que remove os turnos que ficaram pendentes, pois não
                        # precisamos processá-los, já que a partida terminou:
                        remover_todos_turnos()
                        # Colocamos o sub menu de derrota:
                        sub_menu_funcao.atual = sub_menu_funcao.derrota
                        # Tocamos a música de derrota, já que foi o adversário seu que ganhou:
                        tocar_musica("Dados/Recursos/Sprites/SonsPokemon/derrota.wav", False)
                    # A mesma coisa com o pokémon inimigo:
                    elif pokemons[1].foi_derrotado() or pokemons[1].conseguiu_fugir():
                        mensagem.texto = "{} ganhou a batalha".format(pokemons[0].nome)
                        remover_todos_turnos()
                        # Só que agora é o de vitória, já que foi o seu pokémon inimigo que perdeu:
                        sub_menu_funcao.atual = sub_menu_funcao.vitoria
                        tocar_musica("Dados/Recursos/Sprites/SonsPokemon/vitoria.wav", False)
                    else:
                        # Caso contrário, ou seja, a partida não acabou:
                        # Verificaremos se tem algum turno que está pendente, se sim processaremos ele:
                        if len(turnos) > 0:
                            # Resetamos o cursor (ver a função pos_2x2 para mais detalhes):
                            pos_2x2()
                            # Trocaremos o sub menu atual para o que mostra as ações que estão sendo feitas:
                            sub_menu_funcao.atual = sub_menu_funcao.fazendo_acoes
                            # E executamos a função que processa os turnos:
                            process_turns(turnos, mensagem, tempo_funcao)
                        else:
                            # Caso não temos turnos para serem processados agora:
                            # Se estiver no sub menu de fazendo ações, ou seja, o sub menu que mostra que ações estão
                            # sendo feitas:
                            if sub_menu_funcao.atual == sub_menu_funcao.fazendo_acoes:
                                # Se o seu pokémon está bloqueado, então ele deve fazer simplesmente nada:
                                if pokemons[0].bloqueado:
                                    # Fazer nada se seu pokémon estiver bloqueado:
                                    fazer_acao(sub_menu_funcao, None, category.normal_move)
                                    # E mudaremos o sub menu para o que mostra quais ações estão sendo executadas:
                                    sub_menu_funcao.atual = sub_menu_funcao.fazendo_acoes
                                else:
                                    # Caso não esteja bloqueado, então podemos deixar o usuário escolher o que fazer:
                                    # Mostramos a pergunta de o que seu pokémon deve fazer:
                                    mensagem.texto = "O que {} deve fazer?".format(pokemons[0].nome)
                                    # Mudamos o sub menu atual para o principal:
                                    sub_menu_funcao.atual = sub_menu_funcao.principal
                                    # E resetamos o cursor:
                                    pos_2x2()
                else:
                    # Caso o jogo terminou:
                    # Contaremos o tempo que ficará na tela de fim de jogo
                    tempo_funcao.fim_de_jogo_tempo += delta_funcao
                    # Foi colocado 5 segundos:
                    if tempo_funcao.fim_de_jogo_tempo >= 5000:
                        # Quando passar de 5 segundos, volta para a tela de seleção dos pokémons:
                        menu_funcao.atual = menu_funcao.escolhendo_pokemon
                        # Diz também que está no sub menu principal:
                        sub_menu_funcao.atual = sub_menu_funcao.principal
                        # Toca a música de novo de abertura:
                        tocar_musica("Dados/Recursos/Sprites/SonsPokemon/fireRedAbertura.wav", True)
                        # Reseta esse tempo se ocorrer um próximo jogo:
                        tempo_funcao.fim_de_jogo_tempo = 0
                        # E reseta o cursor (ver a função para mais detalhes):
                        pos_menu_principal()

    # A função que processa a vez de cada pokémon:
    def process_turns(turnos_funcao, mensagem_funcao, tempo_funcao):

        # Essa função serve para remover um turno quando ele acabar:
        def remover_turno(ir_logo_pro_proximo=False):
            # Para evitar erros, verificamos se tem pelo menos 1 coisa na lista:
            if len(turnos_funcao) > 0:
                # Se sim, removemos o primeiro turno:
                turnos_funcao.pop(0)
            # Essa função reseta o contador de etapas dos movimentos:
            tempo_funcao.etapa_turno_reseta()
            # Se quer ir logo pro próximo turno sem atraso:
            if ir_logo_pro_proximo:
                # No final os turnos vão estar vazios, aí vai dar erro se tentar acessar algum
                # item da lista de turnos, então só vamos ir pro próximo turno se ainda estiver
                # turnos pendentes:
                if len(turnos_funcao) > 0:
                    process_turns(turnos_funcao, mensagem_funcao, tempo_funcao)

        pokemon_a_fazer = turnos_funcao[0][0]  # Pokémon que vai usar a ação
        pokemon_a_tomar = turnos_funcao[0][1]  # Pokémon que vai sofrer da ação
        move = turnos_funcao[0][2]  # Qual movimento vai ser realizado (id, nome do movimento);
        # Quando for movimento de estado, será True ou false.
        turn_category = turnos_funcao[0][3]  # Pega qual categoria é (movimento normal ou de estado)

        # Só faz o movimento se ele não for None:
        if move is not None:
            # Se o movimento for um movimento de estado, como por exemplo um movimento que
            # acontece depois de um certo tempo:
            if turn_category["id"] == category.state_move["id"]:
                # Aqui temos as etapas que cada movimento tem:
                # Primeira etapa começa no 0:
                if tempo_funcao.etapa_turno == 0:
                    # Nesse caso, será obtido a mensagem do que o efeito fez com o pokémon:
                    mensagens = pokemon_a_fazer.process_effects(move, pokemon_a_tomar)
                    # Se tiver mensagens significa que aconteceu algum efeito:
                    if len(mensagens) > 0:
                        # Mostraremos a mensagem na tela:
                        mensagem_funcao.texto = mensagens[0]
                        # E a gente implementa +1 no tempo.etapa_turno:
                        tempo_funcao.etapa_turno_incrementa()
                    else:
                        # Se não, então não teve, então já podemos remover e ir logo pro próximo turno:
                        remover_turno(True)
                # Agora temos a segunda etapa, observando que a gente vai voltar aqui depois de um certo tempo,
                # executando assim a função que remove o turno, ou seja, termina ele:
                elif tempo_funcao.etapa_turno == 1:
                    remover_turno()
            # Agora, se for um movimento "normal", ou seja, movimento de ataque, entre outros.
            # Só pode se não estiver bloqueado o pokémon:
            elif turn_category["id"] == category.normal_move["id"] and not pokemon_a_fazer.bloqueado:
                # Primeira etapa:
                if tempo_funcao.etapa_turno == 0:
                    # Se o pokémon tentou fugir
                    if move[0] == moves.fugir[0]:
                        # Mostra que ele tentou fugir mostrando o nome dele:
                        mensagem_funcao.texto = "{} tentou fugir".format(pokemon_a_fazer.nome)
                    else:
                        # Caso contrário, é um outro movimento, mostrando o nome e o movimento que usou:
                        mensagem_funcao.texto = "{} usou {}".format(pokemon_a_fazer.nome, str(move[1]))
                    # Incrementa a etapa:
                    tempo_funcao.etapa_turno_incrementa()
                # Segunda etapa:
                elif tempo_funcao.etapa_turno == 1:
                    # Animação básica, assim vai fazer o pokémon ficar "sumindo" e "voltando":
                    if not move[0] == moves.fugir[0]:
                        pokemon_a_tomar.sumindo = True
                    else:
                        fugiu = pokemon_a_fazer.fugir_de(pokemon_a_tomar)
                        if fugiu:
                            # Conseguiu fugir:
                            mensagem.texto = "conseguiu fugir com sucesso"
                        else:
                            # Não conseguiu
                            mensagem.texto = "mas não conseguiu"
                    # Próxima etapa:
                    tempo_funcao.etapa_turno_incrementa()
                # Terceira etapa:
                elif tempo_funcao.etapa_turno == 2:
                    # Percorre toda a lista de movimentos do pokémon que vai fazer o movimento
                    # até achar o movimento certo e obter seu pp:
                    move_pokemon = None
                    for i in range(len(pokemon_a_fazer.movimentos)):
                        # Se o movimento foi encontrado na lista de movimentos do pokémon:
                        if pokemon_a_fazer.movimentos[i][0] == move[0]:
                            # Pegaremos o mesmo:
                            move_pokemon = pokemon_a_fazer.movimentos[i]
                            # E podemos terminar de procurar os movimentos encerrando o "for":
                            break
                    # Atualiza qual foi o ultimo movimento usado desse pokémon:
                    # move[0]: id
                    pokemon_a_fazer.ultimo_movimento_id = move[0]
                    # Desativa a animação básica
                    pokemon_a_tomar.sumindo = False
                    # Processa o movimento atual:
                    # Verificamos se possui pp suficiente para executar o movimento:
                    # Mas o movimento struggle será não gastará pp, já que é usado somente quando
                    # não tem pp's em todos os movimentos:
                    if move[0] == moves.fugir[0]:
                        # Fazer nada:
                        pass
                    elif move[0] == moves.struggle[0]:
                        process_moves(pokemon_a_fazer, pokemon_a_tomar, move[0], mensagem_funcao, moves, tipos, effect)
                    elif not move_pokemon[2] <= 0:  # move_pokemon[2]: pp atual
                        movimentos_bloqueados_ids = []
                        # Pega somente os ids dos movimentos bloqueados:
                        for i in range(len(pokemon_a_fazer.movimentos_bloqueados)):
                            movimentos_bloqueados_ids.append(pokemon_a_fazer.movimentos_bloqueados[0])
                        # Agora verificar se não foi bloqueado:
                        if not obter_id_bloqueados(pokemon_a_fazer) in movimentos_bloqueados_ids:
                            # Gastaremos o seu pp:
                            move_pokemon[2] -= 1
                            # E processaremos o movimento em si, essa função está no arquivo "processar_movimentos.py":
                            process_moves(pokemon_a_fazer, pokemon_a_tomar, move[0], mensagem_funcao, moves, tipos,
                                          effect)
                        else:
                            # Teve seu movimento bloqueado:
                            mensagem_funcao.texto = "mas foi bloqueado"
                    else:
                        # Caso contrário, mostra a mensagem que não tem pp suficiente:
                        mensagem_funcao.texto = "mas não teve mais pp suficiente"
                    # Próximo:
                    tempo_funcao.etapa_turno_incrementa()
                # a última etapa é tirar o movimento que acabou de ser feito da lista
                # de movimentos:
                elif tempo_funcao.etapa_turno == 3:
                    remover_turno()
            # Por último, se o movimento foi do tipo "item", ou seja, ele usou um item.
            # Só pode se não estiver bloqueado também:
            elif turn_category["id"] == category.item_move["id"] and not pokemon_a_fazer.bloqueado:
                # Primeira etapa:
                if tempo_funcao.etapa_turno == 0:
                    # Mostramos o nome do pokémon e o item que ele usou:
                    mensagem_funcao.texto = "{} usou o item {}".format(pokemon_a_fazer.nome, str(move[1]))
                    # Incrementamos a etapa:
                    tempo_funcao.etapa_turno_incrementa()
                # Segunda etapa:
                elif tempo_funcao.etapa_turno == 1:
                    # Usaremos o item em si:
                    usar_item(pokemon_a_fazer, move[0])
                    tempo_funcao.etapa_turno_incrementa()
                # Última etapa:
                else:
                    # Removeremos esse movimento da lista:
                    remover_turno(True)
            else:
                # Remover o movimento da lista (se for inválido):
                remover_turno(True)
        else:
            # Remover o movimento da lista (se for inválido):
            remover_turno(True)
        # Resetamos o tempo que leva para executar essa função de novo:
        tempo_funcao.resetar()

        # Código que executa a função de cada item:

    def usar_item(pokemon_a_usar, item):
        # Se o item for o dire hit:
        if item == itens.dire_hit[0]:  # Aumenta a proporção de acertos críticos de Pokémon em batalha
            # O código do que o item faz em si:
            pokemon_a_usar.ataque_critico += 1
            # Mostra o que aconteceu em forma de texto:
            mensagem.texto = "{} aumentou a proporção de ataque crítico".format(pokemon_a_usar.nome)

        # Se for o guard spec:
        elif item == itens.guard_spec[0]:  # Um item que impede a redução de estatísticas
            pokemon_a_usar.protegido = 3
            mensagem.texto = "{} tem seus dados protegidos por 3 turnos".format(pokemon_a_usar.nome)

        # Se for o x accuracy e etc:
        elif item == itens.x_accuracy[0]:  # Aumenta a estatística de precisão do Pokémon em batalha
            pokemon_a_usar.precisao += 1
            mensagem.texto = "{} aumentou a precisão em 1 estágio".format(pokemon_a_usar.nome)

        # Se for o x attack:
        elif item == itens.x_attack[0]:  # Aumenta a estatística ataque do Pokémon na batalha
            pokemon_a_usar.ataque += 1
            mensagem.texto = "{} aumentou seu ataque em 1 estágio".format(pokemon_a_usar.nome)

        # Se for o x defense:
        elif item == itens.x_defense[0]:  # Aumenta a estatística DEFESA do Pokémon em batalha
            pokemon_a_usar.defesa += 1
            mensagem.texto = "{} aumentou sua defesa em 1 estágio".format(pokemon_a_usar.nome)
        # Se for o x special:
        elif item == itens.x_special[0]:  # Eleva a estatística do ataque especial
            pokemon_a_usar.especial_ataque += 1
            mensagem.texto = "{} aumentou seu ataque especial em 1 estágio".format(pokemon_a_usar.nome)
        # Se for o x speed:
        elif item == itens.x_speed[0]:  # Aumenta a estatística de VELOCIDADE do Pokémon na batalha
            pokemon_a_usar.velocidade += 1
            mensagem.texto = "{} aumentou sua velocidade em 1 estágio".format(pokemon_a_usar.nome)
        # Se for o berry juice:
        elif item == itens.berry_juice[0]:  # Um suco 100% puro. Ele restaura o HP de um Pokémon em 20 pontos.
            pokemon_a_usar.vida += 20
            mensagem.texto = "{} teve seu HP restaurado em 20 pontos".format(pokemon_a_usar.nome)
        # Se for o elixir:
        elif item == itens.elixir[0]:  # Restaura o PP de todos os movimentos de um Pokémon em 10 pontos cada.
            # Percorrer todos os movimentos do pokémon e aumentar seus respectivos pp's:
            for i in range(len(pokemon_a_usar.movimentos)):
                # Pega o pp máximo que pode ter do movimento que está percorrendo:
                pp_max = pokemon_a_usar.movimentos[i][3]

                # Código que aumenta em 10 o pp atual, lembrando que o máximo de pp atual que pode ter é pp_max.
                # movimentos[i][2]: pp atual
                pokemon_a_usar.movimentos[i][2] += 10
                # Verificar se o pp_atual passou do pp_max, se sim, pp_atual = pp_max (para não passar de pp_max)
                if pokemon_a_usar.movimentos[i][2] > pp_max:
                    pokemon_a_usar.movimentos[i][2] = pp_max
            # Mostrar a mensagem que recuperou pp:
            mensagem.texto = "{} recuperou PP".format(pokemon_a_usar.nome)
        # se for o potion:
        elif item == itens.potion[0]:  # Ele restaura o HP de um Pokémon em 20 pontos.
            pokemon_a_usar.vida += 20
            mensagem.texto = "{} ganhou 20 HP".format(pokemon_a_usar.nome)

    # Começa com o easter egg desativado:
    easter_egg_ativado = False

    def ativar_easter_egg():
        # Só ativa se ainda não foi ativado:
        if not easter_egg_ativado:
            # Adiciona os personagens secretos nas listas:
            pokemons_pode_escolher.append(pk_marco)
            pokemons_pode_escolher.append(pk_jorge)
            pokemons_pode_escolher.append(pk_bea)
            pokemons_pode_escolher.append(pk_andre)
            pokemons_pode_escolher.append(pk_thiago)

            # Cores:
            cores_pode_escolher.append(cor.BRANCO)
            cores_pode_escolher.append(cor.BRANCO)
            cores_pode_escolher.append(cor.BRANCO)
            cores_pode_escolher.append(cor.BRANCO)
            cores_pode_escolher.append(cor.BRANCO)

            # Recalcula a posição do cursor:
            pos_menu_principal()

    rodando_o_jogo = True
    # Loop do jogo:
    while rodando_o_jogo:
        # Colocando o jogo para rodar no máximo a 60 quadros por segundo e obtendo o "delta time":
        delta = clock.tick(60)
        # Eventos:
        for event in pygame.event.get():
            # Se o usuário executou a ação de fechar a janela:
            if event.type == pygame.QUIT:
                # Faz o jogo parar de rodar:
                rodando_o_jogo = False
            # Eventos do teclado:
            # Se o evento foi de alguma tecla pressionada:
            if event.type == pygame.KEYDOWN:
                # Se está no menu de batalha:
                if menu.no_menu(menu.batalhando):
                    # Se sim, então verificaremos em qual sub menu está:
                    # Se for no sub menu principal ou no sub menu de escolha do movimento do pokémon:
                    if sub_menu.no_submenu(sub_menu.principal) or sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                        # Aqui será verificado qual tecla foi pressionada.
                        # As teclas são cima, baixo, esquerda e direita do teclado do usuário:
                        if event.key == pygame.K_UP:
                            # Cima:
                            # Toca o som de quando muda a seta de lugar:
                            arq.som_menu_mudou.play()
                            # A posição y da seta subirá para cima:
                            pos.y -= 1
                            # OBS: É checado se a seta passou do limite no setter do y da classe Posicao,
                            # localizado no arquivo "posicao.py".
                        elif event.key == pygame.K_DOWN:
                            # Baixo:
                            # A mesma coisa do código de cima:
                            arq.som_menu_mudou.play()
                            pos.y += 1
                        elif event.key == pygame.K_LEFT:
                            # Esquerda:
                            arq.som_menu_mudou.play()
                            pos.x -= 1
                        elif event.key == pygame.K_RIGHT:
                            # Direita:
                            arq.som_menu_mudou.play()
                            pos.x += 1
                    # Agora, será verificado se está no sub menu principal:
                    if sub_menu.no_submenu(sub_menu.principal):
                        # Se a tecla foi "Esc" (escape), então a gente volta para a tela de seleção
                        # de pokémons:
                        if event.key == pygame.K_ESCAPE:
                            # Toca o som de sempre:
                            arq.som_menu_mudou.play()
                            # Coloca o menu atual sendo o menu de escolha de pokémons: 
                            menu.atual = menu.escolhendo_pokemon
                            # Coloca para tocar a música de abertura:
                            tocar_musica("Dados/Recursos/Sprites/SonsPokemon/fireRedAbertura.wav", True)
                            # Atualiza o cursor (ver os comentários da função para mais informações):
                            pos_menu_principal()
                        # Agora, se a tecla foi "Enter" (return), então vai fazer uma ação de acordo
                        # com o que a seta estava selecionando:
                        if event.key == pygame.K_RETURN:
                            # Toca o efeito sonoro:
                            arq.som_menu_mudou.play()
                            # Executará a função que vai observar qual item foi selecionado (ex: se
                            # foi o botão que olha os itens da mochila, se é o botão de fugir, etc):
                            escolher_acao_batalha(pos)
                    # Se o usuário estiver no sub menu de escolha de ataque, ou seja, o menu em que
                    # o usuário escolhe o movimento que o pokémon irá fazer:
                    elif sub_menu.no_submenu(sub_menu.escolhendo_ataque):
                        # Se a tecla foi "Esc":
                        if event.key == pygame.K_ESCAPE:
                            # Toca o som:
                            arq.som_menu_mudou.play()
                            # Reconfigura a seta (ver a função para mais detalhes):
                            pos_2x2()
                            # Troca o sub menu atual para o principal:
                            sub_menu.atual = sub_menu.principal
                        # Se a tecla foi "Enter"
                        if event.key == pygame.K_RETURN:
                            # Toca o som de sempre:
                            arq.som_menu_mudou.play()
                            # Antes de fazer a ação, primeiro verificar se o movimento está bloqueado
                            # e se possui pp suficiente:
                            if not pokemons[0].movimentos[pos.i][0] in obter_id_bloqueados(pokemons[0]) and \
                                    pokemons[0].movimentos[pos.i][2] > 0:
                                # Executa a função que faz a ação correspondente ao item selecionado
                                # pelo cursor:
                                fazer_acao(sub_menu, pokemons[0].movimentos[pos.i], category.normal_move)
                    # Se o sub menu for o de itens (mochila):
                    elif sub_menu.no_submenu(sub_menu.itens):
                        # Se apertou "Esc":
                        if event.key == pygame.K_ESCAPE:
                            arq.som_menu_mudou.play()
                            pos_2x2()
                            # Volta para o sub menu principal:
                            sub_menu.atual = sub_menu.principal
                        # Aqui verificamos se apertou a tecla cima ou baixo:
                        if event.key == pygame.K_UP:
                            # Cima:
                            arq.som_menu_mudou.play()
                            # Faz a posição y da seta subir:
                            pos.y -= 1
                        elif event.key == pygame.K_DOWN:
                            # Baixo:
                            arq.som_menu_mudou.play()
                            # Faz o y descer:
                            pos.y += 1
                        # Se for "Enter":
                        if event.key == pygame.K_RETURN:
                            arq.som_menu_mudou.play()
                            # Será verificado primeiro se o item "0", que é o botão que aparece em cima dos itens,
                            # (botão "Cancelar") está selecionado:
                            if pos.i == 0:
                                # Reseta o cursor:
                                pos_2x2()
                                # Volta para o sub menu principal:
                                sub_menu.atual = sub_menu.principal
                            # Se não for o item "Cancelar", então a gente pega qual item está selecionado:
                            else:
                                # Agora a gente pega a posição do item selecionado, mas a gente subtrai -1, pois
                                # temos o item "Cancelar" que não está na lista, se não tivesse o "Cancelar", então
                                # não precisaria subtrair, pois o "Cancelar" não fica na lista de itens do pokémon:
                                item_selecionado = pos.i - 1
                                # Agora a gente executa a função que faz a ação que a gente passa como parâmetro:
                                fazer_acao(sub_menu, pokemons[0].itens[item_selecionado], category.item_move)
                                # Como a gente usou o item, então a gente tira ele da lista de itens, pois o item só
                                # se usa uma vez:
                                pokemons[0].itens.pop(item_selecionado)
                # Se estiver no menu de escolha de pokémons:
                elif menu.no_menu(menu.escolhendo_pokemon):
                    # A mesma lógica da seta comentada anteriormente:
                    if event.key == pygame.K_UP:
                        # Cima:
                        arq.som_menu_mudou.play()
                        pos.y -= 1
                    elif event.key == pygame.K_DOWN:
                        # Baixo:
                        arq.som_menu_mudou.play()
                        pos.y += 1
                    # Se a tecla foi "Enter":
                    elif event.key == pygame.K_RETURN:
                        # Significa que o usuário escolheu um pokémon:
                        arq.som_menu_mudou.play()
                        # Tocamos a música desejada:
                        tocar_musica("Dados/Recursos/Sprites/SonsPokemon/batalha.wav", True)
                        # Executamos a função que escolhe o pokémon:
                        escolher_pokemon(menu, sub_menu, mensagem)
                    # Por último, se for a tecla "Esc", sairemos do jogo:
                    elif event.key == pygame.K_ESCAPE:
                        # Faz a condição do while ser falsa:
                        rodando_o_jogo = False
                    # Obter o caractere digitado (Easter Egg):
                    caractere = pygame.key.name(event.key)
                    if easter_egg.processa_caractere(caractere):
                        ativar_easter_egg()

        # Chama a função que processa a lógica, ou seja, o tempo das animações, etc:
        processar_logica(delta, tempo, menu, sub_menu)
        # Agora a função que desenha os gráficos na janela:
        desenhar_graficos()
        # E a função que toca os sons:
        tocar_sons()

    # Quando o while terminar, chegaremos aqui, terminando o jogo.
    # Com isso, precisaremos terminar o pygame:
    pygame.quit()
