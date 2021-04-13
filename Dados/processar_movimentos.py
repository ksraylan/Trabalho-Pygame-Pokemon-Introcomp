# Importações:
import random

import Dados.arquivos as arq
from Dados.global_vars import funcao


def process_moves(pokemon_a_fazer, pokemon_a_tomar, move, mensagem, moves, tipos, effect):
    # Códigos dos movimentos:
    # num: número aleatório que representa a probabilidade como porcentagem (%):
    num = random.randrange(0, 100)  # de 0 a 100%
    # Obter a precisão do pokémon:
    precisao = pokemon_a_fazer.precisao_numero

    if move == moves.growl[0]:
        # Growl reduz o Ataque do alvo em um estágio:
        pokemon_a_tomar.ataque -= 1
        # Mostra a mensagem:
        mensagem.texto = "Ataque de {} diminuiu".format(pokemon_a_tomar.nome)
    elif move == moves.thunder_shock[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40, 100), mensagem)
        # O pokémon só é bloqueado se não for um pokémon elétrico:
        if num <= 10 * precisao and tipos.electric not in pokemon_a_tomar.tipos:  # 10% de chance de ser paralisado:
            # Bloqueado por 1 turno somente se ainda não foi bloqueado:
            if not pokemon_a_tomar.bloqueado:
                pokemon_a_tomar.bloqueado = 1
                # É reduzido a velocidade dele:
                pokemon_a_tomar.velocidade -= 50 * pokemon_a_fazer.velocidade / 100  # 75%
                mensagem.texto += " e foi paralisado"
        # Reproduz o efeito sonoro desse movimento:
        arq.som_Thunder_Shock.play()
    elif move == moves.tail_whip[0]:
        # Reduz a Defesa do alvo em um estágio.
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "Defesa de {} diminuiu".format(pokemon_a_tomar.nome)
    elif move == moves.thunder_wave[0]:
        # 25% de chance do alvo não atacar:
        pokemon_a_tomar.bloqueado = 1
        # A velocidade é reduzida em 75%:
        pokemon_a_tomar.velocidade -= 75 * pokemon_a_fazer.velocidade / 100
        mensagem.texto = "{} ficou bloqueado".format(pokemon_a_tomar.nome)
    elif move == moves.metal_claw[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 50, 95), mensagem)
        if num <= 10 * precisao:  # 10% de chance de seu ataque ser diminuído:
            pokemon_a_fazer.ataque -= 1
    elif move == moves.barrier[0]:
        # Aumenta a defesa do seu pokémon:
        pokemon_a_fazer.defesa += 2
        mensagem.texto = "{} aumentou a defesa".format(pokemon_a_fazer.nome)
    elif move == moves.scratch[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40, 100), mensagem)
    elif move == moves.tackle[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40, 100), mensagem)
        # Efeito sonoro:
        arq.som_Tackle.play()
    elif move == moves.leech_seed[0]:
        # Drena 1/8 do HP máximo:
        # Só funciona se o pokémon inimigo não é do tipo "grass", então adiciona o efeito::
        if tipos.grass not in pokemon_a_tomar.tipos and pokemon_a_tomar.add_effect(effect.leech_seed):
            # Mostra a mensagem:
            mensagem.texto = "{} foi semeado".format(pokemon_a_tomar.nome)
        else:
            # Mostra que não funcionou:
            mensagem.texto = "mas não funcionou"

    elif move == moves.vine_whip[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 45, 100), mensagem)

    elif move == moves.ember[0]:
        # Dano normal:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40, 100), mensagem)
        if num <= 10 * precisao and tipos.fire not in pokemon_a_tomar.tipos:  # e 10% de chance de queimar.
            pokemon_a_tomar.queimado = True
            mensagem.texto += " e foi queimado"
        # Toca o efeito sonoro:
        arq.som_Ember.play()
    elif move == moves.withdraw[0]:
        # Aumenta a defesa em 1 estágio
        pokemon_a_fazer.defesa += 1
        # Mostra que aumentou:
        mensagem.texto = "{} aumentou a defesa".format(pokemon_a_fazer.nome)

    elif move == moves.fury_attack[0]:
        # Probabilidade de 1 a 8
        probabilidade = random.randrange(1, 9)  # 1/8

        # Quantos golpes vai dar:
        if probabilidade <= 3:  # 3/8
            # Dar 2 golpes:
            hits = 2
        elif probabilidade <= 6:  # / 6/8 - 3/8 = 3/8
            # 3 golpes:
            hits = 3
        elif probabilidade <= 7:  # 1/8
            # 4 golpes:
            hits = 4
        else:  # 1/8
            # 5 golpes
            hits = 5
        # 3/8 + 3/8 + 1/8 + 1/8 = 8/8 = 1 (somando todas as probabilidades dá 1)

        # Vai dar golpes de acordo com a probabilidade de quantos_hits:
        for i in range(hits):
            pokemon_a_fazer.atacar(pokemon_a_tomar, 15, 100)

        mensagem.texto = "{} tomou {} golpes".format(pokemon_a_tomar.nome, hits)

    elif move == moves.horn_attack[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 65, 100), mensagem)

    elif move == moves.stomp[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou e 30% de chance de fazer o alvo vacilar:
        pokemon_a_tomar.precisao_temp -= 30
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 65, 100), mensagem)
        # Pega o som do move do arquivo.py:
        arq.som_Stomp.play()
    elif move == moves.hypnosis[0]:
        # O pokemon fica bloqueado por 1-3 rodadas:
        if not pokemon_a_tomar.bloqueado:  # Somente funcionar se ainda não foi bloqueado:
            pokemon_a_tomar.bloqueado = random.randrange(1, 4)
            mensagem.texto = "{} ficou bloqueado".format(pokemon_a_tomar.nome)
            # Pega o som do move do arquivo.py:
            arq.som_Hypnosis.play()
        else:
            mensagem.texto = "mas não funcionou"
    elif move == moves.lick[0]:
        # 30% de chance de paralisar o alvo e processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 20, 100), mensagem)
        # 30% de chance de ser bloqueado (somente se ainda não foi):
        if num <= 30 * precisao and not pokemon_a_tomar.bloqueado:
            pokemon_a_tomar.bloqueado = 1
            mensagem.texto += " e foi bloqueado"
        # Pega o som do move do arquivo.py:
        arq.som_Lick.play()
    elif move == moves.spite[0]:
        # Perde 2 a 5 PP do ultimo movimento que o pokémon inimigo fez:
        # Verificar antes se o pokémon fez algum último movimento:
        if pokemon_a_tomar.ultimo_movimento_id is not None:
            quantidade_perda_pp = random.randrange(2, 6)
            # Percorre a lista de movimentos até encontrar o id do último movimento:
            for i in range(len(pokemon_a_tomar.movimentos)):
                id_move = pokemon_a_tomar.movimentos[i][0]
                if id_move == pokemon_a_tomar.ultimo_movimento_id:
                    # Achou o último movimento
                    # Fazer o movimento perder pp:
                    pokemon_a_tomar.movimentos[i][2] -= quantidade_perda_pp
                    # Não pode deixar o pp ficar menor que 0:
                    if pokemon_a_tomar.movimentos[i][2] < 0:
                        pokemon_a_tomar.movimentos[i][2] = 0
                    # E dar break pois não precisa continuar procurando o movimento,
                    # pois já achou:
                    break
            # Mostra que perdeu pp e sua quantidade:
            mensagem.texto = "{} perdeu {} pp".format(pokemon_a_tomar.nome, quantidade_perda_pp)
        else:
            # O pokémon inimigo fez nenhum movimento ainda:
            mensagem.texto = "mas não funcionou"

    elif move == moves.curse[0]:
        # Perde metade de seu hp máximo do usuário:
        if tipos.ghost in pokemon_a_fazer.tipos:
            # Se o pokémon que está fazendo é um fantasma:
            if pokemon_a_tomar.add_effect(effect.curse):
                pokemon_a_fazer.vida_maxima -= pokemon_a_fazer.vida_maxima / 2

                # Mostra o que aconteceu:
                mensagem.texto = "{} ficou amaldiçoado".format(pokemon_a_tomar.nome)

                # Se tem menos da metade da vida máxima, seu pokémon desmaia:
                if pokemon_a_fazer.vida < pokemon_a_fazer.vida_maxima/2:
                    pokemon_a_fazer.vida = 0
            else:
                mensagem.texto = "não funcionou"
        else:
            # Ele não é um fantasma:
            pokemon_a_fazer.velocidade -= 1
            pokemon_a_fazer.ataque += 1
            pokemon_a_fazer.defesa += 1
            mensagem.texto = "{} teve estados aumentados".format(pokemon_a_fazer.nome)

    elif move == moves.leer[0]:
        # A defesa do alvo diminui em 1 estágio:
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "Defesa de {} diminuiu".format(pokemon_a_tomar.nome)

    elif move == moves.twister[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou e o alvo tem chance de vacilar de 30%:
        pokemon_a_tomar.precisao_temp -= 30
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40, 100), mensagem)
        # Toca o som do move:      
        arq.som_Twister.play()
    elif move == moves.wrap[0]:
        # Wrap inflige dano no primeiro turno, em seguida, prende o oponente,
        # fazendo com que percam 1⁄8 de seu HP máximo após cada turno.
        # Nas gerações 2-5, o alvo perde apenas 1/16 de seu HP máximo após cada turno
        # Nas gerações 1-4, Wrap tem 85% de precisão.
        # Processa o damage e mostra se errou e o quanto de vida tirou:

        # 85% de precisão, se funcionar, adiciona o efeito::
        if num <= 85 * precisao and pokemon_a_tomar.add_effect(effect.wrap):
            funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 15, 100), mensagem)
        else:
            # Errou:
            mensagem.texto = "mas não funcionou"

    elif move == moves.confusion[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou e 10% de chance de ficar bloqueado:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 50, 100), mensagem)
        if num <= 10 * precisao and not pokemon_a_tomar.bloqueado:  # 10% (só se ainda não foi bloqueado)
            pokemon_a_tomar.bloqueado = 1
            mensagem.texto += " e ficou bloqueado"
        # Toca o som:
        arq.som_Confusion.play()
    elif move == moves.disable[0]:
        # Bloqueia o movimento anterior por 1-8 turnos:
        # Chance de 55% e verifica se teve o ultimo_movimento do pokémon inimigo:
        if num <= 55 * precisao and pokemon_a_tomar.ultimo_movimento_id is not None:
            # Por quantos turnos estará desativado:
            turnos_a_desativar = random.randrange(1, 9)
            # Adiciona o movimento como bloqueado:
            pokemon_a_tomar.adicionar_movimento_bloqueado(pokemon_a_tomar.ultimo_movimento_id, turnos_a_desativar)
            # Mostra o que aconteceu:
            mensagem.texto = "Último movimento desativado ({})".format(pokemon_a_tomar.nome)
        else:
            # Mostra que não funcionou:
            mensagem.texto = "mas não funcionou"
        pass

    elif move == moves.mist[0]:
        # Os dados do usuário (ataque, defesa, etc) não mudam:
        pokemon_a_fazer.protegido = 4
        mensagem.texto = "{} ficou protegido".format(pokemon_a_fazer.nome)
    elif move == moves.bubble[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou e reduz a velocidade:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40, 100), mensagem)
        if num <= 10 * precisao:  # 10% de chance de sua velocidade diminuir:
            pokemon_a_tomar.velocidade -= 1
        # Toca o som:
        arq.som_Bubble.play()
    elif move == moves.psychic[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou e menos 10% da defesa especial:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 90, 100), mensagem)
        if num <= 10 * precisao:
            pokemon_a_tomar.especial_defesa -= 1

    elif move == moves.struggle[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou
        # e perde 1/4 de HP do dano que o inimigo recebeu:
        pokemon_a_fazer.vida -= funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 50, 100),
                                                                   mensagem) / 4
    elif move == moves.fugir[0]:
        # O movimento de fugir é feito na função process_moves (main.py)
        pass
