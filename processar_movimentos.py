import random
from global_vars import funcao
import arquivos as arq
def process_moves(pokemon_a_fazer, pokemon_a_tomar, move, mensagem, moves, tipos, effect):
    # códigos dos movimentos:
    num = random.randrange(0,101)
    
    if move == moves.growl[0]: # (Usando)
        # Growl lowers the target's Attack by one stage.
        pokemon_a_tomar.ataque -= 1
        mensagem.texto = "O ataque de {} diminuiu".format(pokemon_a_tomar.nome)
    elif move == moves.thunder_shock[0]: # (Usando)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10 and not tipos.electric in pokemon_a_tomar.tipos: # 10% de chance de ser paralizado:
            pokemon_a_tomar.bloqueado = 1
            pokemon_a_tomar.velocidade -= 50 * pokemon_a_fazer.velocidade / 100 #75%
            mensagem.texto = "e foi paralizado"
        arq.som_Thunder_Shock.play()
    elif move == moves.tail_whip[0]: # (Usando)
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "Defesa de {} diminuiu".format(pokemon_a_tomar.nome)

    elif move == moves.thunder_wave[0]: # (Usando) 
        #25% de chance do alvo não atacar
        pokemon_a_tomar.paralisado = True
        # Speed is decreased by 75%
        pokemon_a_tomar.velocidade -= 75 * pokemon_a_fazer.velocidade / 100
        mensagem.texto = "{} ficou paralisado".format(pokemon_a_tomar.nome)
    elif move == moves.metal_claw[0]: # (Usando)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_fazer.ataque -= 1
    elif move == moves.bubble[0]: # (Usando)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.velocidade -= 1
    elif move == moves.barrier[0]: # (Usando)
        pokemon_a_fazer.defesa += 2
        mensagem.texto = "{} aumentou sua defesa".format(pokemon_a_fazer.nome)
    elif move == moves.scratch[0]: # (Usando)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
    elif move == moves.tackle[0]: # (Usando) 
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Tackle.play()
    elif move == moves.leech_seed[0]: # (Usando)
        if not tipos.grass in pokemon_a_tomar.tipos:
            pokemon_a_tomar.add_effect(effect.leech_seed)
        else:
            mensagem.texto = "Parece que não surgiu efeito"
            
    elif move == moves.vine_whip[0]: # (Usando)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        
    elif move == moves.ember[0]: # (Usando)
        #10% de chance de queimar  
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10 and not tipos.fire in pokemon_a_tomar.tipos:
            pokemon_a_tomar.vida -= 1/8
            mensagem.texto = "e foi queimado"
        arq.som_Ember.play()
    elif move == moves.withdraw[0]: # (Usando)
        #aumenta a defesa em 1 estágio
        pokemon_a_fazer.defesa += 1
        mensagem.texto = "{} teve a defesa aumentada!".format(pokemon_a_fazer.nome)
        
    elif move == moves.fury_attack[0]: # (Usando)
        
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
            pokemon_a_fazer.atacar(pokemon_a_tomar)

        mensagem.texto = "{} tomou {} ataques".format(pokemon_a_tomar.nome, hits)
        
    elif move == moves.horn_attack[0]: # (Usando)
        #damage
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.stomp[0]: # (Usando)
        #damage e 30% de chance de fazer o alvo vacilar
        pokemon_a_tomar.precisao_temp -= 30
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Stomp.play()
    
    elif move == moves.hypnosis[0]: # (Usando)
        #o pokemon fica bloqueado por 1-3 rodadas
        pokemon_a_tomar.bloqueado = random.randrange(1, 4)
        mensagem.texto = "{} ficou bloqueado".format(pokemon_a_tomar.nome)
        arq.som_Hypnosis.play()
    elif moves == moves.lick[0]: # (Usando)
        #30% de chance de paralisar o alvo
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 30:              
            pokemon_a_tomar.paralisado = True
            mensagem.texto += "e foi paralisado"
        arq.som_Lick.play()
    elif move == moves.spite[0]: # (Usando)
        # perde 2-5 PP do ultimo movimento 
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
    
    elif move == moves.curse[0]: # (Usando)
        pokemon_a_tomar.vida_maxima -= pokemon_a_tomar.vida_maxima/2
        pokemon_a_tomar.vida -= pokemon_a_tomar.vida/4
        mensagem.texto = "{} perdeu HP".format(pokemon_a_tomar.nome)

    elif move == moves.leer[0]: # (Usando)
        #a defesa do alvo diminu em 1 estágio
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "{} teve sua defesa diminuida!".format(pokemon_a_tomar.nome)

    elif move == moves.twister[0]: # (Usando)
        #deals damage e o alvo tem chance de vacilar de 30%
        pokemon_a_tomar.precisao_temp -= 30
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Twister.play()
    elif move == moves.wrap[0]: # (Usando)
        # Wrap inflicts damage on the first turn then traps the opponent,
        # causing them to lose 1⁄8 of their maximum HP after each turn, for 4-5 turns. (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.confusion[0]: # (Usando)
        #damage e 1% de chance de diminuir a velocidade do alvo
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.confuso = True
            mensagem.texto += "e ficou confuso"
        arq.som_Confusion.play()
    elif move == moves.disable[0]: # (Usando)
        # bloqueia o movimento anterior por 1-8 turnos
        # Chance de 55% e verifica se teve o ultimo_movimento do pokemon inimigo:
        if num <= 55 and not pokemon_a_tomar.ultimo_movimento_id == None:
            turnos_a_desativar = random.randrange(1, 9)
            pokemon_a_tomar.adicionar_movimento_bloqueado(pokemon_a_tomar.ultimo_movimento_id, turnos_a_desativar)
            mensagem.texto = "{} teve seu último movimento desativado".format(pokemon_a_tomar.nome)
        else:
            mensagem.texto = "mas não funcionou"
        pass

    elif move == moves.mist[0]: # (Usando)
        # os dados do usuario nao mudam
        pokemon_a_fazer.protegido = 4
        mensagem.texto = "{} ficou protegido".format(pokemon_a_fazer.nome)

    elif move == moves.psychic[0]: # (Usando)
        #deals damage e menos 10% da defesa especial
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.especial_defesa -= 1

    elif move == moves.struggle[0]:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)