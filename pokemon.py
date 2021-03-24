# Importações
import random
import math
from effect import Effect, compare_effects
# Classe que possui as características de um pokémon:
class Pokemon:
    def __init__(self, nome, vida, ataque, defesa, velocidade, especial_ataque, especial_defesa, nivel, genero, tipos, movimentos, imagens):
        self.__nome = nome
        self.__vida = vida
        self.__vida_maxima = vida
        self.__ataque = ataque
        self.__defesa = defesa
        self.__velocidade = velocidade
        self.__especial_ataque = especial_ataque
        self.__especial_defesa = especial_defesa
        self.__nivel = nivel
        self.__genero = genero
        self.__imagem_costas = imagens[1]
        self.__imagem_frente = imagens[0]
        self.__tentou_fugir = 0
        self.__fugiu = False
        self.__sumido = False
        self.__sumindo = False
        self.__deslocamento = [0,0] # x, y
        self.__tipos = tipos
        self.__movimentos = movimentos
        self.__effects = []
        self.effect = Effect()

    def batalha(self,ataque,outro_pokemon):
        outro_pokemon.vida -= ataque

    def foi_derrotado(self):
        return True if self.__vida <= 0 else False
    def conseguiu_fugir(self):
        return self.__fugiu

    def process_effects(self, priority, enemy_pokemon):
        effect = self.effect
        # id, offset, stops ,priority (True = before turns, False = atfer all turns)
        for i in range(len(self.__effects)):
            # processa efeito por efeito:
            effect_pokemon = self.__effects[i]
            if compare_effects(effect.leech_seed, effect_pokemon, priority):
                vida_perdida = 12.5 * self.vida_maxima / 100
                self.vida -= vida_perdida
                enemy_pokemon.vida += vida_perdida
                print("Applied effect")

            if effect_pokemon["offset"] > effect_pokemon["stops"]:
                self.__effects.pop(i)
            else:
                effect_pokemon["offset"] += 1
        

    def atacar(self, outro_pokemon):
        # A = Accuracymove * Adjusted_stages * Other_mods
        A = random.randrange(0,101) * 1 * 1
        # The game then selects a random number R from 1 to 100 and compares it to A
        # to determine whether the move hits. If R is less than or equal to A, the move hits.
        R = random.randrange(0, 101)
        acertou = 1 if R <= A else 0

        multiplicador_critico = (2 * self.__nivel + 5) / (self.__nivel + 5)
        # poder (teste):
        poder = 1
        print("Ataque: ", self.__ataque)
        ataque_critico = 1

        chance_critico = random.randrange(0, 101)
        print("Chance crítico: ", chance_critico)
        if chance_critico <= 33.33:
            ataque_critico = multiplicador_critico

        # modificador = alvos * tempo_meteorológico * Badge * ataque_critico * aleatorio de 0.85 a 1.00 * bônus de ataque do mesmo tipo * tipo * queimado * outro (não precisa)
        modificador = 1 * 1 * 1 * ataque_critico * (random.randrange(85, 100)/100) * 1 * 1 * 1 * 1
        formula = ( (((2 * self.__nivel)/ 5 + 2) * poder * self.__ataque / outro_pokemon.defesa) / 50 + 2) * modificador * acertou
        formula = math.trunc(formula)
        outro_pokemon.vida -= formula
        return formula

    
    def fugir_de(self, outro_pokemon):
        self.__tentou_fugir += 1
        A = self.__velocidade
        B = outro_pokemon.velocidade
        C = self.__tentou_fugir
        F = ((A * 128/B) + 30 * C) % 256

        if random.randrange(0, 255) < F:
            self.__fugiu = True
            return True
        else:
            # não conseguiu
            return False
    
    def cura(self, quantidade):
        self.__vida += quantidade

    @property
    def effects(self):
        return self.__effects

    @property
    def tipos(self):
        return self.__tipos

    @property
    def movimentos(self):
        return self.__movimentos

    @property
    def deslocamento(self):
        return self.__deslocamento

    @deslocamento.setter
    def deslocamento(self, deslocamento):
        self.__deslocamento = deslocamento

    def copy(self):
        return Pokemon(self.__nome, self.__vida, self.__ataque, self.__defesa, self.__velocidade, self.__especial_ataque, self.__especial_defesa, self.__nivel, self.__genero, self.__tipos, self.__movimentos, [self.imagem_frente,self.imagem_costas])

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
       if self.__vida < 0:
            return 0
       else:
            return self.__vida

    @property
    def vida_maxima(self):
        return self.__vida_maxima
    
    @property
    def ataque(self):
        return self.__ataque
    
    @property
    def defesa(self):
        return self.__defesa

    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def especial_ataque(self):
        return self.__especial_ataque

    @property
    def especial_defesa(self):
        return self.__especial_defesa

    @property
    def genero(self):
        return self.__genero

    @property
    def imagem_costas(self):
        return self.__imagem_costas

    @property
    def imagem_frente(self):
        return self.__imagem_frente

    @property
    def nivel(self):
        return self.__nivel

    @property
    def sumido(self):
        return self.__sumido
    
    @property
    def sumindo(self):
        return self.__sumindo

    def inverte_sumido(self):
        self.__sumido = not self.__sumido



    # setters:

    def add_effect(self, effect):
        placed = True if not effect in self.__effects else False
        if placed:
            self.__effects.append(effect)
        return placed

    @sumindo.setter
    def sumindo(self, sumindo):
        self.__sumindo = sumindo
        self.__sumido = sumindo

    @sumido.setter
    def sumido(self, valor):
        self.__sumido = valor

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @vida.setter
    def vida(self,vida):
        vida_a_setar = vida

        if vida_a_setar < 0:
            vida_a_setar = 0
        elif vida_a_setar > self.__vida_maxima:
            vida_a_setar = self.__vida_maxima

        self.__vida = vida_a_setar
        
    @ataque.setter
    def ataque(self,ataque):
        self.__ataque = ataque

    @defesa.setter
    def defesa(self,defesa):
        self.__defesa = defesa

    @velocidade.setter
    def velocidade(self,velocidade):
        self.__velocidade = velocidade
    
    @especial_ataque.setter
    def especial_ataque(self,especial):
        self.__especial_ataque = especial

    @especial_defesa.setter
    def especial_defesa(self,especial):
        self.__especial_defesa = especial

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @imagem_costas.setter
    def imagem_costas(self,imagem_costa):
        self.__imagem_costas = imagem_costa

    @imagem_frente.setter
    def imagem_frente(self,imagem_frente):
        self.__imagem_frente = imagem_frente

    @nivel.setter
    def nivel(self,nivel):
        self.__nivel = nivel

    
