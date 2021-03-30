import random
from global_vars import funcao
import arquivos as arq
def process_moves(pokemon_a_fazer, pokemon_a_tomar, move, Acao, mensagem, moves, tipos, effect):
    print("Movimento executado:", move)
    # códigos dos movimentos:
    num = random.randrange(0,101)
    
    if move == Acao.ataque_simples:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
    if move == moves.growl[0]:
        # Growl lowers the target's Attack by one stage.
        pokemon_a_tomar.ataque -= 1
        mensagem.texto = "O ataque de {} diminuiu".format(pokemon_a_tomar.nome)
    elif move == moves.thunder_shock[0]:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10 and not tipos.electric in pokemon_a_tomar.tipos: # 10% de chance de ser paralizado:
            pokemon_a_tomar.bloqueado = 1
            pokemon_a_tomar.velocidade -= 50 * pokemon_a_fazer.velocidade / 100 #75%
            mensagem.texto = "e foi paralizado"
        arq.som_Thunder_Shock.play()
    elif move == moves.tail_whip[0]:
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "Defesa de {} diminuiu".format(pokemon_a_tomar.nome)

    elif move == moves.thunder_wave[0]: #25% de chance do alvo não atacar
        pokemon_a_tomar.paralisado = True
        # Speed is decreased by 75%
        pokemon_a_tomar.velocidade -= 75 * pokemon_a_fazer.velocidade / 100
        mensagem.texto = "{} ficou paralisado".format(pokemon_a_tomar.nome)

    elif move == moves.quick_attack[0]: #deals damage (IMPLEMENTAR ataque prioritário!)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Quick_Attack.play()
    elif move == moves.double_team[0]: # (IMPLEMENTAR)
        #pokemon_a_tomar. -= 1
        #pokemon_a_tomar.pode_fugir == False 
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        #mensagem.texto = "{} perdeu {} HP e sua chance de fugir diminuiu em um estágio!".format(pokemon_a_tomar.nome)
        
    elif move == moves.slam[0]: 
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        
    elif move == moves.thunderbolt[0]:#25% de chance do alvo não atacar
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.paralisado = True
            mensagem.texto = "e foi paralisado"
            
    elif move == moves.agility[0]: #aumenta velocidade em +2 estágios
        pokemon_a_fazer.velocidade += 2 
        mensagem.texto = "{} teve a velocidade aumentada".format(pokemon_a_fazer.nome)

    elif move == moves.thunder[0]:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 30:
            pokemon_a_tomar.paralisado = True
            mensagem.texto = "e foi paralisado"
        arq.som_Thunder.play()
    
    elif move == moves.scratch[0]:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.smokescreen[0]: #precisão do alvo reduz em 1 estágio
        pokemon_a_tomar.precisao -= 1
        mensagem.texto = "{} teve a precisão reduzida".format(pokemon_a_tomar.nome)

    elif move == moves.rage[0]: #ataque aumenta em 1 estágio
        pokemon_a_fazer.ataque += 1 
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        mensagem.texto += "e ataque aumentado"

    elif move == moves.scary_face[0]: #diminui velocidade do alvo em 2 estágios
        if num <= 90:
            pokemon_a_tomar.velocidade -= 2
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} teve a velocidade diminuida".format(pokemon_a_tomar.nome)
        else:
            mensagem.texto = "Parece que não surgiu efeito"

    elif move == moves.flamethrower[0]: #10% de chance de queimar (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.vida -= 1/16
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "e foi queimado" 
        arq.som_Flamethrower.play()
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
        arq.som_Tackle.play()
    elif move == moves.leech_seed[0]:
        if not tipos.grass in pokemon_a_tomar.tipos:
            pokemon_a_tomar.add_effect(effect.leech_seed)
        else:
            mensagem.texto = "Parece que não surgiu efeito"
            
    elif move == moves.vine_whip[0]:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        
    elif move == moves.poison_powder[0]: # veneno (IMPLEMENTAR)
        pokemon_a_tomar.vida -= pokemon_a_tomar.vida / 8
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} perdeu 1/8 HP!".format(pokemon_a_tomar.nome)

    elif move == moves.sleep_powder[0]: #coloca o alvo para dormir por até 3 turnos
        pokemon_a_tomar.bloqueado = 3 
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} dormindo por {} turnos!".format(pokemon_a_tomar.nome, 3)
        
    elif move == moves.razor_leaf[0]: #taxa de acerto crítico de 1/8 (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        
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
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10 and not tipos.fire in pokemon_a_tomar.tipos:
            pokemon_a_tomar.vida -= 1/8
            mensagem.texto = "e foi queimado"
        arq.som_Ember.play()
    elif move == moves.withdraw[0]: #aumenta a defesa em 1 estágio
        pokemon_a_fazer.defesa += 1
        mensagem.texto = "{} teve a defesa aumentada!".format(pokemon_a_fazer.nome)
        
    elif move == moves.water_gun[0]:
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        
    #elif move == moves.bite[0]: #30% de chance do alvo vacilar (IMPLEMENTAR)
        arq.som_Bite.play()
    elif move == moves.rapid_spin[0]:
        pokemon_a_fazer.velocidade += 1
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        mensagem.texto = "e sua velocidade aumentou"
    #elif move == moves.protect[0]: #protege o pokemon de quaisquer ataques (IMPLEMENTAR)
    #elif move == moves.rain_dance[0]: #provoca chuva (IMPLEMENTAR)
            
    elif move == moves.skull_bash[0]:#aumenta a defesa em +1 e dar dano segundo turno (IMPLEMENTAR)
        pokemon_a_fazer.defesa += 1
        mensagem.texto = "{} teve a defesa aumentada!".format(pokemon_a_fazer.nome)
        
    elif move == moves.hydro_pump[0]: #damage
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Hydro_Pump.play()
    elif move == moves.fury_attack[0]: # (IMPLEMENTAR) (efeito)
        pokemon_a_tomar.vida -= 1
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} perdeu 1 HP!".format(pokemon_a_tomar.nome)
        
    elif move == moves.horn_attack[0]:#damage
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.stomp[0]: #damage e 30% de chance de fazer o alvo vacilar (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Stomp.play()
    #elif move == moves.rock_blast[0]: #atinge 3 vezes por turno usado. A probabilidade de cada intervalo é mostrada à direita, com a potência total após cada acerto.Cada golpe de Rock Blast é tratado como um ataque separado (IMPLEMENTAR)
    elif move == moves.horn_drill[0]: #fará o oponente desmaiar (IMPLEMENTAR)
        pokemon_a_tomar.bloqueado = 3
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} desmaiou".format(pokemon_a_tomar.nome)

    elif move == moves.take_down[0]:#perde 25 hp (IMPLEMENTAR)
        pokemon_a_tomar.vida -=25
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} perdeu 1 HP!".format(pokemon_a_tomar.nome)
        
    elif move == moves.earthquake[0]: #o dano acertará com o dobro de poder (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        mensagem.texto = "{} perdeu x HP!".format(pokemon_a_tomar.nome)
        
    elif move == moves.megahorn[0]: #deals damage
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        arq.som_Megahorn.play()
    elif move == moves.hypnosis[0]:#o pokemon fica bloqueado por 3 rodadas (IMPLEMENTAR)
        pokemon_a_tomar.bloqueado = 3
        pokemon_a_fazer.atacar(pokemon_a_tomar)
        mensagem.texto = "{} desmaiou por {} turnos!".format(pokemon_a_tomar.nome, 3)
        arq.som_Hypnosis.play()
    elif moves == moves.lick[0]: #30% de chance de paralisar o alvo
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 30:              
            pokemon_a_tomar.paralisado = True
            mensagem.texto += "e foi paralisado"
        arq.som_Lick.play()
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
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
    elif move == moves.dream_eater[0]: # (IMPLEMENTAR) melhor.  #caso o pokemon esteja bloqueado o usuario recebe 50% de vida
        if pokemon_a_tomar.bloqueado:
            pokemon_a_fazer.vida += 50/100
            pokemon_a_fazer.atacar(pokemon_a_tomar)
            mensagem.texto = "{} aumentou o HP em 50%!".format(pokemon_a_fazer.nome)

    elif move == moves.destiny_bond[0]: #se o usuário desmaiar, o oponente também desmaia
        if pokemon_a_fazer.bloqueado is True:
            pokemon_a_tomar.bloqueado = True
            mensagem.texto = "{} desmaiou!".format(pokemon_a_tomar.nome)
        
    elif move == moves.shadow_ball[0]: #diminui a defesa especial do adversario em 20%
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 20:
            pokemon_a_tomar.especial_defesa -= 1
            mensagem.texto = "e sua defesa especial diminuiu"

    elif move == moves.nightmare[0]: #Se o alvo estiver dormindo, faz com que ele perca 1⁄4 de seu HP máximo (IMPLEMENTAR)
        if pokemon_a_tomar.bloqueado is True:
            pokemon_a_tomar.vida_maxima -= pokemon_a_tomar.vida_maxima/4
            mensagem.texto = "{} perdeu HP!".format(pokemon_a_tomar.nome)        
    
    elif move == moves.mean_look[0]:#oponente nao pode fugir ou mudar (IMPLEMENTAR o "mudar?")
        pokemon_a_tomar.pode_fugir = False
        mensagem.texto = "{} não pode fugir!".format(pokemon_a_tomar.nome) 

    elif move == moves.leer[0]: #a defesa do alvo diminu em 1 estágio
        pokemon_a_tomar.defesa -= 1
        mensagem.texto = "{} teve sua defesa diminuida!".format(pokemon_a_tomar.nome)

    elif  move == moves.twister[0]:#deals damage e o alvo tem chance de vacilar de 30% (IMPLEMENTAR o "vacilar")
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 30:
            mensagem.texto = "e fez ele vacilar"
        arq.som_Twister.play()
    elif move == moves.wrap[0]: #o alvo perde 1/8 HP (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.safeguard[0]: #deixa seu pokémon protegido contra ataques de estado
        pokemon_a_fazer.protegido = True

    elif move == moves.wing_attack[0]: #damage
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.outrage[0]:  # (IMPLEMENTAR)
        pokemon_a_fazer.atacar(pokemon_a_fazer)
    
    elif move == moves.hyperbeam[0]:# (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)

    elif move == moves.confusion[0]: #damage e 1% de chance de diminuir a velocidade do alvo
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.confuso = True
            mensagem.texto += "e ficou confuso"
        arq.som_Confusion.play()
    elif move == moves.disable[0]: # bloqueia o movimento anterior por 6 turnos (IMPLEMENTAR)
        pass

    elif move == moves.mist[0]:# os dados do usuario nao mudam
        pokemon_a_fazer.protegido = 4
        mensagem.texto = "{} ficou protegido".format(pokemon_a_fazer.nome)

    elif move == moves.swift[0]: #damage (IMPLEMENTAR)
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        
    elif move == moves.psychic[0]: #deals damage e menos 10% da defesa especial
        funcao.mostrar_texto_ataque_normal(pokemon_a_fazer.atacar(pokemon_a_tomar), mensagem)
        if num <= 10:
            pokemon_a_tomar.especial_defesa -= 1

    elif move == moves.psych_up[0]: #Copia as mudanças de estatísticas do oponente (IMPLEMENTAR)
        mensagem.texto = "{} fica com as estatísticas igual ao oponente!".format(pokemon_a_fazer.nome)        

    elif move == moves.recover[0]:#recupera 50% de hp
        pokemon_a_fazer.vida += 50 * pokemon_a_fazer.vida_maxima/100
        mensagem.texto = "{} recuperou HP".format(pokemon_a_fazer.nome)
        arq.som_Recover.play()
    elif move == moves.future_sight[0]:#deals damage (IMPLEMENTAR)
        pokemon_a_fazer.atacar(pokemon_a_tomar)
    
    elif move == moves.amnesia[0]: #aumeneta a defesa especial do usuário em dois estágios
        pokemon_a_fazer.especial_defesa += 2
        mensagem.texto = "{} aumentou a defesa especial".format(pokemon_a_fazer.nome)       