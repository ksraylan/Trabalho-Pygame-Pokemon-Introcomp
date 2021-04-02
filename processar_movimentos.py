import random
from global_vars import funcao
import arquivos as arq
def process_moves(pokemon_a_fazer, pokemon_a_tomar, move, mensagem, moves, tipos, effect):
    print("Movimento executado:", move)
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
    elif move == moves.metal_claw[0]: # (Usando) (IMPLEMENTAR)
        pass
    elif move == moves.bubble[0]: # (Usando) (IMPLEMENTAR)
        pass
    elif move == moves.barrier[0]: # (Usando)
        pass
    elif move == moves.scratch[0]: # (Usando)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.tackle[0]: # (Usando) 
        #power of 35 e 95% acerto (IMPLEMENTAR)
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} perdeu x HP!".format(pokemon_a_tomar.nome)
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
        # (IMPLEMENTAR) (efeito)
        pokemon_a_tomar.vida -= 1
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} perdeu 1 HP!".format(pokemon_a_tomar.nome)
        
    elif move == moves.horn_attack[0]: # (Usando)
        #damage
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.stomp[0]: # (Usando)
        #damage e 30% de chance de fazer o alvo vacilar (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Stomp.play()
    
    elif move == moves.hypnosis[0]: # (Usando)
        #o pokemon fica bloqueado por 3 rodadas (IMPLEMENTAR)
        pokemon_a_tomar.bloqueado = 3
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} desmaiou por {} turnos!".format(pokemon_a_tomar.nome, 3)
        arq.som_Hypnosis.play()
    elif moves == moves.lick[0]: # (Usando)
        #30% de chance de paralisar o alvo
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 30:              
            pokemon_a_tomar.paralisado = True
            mensagem.texto += "e foi paralisado"
        arq.som_Lick.play()
    elif move == moves.spite[0]: # (Usando)
        #perde 2-5 PP (oponente) (IMPLEMENTAR) (PP)
        pass
    
    elif move == moves.curse[0]: # (Usando) (IMPLEMENTAR) (VER DE NOVO)
        pokemon_a_tomar.vida -= 25/100
        pokemon_a_fazer.vida_maxima -= 50/100
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} perdeu 25% HP e 50% HP máximo!".format(pokemon_a_tomar.nome)

    elif move == moves.leer[0]: # (Usando)
        #a defesa do alvo diminu em 1 estágio
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "{} teve sua defesa diminuida!".format(pokemon_a_tomar.nome)

    elif move == moves.twister[0]: # (Usando)
        #deals damage e o alvo tem chance de vacilar de 30% (IMPLEMENTAR o "vacilar")
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 30:
            mensagem.texto = "e fez ele vacilar"
        arq.som_Twister.play()
    elif move == moves.wrap[0]: # (Usando)
        #o alvo perde 1/8 HP (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.confusion[0]: # (Usando)
        #damage e 1% de chance de diminuir a velocidade do alvo
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.confuso = True
            mensagem.texto += "e ficou confuso"
        arq.som_Confusion.play()
    elif move == moves.disable[0]: # (Usando)
        # bloqueia o movimento anterior por 6 turnos (IMPLEMENTAR)
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