class Tipos:
    def __init__(self):
        pass
    @property
    def normal(self):
        return 0
    @property
    def fire(self):
        return 1
    @property
    def water(self):
        return 2
    @property
    def grass(self):
        return 3
    @property
    def electric(self):
        return 4
    @property
    def ice(self):
        return 5
    @property
    def fighting(self):
        return 6
    @property
    def poison(self):
        return 7
    @property
    def ground(self):
        return 8
    @property
    def flying(self):
        return 9
    @property
    def psychic(self):
        return 10
    @property
    def bug(self):
        return 11
    @property
    def rock(self):
        return 12
    @property
    def ghost(self):
        return 13
    @property
    def dragon(self):
        return 14
    @property
    def dark(self):
        return 15
    @property
    def steel(self):
        return 16
"""
class Tipo_Movimento:
    def __init__(self):
        pass

    @property
    def ataque_simples(self):
        return 0
    @property
    def diminuir_defesa(self):
        return 1
    @property
    def consome_vida_por_rodada(self):
        return 2
    @property
    def veneno(self):
        return 3
    @property
    def colocar_para_dormir(self):
        return 4
    @property
    def diminuir_ataque(self):
        return 5
    @property
    def diminuir_especial_ataque(self):
        return 6
    @property
    def cura(self):
        return 7
    @property

    
"""
class Movimento:
    def __init__(self):
        pass

    # geração 3 (talvez não precise):
    
    @property
    def aerial_ace(self):
        return 0
    @property
    def air_cutter(self):
        return 1
    @property
    def arm_thrust(self):
        return 2
    @property
    def aromatherapy(self):
        return 3
    @property
    def assist(self):
        return 4
    @property
    def astonish(self):
        return 5
    @property
    def blast_burn(self):
        return 6
    @property
    def blaze_kick(self):
        return 7
    @property
    def block(self):
        return 8
    @property
    def bounce(self):
        return 9
    @property
    def brick_break(self):
        return 10
    @property
    def bulk_up(self):
        return 11
    @property
    def bullet_seed(self):
        return 12
    @property
    def calm_mind(self):
        return 13
    @property
    def camouflage(self):
        return 14
    @property
    def charge(self):
        return 15
    @property
    def cosmic_power(self):
        return 16
    @property
    def covet(self):
        return 17
    @property
    def crush_claw(self):
        return 18
    @property
    def dive(self):
        return 19
    @property
    def doom_desire(self):
        return 20
    @property
    def dragon_claw(self):
        return 21
    @property
    def dragon_dance(self):
        return 22
    @property
    def endeavor(self):
        return 23
    @property
    def eruption(self):
        return 24
    @property
    def extrasensory(self):
        return 25
    @property
    def facade(self):
        return 26
    @property
    def fake_out(self):
        return 27
    @property
    def fake_tears(self):
        return 28
    @property
    def feather_dance(self):
        return 29
    @property
    def flatter(self):
        return 30
    @property
    def focus_punch(self):
        return 31
    @property
    def follow_me(self):
        return 32
    @property
    def frenzy_plant(self):
        return 33
    @property
    def grass_whistle(self):
        return 34
    @property
    def grudge(self):
        return 35
    @property
    def hail(self):
        return 36
    @property
    def heat_wave(self):
        return 37
    @property
    def helping_hand(self):
        return 38
    @property
    def howl(self):
        return 39
    @property
    def hydro_cannon(self):
        return 40
    @property
    def hyper_voice(self):
        return 41
    @property
    def ice_ball(self):
        return 42
    @property
    def icicle_spear(self):
        return 43
    @property
    def imprison(self):
        return 44
    @property
    def ingrain(self):
        return 45
    @property
    def iron_defense(self):
        return 46
    @property
    def knock_off(self):
        return 47
    @property
    def leaf_blade(self):
        return 48
    @property
    def luster_purge(self):
        return 49
    @property
    def magic_coat(self):
        return 50
    @property
    def megical_leaf(self):
        return 51
    @property
    def memento(self):
        return 52
    @property
    def metal_sound(self):
        return 53
    @property
    def meteor_mash(self):
        return 54
    @property
    def mist_ball(self):
        return 55
    @property
    def mud_shot(self):
        return 56
    @property
    def mud_sport(self):
        return 57
    @property
    def muddy_water(self):
        return 58
    @property
    def nature_power(self):
        return 59
    @property
    def needle_arm(self):
        return 60
    @property
    def odor_sleuth(self):
        return 61
    @property
    def overheat(self):
        return 62
    @property
    def poison_fang(self):
        return 63
    @property
    def poison_tail(self):
        return 64
    @property
    def psycho_boost(self):
        return 65
    @property
    def recycle(self):
        return 66
    @property
    def reflesh(self):
        return 67
    @property
    def revenge(self):
        return 68
    @property
    def rock_blast(self):
        return [69, "Rock Blast"]
    @property
    def rock_tomb(self):
        return 70
    @property
    def role_play(self):
        return 71
    @property
    def sand_tomb(self):
        return 72
    @property
    def secret_power(self):
        return 73
    @property
    def shadow_punch(self):
        return [74, "Shadow Punch"]
    @property
    def sheer_cold(self):
        return 75
    @property
    def shock_wave(self):
        return 76
    @property
    def signal_beam(self):
        return 77
    @property
    def silver_wind(self):
        return 78
    @property
    def skill_swap(self):
        return 79
    @property
    def sky_uppercut(self):
        return 80
    @property
    def slack_off(self):
        return 81
    @property
    def smelling_salts(self):
        return 82
    @property
    def snatch(self):
        return 83
    @property
    def spit_up(self):
        return 84
    @property
    def stockpile(self):
        return 85
    @property
    def superpower(self):
        return 86
    @property
    def swallow(self):
        return 87
    @property
    def tail_grow(self):
        return 88
    @property
    def taunt(self):
        return 89
    @property
    def teeter_dance(self):
        return 90
    @property
    def tickle(self):
        return 91
    @property
    def torment(self):
        return 92
    @property
    def trick(self):
        return 93
    @property
    def uproar(self):
        return 94
    @property
    def volt_tackle(self):
        return 95
    @property
    def water_pulse(self):
        return 96
    @property
    def water_sport(self):
        return 97
    @property
    def water_spout(self):
        return 98
    @property
    def wheather_ball(self):
        return 99
    @property
    def will_o_wisp(self):
        return 100
    @property
    def wish(self):
        return 101
    @property
    def yawm(self):
        return 102
    
    # geração 1:
    @property
    def tackle(self):
        return [-1, "Tackle"]
    @property
    def growl(self):
        return [-2, "Growl"]
    @property
    def leech_seed(self):
        return [-3, "Leech Seed"]
    @property
    def vine_whip(self):
        return [-4, "Vine Whip"]
    @property
    def poison_powder(self):
        return [-5, "Poison Powder"]
    @property
    def sleep_powder(self):
        return [-6, "Sleep Powder"]
    @property
    def razor_leaf(self):
        return [-7, "Razor Leaf"]
    @property
    def sweet_scent(self):
        return [-8, "Sweet Scent"]
    @property
    def growth(self):
        return [-9, "Growth"]
    @property
    def synthesis(self):
        return [-10, "Synthesis"]
    @property
    def solar_beam(self):
        return [-11, "Solar Beam"]
    @property
    def thunder_shock(self):
        return [-12, "Thunder Shock"]
    @property
    def tail_whip(self):
        return [-13, "Tail Whip"]
    @property
    def quick_attack(self):
        return [-14, "Quick Attack"]
    @property
    def double_team(self):
        return [-15, "Double Team"]
    @property
    def slam(self):
        return [-16, "Slam"]
    @property
    def thunderbolt(self):
        return [-17, "Thunderbolt"]
    @property
    def agility(self):
        return [-18, "Agility"]
    @property
    def thunder(self):
        return [-19, "Thunder"]
    @property
    def light_screen(self):
        return [-20, "Light Screen"]
    @property
    def thunder_wave(self):
        return [-21, "Thunder Wave"]
    @property
    def scratch(self):
        return [-22, "Scratch"]
    @property
    def ember(self):
        return [-23, "Ember"]
    @property
    def mokescreen(self):
        return [-24, "Mokescreen"]
    @property
    def rage(self):
        return [-25, "Rage"]
    @property
    def scary_face(self):
        return [-26, "Scary Face"]
    @property
    def flamethrower(self):
        return [-27, "Flamethrower"]
    @property
    def slash(self):
        return [-28, "Slash"]
    @property
    def dragon_rage(self):
        return [-29, "Dragon Rage"]
    @property
    def fire_spin(self):
        return [-30, "Fire Spin"]
    @property
    def withdraw(self):
        return [-31, "Withdraw"]
    @property
    def water_gun(self):
        return [-32, "Water Gun"]
    @property
    def bite(self):
        return [-33, "Bite"]
    @property
    def rapid_spin(self):
        return [-34, "Rapid Spin"]
    @property
    def protect(self):
        return [-35, "Protect"]
    @property
    def rain_dance(self):
        return [-36, "Rain Dance"]
    @property
    def skull_bash(self):
        return [-37, "Skull Bash"]
    @property
    def bubble(self):
        return [-38, "Bubble"]
    @property
    def hydro_pump(self):
        return [-39, "Hydro Pump"]
    @property
    def fury_attack(self):
        return [-40, "Fury Attack"]
    @property
    def horn_attack(self):
        return [-41, "Horn Attack"]
    @property
    def stomp(self):
        return [-42, "Stomp"]
    @property
    def horn_drill(self):
        return [-43, "Horn Drill"]
    @property
    def take_down(self):
        return [-44, "Take Down"]
    @property
    def earthquake(self):
        return [-45, "Earthquake"]
    @property
    def megahorn(self):
        return [-46, "Megahorn"]
    @property
    def curse(self):
        return [-47, "Curse"]
    @property
    def night_shade(self):
        return [-48, "Night Shade"]
    @property
    def confuse_ray(self):
        return [-49, "Confuse Ray"]
    @property
    def dream_eater(self):
        return [-50, "Dream Eater"]
    @property
    def destiny_bond(self):
        return [-51, "Destiny Bond"]
    @property
    def hypnosis(self):
        return [-52, "Hypnosis"]
    @property
    def lick(self):
        return [-53, "Lick"]
    @property
    def spite(self):
        return [-54, "Spite"]
    @property
    def shadow_ball(self):
        return [-55, "Shadow Ball"]
    @property
    def nightmare(self):
        return [-56, "Nightmare"]
    @property
    def mean_look(self):
        return [-57,"Mean Look"]
    @property
    def leer(self):
        return [-58, "Leer"]
    @property
    def twister(self):
        return [-59, "Twister"]
    @property
    def wrap(self):
        return [-60, "Wrap"]
    """
    @property
    def drago_rage(self):
        return [-61,"Drago Rage"]
    """
    @property
    def safeguard(self):
        return [-62,"Safeguard"]
    @property
    def wing_attack(self):
        return [-63, "Wing Attack"]
    @property
    def outrage(self):
        return [-64, "Outrage"]
    @property
    def hyperbeam(self):
        return [-65, "Hyperbeam"]
    @property
    def confusion(self):
        return [-66, "Confusion"]
    @property
    def disable(self):
        return [-67, "Disable"]
    @property
    def barrier(self):
        return [-68, "Barrier"]
    @property
    def mist(self):
        return [-69,"Mist"]
    @property
    def swift(self):
        return [-70, "Swift"]
    @property
    def recover(self):
        return [-71, "Recover"]
    @property
    def psychic(self):
        return [-72, "Psychic"]
    @property
    def psych_up(self):
        return [-73, "Psych Up"]
    @property
    def future_sight(self):
        return [-74,"Future Sight"]
    @property
    def amnesia(self):
        return [-75,"Amnesia"]





class Ataque:
    def __init__(self, valor, precisao, chance_critico, tipo_movimento,):
        self.__valor = valor
        self.__precisao = precisao
        self.__chance_critico = chance_critico
        self.__tipo_movimento = tipo_movimento
        
    @property
    def valor(self):
        return self.__valor
        
    @property
    def precisao(self):
        return self.__precisao

    @property
    def chance_critico(self):
        return self.__chance_critico
    
    @property
    def tipo_movimento(self):
        return self.__tipo_movimento