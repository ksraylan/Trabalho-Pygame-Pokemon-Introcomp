# Importações
import random
import math
from effect import Effect

vel_anim = 0.05
# A class with all stats of a pokémon (in this game). Contains methods
# that calculates the damage, things like that.
class Pokemon:
    def __init__(self, nome, vida, ataque, defesa, velocidade, especial_ataque, especial_defesa, nivel, genero, tipos, movimentos, imagens):
        # Contains all properties of a pokémon:
        self.__nome = nome
        self.__vida = vida/2
        self.__vida_anim = 0
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
        self.__pode_fugir = True
        self.__fugiu = False
        self.__sumido = False
        self.__sumindo = False
        self.__deslocamento = [0,0] # x, y
        self.__tipos = tipos
        self.__movimentos = movimentos
        self.__pokemon_effects = []
        # This is to easy acess to a "list" of all effects:
        self.effects = Effect()
        self.__bloqueado = 0
        self.__protegido = 0
        self.__paralisado = False
        self.__precisao = 1

    @property
    def precisao(self):
        return self.__precisao

    @precisao.setter
    def precisao(self, valor):
        self.__precisao = valor

    @property
    def paralisado(self):
        return self.__paralisado
    
    @paralisado.setter
    def paralisado(self, valor):
        self.paralisado = valor

    @property
    def vida_anim(self):
        return self.__vida_anim

    @vida_anim.setter
    def vida_anim(self, value):
        if value > self.__vida_maxima:
            value = self.__vida_maxima
        elif value < 0:
            value = 0
        self.__vida_anim = value

    @property
    def protegido(self):
        return self.__protegido
    
    @protegido.setter
    def protegido(self, value):
        self.__protegido = value

    def esta_protegido(self):
        return True if self.__protegido > 0 else False

    def atualiza_vida_anim(self, delta):
        valor = vel_anim * delta
        if self.__vida - valor/2 < self.__vida_anim < self.__vida + valor/2:
            self.vida_anim = self.vida
        elif self.__vida_anim < self.__vida:
            self.vida_anim += valor
        elif self.__vida_anim > self.__vida:
            self.vida_anim -= valor      

    def is_blocked(self):
        return True if self.__bloqueado > 0 else False

    @property
    def pode_fugir(self):
        return self.__pode_fugir
    
    @pode_fugir.setter
    def pode_fugir(self, value):
        self.__pode_fugir = value

    @property
    def bloqueado(self):
        return self.__bloqueado
    
    @bloqueado.setter
    def bloqueado(self, value):
        self.__bloqueado = value

    def batalha(self,ataque,outro_pokemon):
        # Deprecated!
        outro_pokemon.vida -= ataque

    def foi_derrotado(self):
        # Returns True if this pokémon is not alive (your life is below or equals 0):
        return True if self.__vida <= 0 else False
    def conseguiu_fugir(self):
        # Returns if this pokémon sucessful runned away:
        return self.__fugiu

    def process_effects(self, priority, enemy_pokemon):
        if priority is True:
            self.__bloqueado -= 1
            self.__protegido -= 1
        print("len:", len(self.__pokemon_effects))
        # Process all effects:
        for i in range(len(self.__pokemon_effects)):
            # Get a effect from the list of the effects of the current pokémon:
            effect_pokemon = self.__pokemon_effects[i]
            # Now it needs to verify if the priority of the effect from the pokémon
            # is equal to the current priority (True: before the turns; False: after
            # the turns.):
            print("loop part")
            if self.__pokemon_effects[i]["priority"] is priority:
                # Call the function that process the effect:
                self.__process_one_effect(effect_pokemon, enemy_pokemon)
                # (PRECISA COMENTAR!)
                print("prority part")
                if effect_pokemon["stops"] is not None and effect_pokemon["offset"] > effect_pokemon["stops"]:
                    self.__pokemon_effects.pop(i)
                else:
                    effect_pokemon["offset"] += 1

    def __process_one_effect(self, pokemon_effects, enemy_pokemon):
        # Get the list of all effects that exists in the code "effect.py":
        effects = self.effects
        # Now this verifies if the actual effect is equal a effect, if yes, do a
        # specific thing:
        if pokemon_effects["id"] == effects.leech_seed["id"]:
            vida_perdida = 12.5 * self.vida_maxima / 100
            self.vida -= vida_perdida
            enemy_pokemon.vida += vida_perdida
            print("Applied effect")
        

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
        ataque_critico = 1

        chance_critico = random.randrange(0, 101)
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
    def pokemon_effects(self):
        return self.__pokemon_effects

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
        place = True if not effect in self.__pokemon_effects else False
        if place:
            print("placed effect")
            self.__pokemon_effects.append(effect)
        else:
            print("not placed effect")
        return place

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
        if not self.__protegido:
            self.__ataque = ataque

    @defesa.setter
    def defesa(self,defesa):
        if not self.__protegido:
            self.__defesa = defesa

    @velocidade.setter
    def velocidade(self,velocidade):
        if not self.__protegido:
            self.__velocidade = velocidade
    
    @especial_ataque.setter
    def especial_ataque(self,especial):
        if not self.__protegido:
            self.__especial_ataque = especial

    @especial_defesa.setter
    def especial_defesa(self,especial):
        if not self.__protegido:
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