import random
import math
# Características de um pokémon:
class Pokemon:
    def __init__(self, nome, vida, ataque, defesa, velocidade, especial_ataque, especial_defesa, nivel, genero, imagens):
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

    @property
    def deslocamento(self):
        return self.__deslocamento

    @deslocamento.setter
    def deslocamento(self, deslocamento):
        self.__deslocamento = deslocamento

    def copy(self):
        return Pokemon(self.__nome, self.__vida, self.__ataque, self.__defesa, self.__velocidade, self.__especial_ataque, self.__especial_defesa, self.__nivel, self.__genero, [self.imagem_frente,self.imagem_costas])

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
        self.__vida = vida
        
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

    def batalha(self,ataque,outro_pokemon):
        outro_pokemon.vida -= ataque

    def foi_derrotado(self):
        return True if self.__vida <= 0 else False
    def conseguiu_fugir(self):
        return self.__fugiu

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
        if chance_critico <= 6.25:
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

    