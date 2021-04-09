#Importações:
import random
from global_vars import funcao
import arquivos as arq
def process_moves(pokemon_a_fazer, pokemon_a_tomar, move, mensagem, moves, tipos, effect):
    # códigos dos movimentos:
    num = random.randrange(0,101)
    
    if move == moves.growl[0]: 
        # Growl reduz o Ataque do alvo em um estágio:
        pokemon_a_tomar.ataque -= 1
        mensagem.texto = "O ataque de {} diminuiu".format(pokemon_a_tomar.nome)
    elif move == moves.thunder_shock[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40), mensagem)
        if num <= 10 and not tipos.electric in pokemon_a_tomar.tipos: # 10% de chance de ser paralizado:
            pokemon_a_tomar.bloqueado = 1
            pokemon_a_tomar.velocidade -= 50 * pokemon_a_fazer.velocidade / 100 #75%
            mensagem.texto = "e foi paralizado"
        arq.som_Thunder_Shock.play()
    elif move == moves.tail_whip[0]: 
        # Reduz a Defesa do alvo em um estágio.
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "Defesa de {} diminuiu".format(pokemon_a_tomar.nome)

    elif move == moves.thunder_wave[0]: 
        #25% de chance do alvo não atacar:
        pokemon_a_tomar.paralisado = True
        # A velocidade é reduzida em 75%:
        pokemon_a_tomar.velocidade -= 75 * pokemon_a_fazer.velocidade / 100
        mensagem.texto = "{} ficou paralisado".format(pokemon_a_tomar.nome)
    elif move == moves.metal_claw[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 50), mensagem)
        if num <= 10:
            pokemon_a_fazer.ataque -= 1
    elif move == moves.bubble[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou e reduz a velocidade:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40), mensagem)
        if num <= 10:
            pokemon_a_tomar.velocidade -= 1
    elif move == moves.barrier[0]: 
        # Aumenta a defesa do seu pokemon:
        pokemon_a_fazer.defesa += 2
        mensagem.texto = "{} aumentou sua defesa".format(pokemon_a_fazer.nome)
    elif move == moves.scratch[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40), mensagem)
    elif move == moves.tackle[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40), mensagem)
        arq.som_Tackle.play()
    elif move == moves.leech_seed[0]: 
        # Drena 1/8 do HP máximo:
        if not tipos.grass in pokemon_a_tomar.tipos:
            pokemon_a_tomar.add_effect(effect.leech_seed)
            mensagem.texto = "{} foi semeado".format(pokemon_a_tomar.nome)
        else:
            mensagem.texto = "mas não funcionou"
            
    elif move == moves.vine_whip[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 45), mensagem)
        
    elif move == moves.ember[0]:
        #10% de chance de queimar  
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40), mensagem)
        if num <= 10 and not tipos.fire in pokemon_a_tomar.tipos:
            pokemon_a_tomar.vida -= 1/8
            mensagem.texto = "e foi queimado"
        arq.som_Ember.play()
    elif move == moves.withdraw[0]:
        #aumenta a defesa em 1 estágio
        pokemon_a_fazer.defesa += 1
        mensagem.texto = "{} teve a defesa aumentada!".format(pokemon_a_fazer.nome)
        
    elif move == moves.fury_attack[0]:
        
        probabilidade = random.randrange(1,9) # 1/8

        quantos_hits = 0

        if probabilidade <= 3: #3/8
            hits = 2
        elif probabilidade <= 6: #/ 6/8 - 3/8 = 3/8
            hits = 3
        elif probabilidade <= 7: # 1/8
            hits = 4
        else: # 1/8
            hits = 5
        # 3/8 + 3/8 + 1/8 + 1/8 = 8/8 = 1 (somando todas as probabilidades dá 1)

        # vai dar hits de acordo com a probabilidade de quantos hits:
        for i in range(hits):
            num = random.randrange(0,101)
            pokemon_a_fazer.atacar(pokemon_a_tomar, 15)

        mensagem.texto = "{} tomou {} ataques".format(pokemon_a_tomar.nome, hits)
        
    elif move == moves.horn_attack[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 65), mensagem)

    elif move == moves.stomp[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou e 30% de chance de fazer o alvo vacilar:
        pokemon_a_tomar.precisao_temp -= 30
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 65), mensagem)
        arq.som_Stomp.play()
    elif move == moves.hypnosis[0]:
        #o pokemon fica bloqueado por 1-3 rodadas:
        pokemon_a_tomar.bloqueado = random.randrange(1, 4)
        mensagem.texto = "{} ficou bloqueado".format(pokemon_a_tomar.nome)
        arq.som_Hypnosis.play()
    elif move == moves.lick[0]:
        # 30% de chance de paralisar o alvo e processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 30), mensagem)
        if num <= 30:              
            pokemon_a_tomar.paralisado = True
            mensagem.texto += "e foi paralisado"
        arq.som_Lick.play()
    elif move == moves.spite[0]: 
        # perde 2-5 PP do ultimo movimento:
        # Verificar antes se o pokémon fez último movimento:
        if not pokemon_a_tomar.ultimo_movimento_id == None:
            quantidade_perda_pp = random.randrange(2,6)
            # percorre a lista de movimentos até encontrar o id do último movimento:
            for i in range(len(pokemon_a_tomar.movimentos)):
                id_move = pokemon_a_tomar.movimentos[i][0]
                if id_move == pokemon_a_tomar.ultimo_movimento_id:
                    # achou o último movimento
                    # fazer o movimento perder pp:
                    pokemon_a_tomar.movimentos[i][2] -= quantidade_perda_pp
                    # não pode deixar o pp ficar menor que 0:
                    if pokemon_a_tomar.movimentos[i][2] < 0:
                        pokemon_a_tomar.movimentos[i][2] = 0
                    # e dar break pois não precisa continuar procurando o movimento,
                    # pois já achou:
                    break
            mensagem.texto = "{} perdeu pp".format(pokemon_a_tomar.nome)
        else:
            mensagem.texto = "mas não funcionou"
    
    elif move == moves.curse[0]: 
        # Pokemon perde HP:
        pokemon_a_tomar.vida_maxima -= pokemon_a_tomar.vida_maxima/2
        pokemon_a_tomar.vida -= pokemon_a_tomar.vida/4
        mensagem.texto = "{} perdeu HP".format(pokemon_a_tomar.nome)

    elif move == moves.leer[0]: 
        #a defesa do alvo diminu em 1 estágio:
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "{} teve sua defesa diminuida!".format(pokemon_a_tomar.nome)

    elif move == moves.twister[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou e o alvo tem chance de vacilar de 30%:
        pokemon_a_tomar.precisao_temp -= 30
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 40), mensagem)
        arq.som_Twister.play()
    elif move == moves.wrap[0]:
        # Wrap inflige dano no primeiro turno, em seguida, prende o oponente,
        # fazendo com que percam 1⁄8 de seu HP máximo após cada turno (IMPLEMENTAR)
        # Nas gerações 1-4, os efeitos posteriores do Wrap duram 2-5 turnos em vez de 4-5;
        # Nas gerações 2-5, o alvo perde apenas 1/16 de seu HP máximo após cada turno
        # Nas gerações 1-4, Wrap tem 85% de precisão.
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 15), mensagem)

        if num <= 85:
            quantas_rodadas = random.randrange(2,6)
            pokemon_a_tomar.add_effect(effect.wrap)
        else:
            mensagem.texto = "mas não funcionou"
        

    elif move == moves.confusion[0]:
        # Processa o damage e mostra se errou e o quanto de vida tirou e 1% de chance de diminuir a velocidade do alvo:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 50), mensagem)
        if num <= 10:
            pokemon_a_tomar.confuso = True
            mensagem.texto += "e ficou confuso"
        arq.som_Confusion.play()
    elif move == moves.disable[0]: 
        # bloqueia o movimento anterior por 1-8 turnos:
        # Chance de 55% e verifica se teve o ultimo_movimento do pokemon inimigo:
        if num <= 55 and not pokemon_a_tomar.ultimo_movimento_id == None:
            turnos_a_desativar = random.randrange(1, 9)
            pokemon_a_tomar.adicionar_movimento_bloqueado(pokemon_a_tomar.ultimo_movimento_id, turnos_a_desativar)
            mensagem.texto = "{} teve seu último movimento desativado".format(pokemon_a_tomar.nome)
        else:
            mensagem.texto = "mas não funcionou"
        pass

    elif move == moves.mist[0]: 
        # os dados do usuário não mudam:
        pokemon_a_fazer.protegido = 4
        mensagem.texto = "{} ficou protegido".format(pokemon_a_fazer.nome)

    elif move == moves.psychic[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou e menos 10% da defesa especial:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 90), mensagem)
        if num <= 10:
            pokemon_a_tomar.especial_defesa -= 1

    elif move == moves.struggle[0]: 
        # Processa o damage e mostra se errou e o quanto de vida tirou:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar, 50), mensagem)