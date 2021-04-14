# Importações:
# Importação da biblioteca que randomiza os números:
# Importação da biblioteca da matemática:
import math
import random

# Importar os arquivos:
import Dados.arquivos as arq
# Importação dos efeitos:
from Dados.effect import Effect
from Dados.global_vars import funcao

# Velocidade da animação da barra de vida:
vel_anim = 0.03
# Velocidade da animação do pokémon e da barra:
vel_anim_2 = 0.005
# Velocidade da animação de entrada:
vel_anim_3 = 0.0005
# Aumenta isso a cada nível:
multiplicador_nivel = 0.5


# Uma class com todas as estatísticas de um pokémon (neste jogo). Contém métodos
# que calculam o dano, coisas assim:
class Pokemon:
    def __init__(self, nome, vida, ataque, defesa, velocidade, especial_ataque, especial_defesa, nivel, chance_genero,
                 tipos, movimentos, itens, imagem_id, is_easter_egg):
        # Contém todas as propriedades do pokémon:
        self.__nome = nome
        # Multiplicador de nível:
        multiplicando = int((nivel - 1) * multiplicador_nivel)
        self.__vida = vida + multiplicando
        self.__vida_anim = 0
        self.__vida_maxima = vida + multiplicando
        self.__ataque = ataque + multiplicando
        self.__defesa = defesa + multiplicando
        self.__velocidade = velocidade + multiplicando
        self.__especial_ataque = especial_ataque + multiplicando
        self.__especial_defesa = especial_defesa + multiplicando
        self.__nivel = nivel
        self.__imagem_id = imagem_id
        self.__is_easter_egg = is_easter_egg

        if not is_easter_egg:
            # Se não for Easter Egg carrega a imagem dos pokémons normais:
            imagens = arq.carregar_imagem_pokemon(imagem_id, funcao.shiny_aleatorio())
        else:
            # Caso seja carrega as imagens do Easter Egg:
            imagens = arq.carregar_imagem_easter_egg(imagem_id)

        # Coloca as imagens correspondentes:
        self.__imagem_costas = imagens[1]
        self.__imagem_frente = imagens[0]
        self.__tentou_fugir = 0
        self.__pode_fugir = True
        self.__fugiu = False
        self.__sumido = False
        self.__sumindo = False
        self.__deslocamento = [0, 0]  # x, y
        self.__tipos = tipos
        self.__conjunto_movimentos = movimentos
        self.__chance_genero = chance_genero  # chance em porcentagem de ser feminino
        # O que sobrou da porcentagem é a chance de ser masculino.

        # Se especificou um gênero específico:
        if chance_genero == "F" or chance_genero == "M":
            self.__genero = chance_genero
        # Se não tiver gênero:
        elif chance_genero is None:
            self.__genero = ""
        else:
            # Calcula a probabilidade:
            chance_feminino = random.randrange(0, 100)  # de 0% a 100%
            if chance_feminino <= chance_genero:
                # É feminino:
                self.__genero = "F"
            else:
                # É masculino:
                self.__genero = "M"

        # Lista com os movimentos:
        self.__movimentos = []
        for i in range(len(movimentos)):
            # Transforma os movimentos que estão em tuplas em listas:
            self.__movimentos.append(list(movimentos[i]))

        # Isso facilita o acesso a uma "lista" de todos os efeitos:
        self.effects = Effect()
        # Por quantas rodadas ficará bloqueado:
        self.__bloqueado = 0
        # Por quantas rodadas ficará protegido (não muda o ataque, defesa, etc):
        self.__protegido = 0
        # Precisão:
        self.__precisao = 1
        # Itens que o pokémon terá na mochila:
        self.__itens = itens
        # Chance de ataque crítico:
        self.__ataque_critico = 0
        # precisão do movimento que se aplica apenas em uma rodada:
        self.__precisao_temp = 100
        # O último movimento executado por ele:
        self.__ultimo_movimento_id = None
        # Lista com os movimentos que não podem ser usados
        self.__movimentos_bloqueados = []
        # Efeitos que o pokémon "pega" do outro:
        self.__pokemon_effects = []  # Começa com nenhum efeito
        # Se está queimado:
        self.queimado = False
        # Posição do pokémon e da barra (offset):
        self.pos_offset = 0
        self.pos_offset_descendo = True
        self.circulo_offset = 1

    def pos_offset_parar(self):
        # Reseta a animação do pokémon se mexendo:
        self.pos_offset = 0
        self.pos_offset_descendo = True

    def processar_pos_offset(self, delta):
        # Animação do pokémon se mexendo:
        if self.pos_offset_descendo:
            self.pos_offset += vel_anim_2 * delta
            while self.pos_offset > 1:
                self.pos_offset_descendo = False
                self.pos_offset -= vel_anim_2 * delta
        else:
            self.pos_offset -= vel_anim_2 * delta
            while self.pos_offset < 0:
                self.pos_offset_descendo = True
                self.pos_offset += vel_anim_2 * delta

    def processar_circulo_anim(self, delta):
        if not self.circulo_offset == 0:
            self.circulo_offset -= delta * vel_anim_3
            if self.circulo_offset < 0:
                self.circulo_offset = 0

    # Getters e setters:
    @property
    def ultimo_movimento_id(self):
        return self.__ultimo_movimento_id

    @ultimo_movimento_id.setter
    def ultimo_movimento_id(self, valor):
        self.__ultimo_movimento_id = valor

    @property
    def movimentos_bloqueados(self):
        return self.__movimentos_bloqueados

    @movimentos_bloqueados.setter
    def movimentos_bloqueados(self, valor):
        self.__movimentos_bloqueados = valor

    # Movimento do pokemon que será bloqueado:
    def adicionar_movimento_bloqueado(self, movimento_id, por_quantos_turnos):
        # Precisamos somente da id do movimento (índice 0):
        self.movimentos_bloqueados.append([movimento_id, por_quantos_turnos])

    def __passou_um_turno(self):

        # Restaura a precisão (chance de não vacilar):
        self.__precisao_temp = 100
        # Diminui por 1 estágio o tempo bloqueado
        self.__bloqueado -= 1
        # Começa do primeiro:
        i = 0
        while i < len(self.movimentos_bloqueados):
            # Diminui o tempo que o movimento está bloqueado:
            self.movimentos_bloqueados[i][1] -= 1
            # Se a quantidade de turnos chegarem a zero, então o movimento não é mais bloqueado,
            # assim, temos que tirar ele da lista dos bloqueados:
            if self.movimentos_bloqueados[i][1] <= 0:
                self.movimentos_bloqueados.pop(i)
                # Como removeu o item, a lista diminuiu de tamanho,
                # então temos que diminuir o i por 1:
                i -= 1
            # Próximo:
            i += 1

    @property
    def precisao_numero(self):
        # Retorna a precisão em número para ser multiplicado
        # Obtém o estágio:
        e = self.precisao
        if e <= -6:
            return 33/100
        elif e == -5:
            return 36/100
        elif e == -4:
            return 43/100
        elif e == -3:
            return 50/100
        elif e == -2:
            return 60/100
        elif e == -1:
            return 75/100
        elif e == 1:
            return 133/100
        elif e == 2:
            return 166/100
        elif e == 3:
            return 200/100
        elif e == 4:
            return 250/100
        elif e == 5:
            return 266/100
        elif e == 6:
            return 300/100
        else:  # estágio 0:
            return 100/100

    # Getters e setters:
    @property
    def precisao_temp(self):
        return self.__precisao_temp

    @precisao_temp.setter
    def precisao_temp(self, precisao_temp):
        self.__precisao_temp = precisao_temp

    @property
    def ataque_critico(self):
        return self.__ataque_critico

    @ataque_critico.setter
    def ataque_critico(self, ataque_critico):
        # Não existe ataque crítico negativo:
        if ataque_critico < 0:
            ataque_critico = 0
        self.__ataque_critico = ataque_critico

    @property
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, itens):
        self.__itens = itens

    @property
    def precisao(self):
        return self.__precisao

    @precisao.setter
    def precisao(self, valor):
        self.__precisao = valor

    @property
    def vida_anim(self):
        # Retorna a vida animada (tamanho atual da animação):
        # Mas antes verificar se a animação não está negativa ou passou do tamanho
        # limite do máximo da vida:
        self.checar_e_corrigir_vida_anim()
        return self.__vida_anim

    # Correção de vida:
    def checar_e_corrigir_vida_anim(self):
        # Verifica se a vida animada é maior que a vida máxima:
        if self.__vida_anim > self.__vida_maxima:
            # E se essa verificação for efetivada,
            # a vida animada recebe o valor da vida máxima:
            self.__vida_anim = self.__vida_maxima
        # Verifica se a vida animada é menor que zero:
        elif self.__vida_anim < 0:
            # Sendo a afirmação efetivada, a vida animada reseta:
            self.__vida_anim = 0

    @vida_anim.setter
    def vida_anim(self, value):
        # Coloca o valor da animação de vida:
        self.__vida_anim = value
        # E corrige se necessário:
        self.checar_e_corrigir_vida_anim()

    @property
    def protegido(self):
        return self.__protegido

    @protegido.setter
    def protegido(self, value):
        self.__protegido = value

    # Verifica se o pokemon está protegido:
    def esta_protegido(self):
        return True if self.__protegido > 0 else False

    # Atualiza a vida:
    def atualiza_vida_anim(self, delta):
        valor = vel_anim * delta
        # Verifica se a animação da vida está perto da vida atual:
        if self.__vida - valor / 2 < self.__vida_anim < self.__vida + valor / 2:
            # Se está perto, então já pode terminar a animação:
            self.vida_anim = self.vida
        # Se não, então se for menor, aumenta a barra de vida:
        elif self.__vida_anim < self.__vida:
            self.vida_anim += valor
        # Caso contrário, diminui:
        elif self.__vida_anim > self.__vida:
            self.vida_anim -= valor

            # Verifica se o pokemon está bloqueado:

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
        esta_bloqueado = True if self.__bloqueado > 0 else False
        return esta_bloqueado

    @bloqueado.setter
    def bloqueado(self, value):
        self.__bloqueado = value

    # Pokemon perdeu:
    def foi_derrotado(self):
        # Retorna True se este pokémon não estiver vivo (sua vida está abaixo ou igual a 0):
        return True if self.__vida <= 0 else False

    # Pokemon fugiu:
    def conseguiu_fugir(self):
        # Retorna False se este pokémon fugiu com sucesso:
        return self.__fugiu

    # Processa os efeitos
    def process_effects(self, priority, enemy_pokemon):
        # Priority True: antes do movimento
        # False: depois do movimento
        if priority is True:
            self.__protegido -= 1
        else:
            self.__passou_um_turno()

        lista_mensagens = []

        # Iniciará pelo primeiro efeito:
        i = 0
        # Processa efeito por efeito até o último:
        while i < len(self.__pokemon_effects):
            # Obtenha um efeito da lista de efeitos do pokémon atual:
            effect_pokemon = self.__pokemon_effects[i]
            # Agora é necessário verificar o efeito para o pokémon
            # se é igual a corrente de prioridade (True: antes dos turnos; False: depois
            # dos turnos.):
            if self.__pokemon_effects[i]["priority"] is priority:
                if effect_pokemon["offset"] >= 0:
                    # Chamar a função que processa o efeito:
                    self.__process_one_effect(effect_pokemon, enemy_pokemon, lista_mensagens)
                    # Verifica se o "offset" chegou no "stops", e se o stops é igual a None, então o efeito ficará
                    # no pokémon para "sempre":
                    if effect_pokemon["stops"] is not None and effect_pokemon["offset"] > effect_pokemon["stops"]:
                        self.__pokemon_effects.pop(i)
                        # tem que diminuir o "i", se não vai pular o próximo efeito, pois removeu um item
                        # da lista:
                        i -= 1
                # Aumenta o offset, como se tivesse passado um turno:
                effect_pokemon["offset"] += 1
            # Próximo efeito:
            i += 1
        # Retornar as mensagens que deve aparecer:
        return lista_mensagens

    def __process_one_effect(self, pokemon_effects, enemy_pokemon, lista_mensagens):
        # Obtém da lista todos os efeitos que existem no código "effect.py":
        effects = self.effects
        # Agora,verifica se o efeito real é igual a um efeito, se sim, faça um
        # coisa específica:

        # Código que processa o efeito, como no processar_movimentos
        # Self: seu pokemon
        # Enemy_pokemon: pokemon inimigo
        if pokemon_effects["id"] == effects.leech_seed["id"]:  # Leech Seed
            # A mensagem que aparecerá quando aplicar o efeito:
            mensagem = "O HP de {} foi sugado".format(self.nome, enemy_pokemon.nome)
            # Colocar a mensagem na lista de mensagens:
            lista_mensagens.append(mensagem)
            # Código do efeito em si:
            vida_perdida = 12.5 * self.vida_maxima / 100
            self.vida -= vida_perdida
            enemy_pokemon.vida += vida_perdida
        elif pokemon_effects["id"] == effects.wrap["id"]:  # Wrap:
            # Esse efeito faz perder 1/8 da vida do seu pokémon:
            self.vida_maxima -= self.vida_maxima / 8
            # Mensagem:
            mensagem = "HP máximo de {} foi reduzido".format(self.nome)
            # Adicionando na lista:
            lista_mensagens.append(mensagem)
        elif pokemon_effects["id"] == effects.curse["id"]:
            # Perde 1/4 de sua vida máxima:
            self.vida_maxima -= self.vida_maxima / 4
            # Mensagem:
            mensagem = "HP máximo de {} foi reduzido".format(self.nome)
            # Adicionando na lista:
            lista_mensagens.append(mensagem)

    # Ataque do adversário:
    def atacar(self, outro_pokemon, poder, precisao=100):
        rand_1 = random.randrange(0, 100)
        rand_2 = random.randrange(0, 100)
        if rand_1 <= self.precisao_temp and rand_2 <= precisao * self.precisao_numero:
            acertou = 1
        else:
            acertou = 0
        # Poder (teste):
        # 1: ataque normal:
        ataque_critico = 1
        # Chance de crítico:
        chance_critico = -1
        # Quanto maior o ataque crítico, maior a chance de dar ataque crítico:
        if self.ataque_critico == 0:
            chance_critico = random.randrange(0, 16)  # 1/16
        elif self.ataque_critico == 1:
            chance_critico = random.randrange(0, 8)  # 1/8
        elif self.ataque_critico == 2:
            chance_critico = random.randrange(0, 4)  # 1/4
        elif self.ataque_critico == 3:
            chance_critico = random.randrange(0, 3)  # 1/3
        elif self.ataque_critico >= 4:
            chance_critico = random.randrange(0, 2)  # 1/2
        # Se deu 0, então deu a chance:
        if chance_critico == 0:
            # O ataque_critico agora será aplicado pelo multiplicador critico:
            ataque_critico = (2 * self.__nivel + 5) / (self.__nivel + 5)

        # Modificador = alvos * tempo_meteorológico * Badge * ataque_critico * aleatório de 0.85 a 1.00 *
        # bônus de ataque do mesmo tipo * tipo * queimado * outro
        modificador = ataque_critico * (random.randrange(85, 100) / 100)
        # Fórmula de dano:
        formula = ((((
                             2 * self.__nivel) / 5 + 2) * poder * self.__ataque / outro_pokemon.defesa) /
                   50 + 2) * modificador * acertou * (2 if self.queimado else 1)
        # Diz que o resultado deve ser "truncado":
        formula = math.trunc(formula)
        # A vida do pokémon inimigo será diminuída pela fórmula:
        outro_pokemon.vida -= formula
        # Retorna o quanto de dano deu e o ataque foi crítico:
        return formula, True if chance_critico == 0 else False

    # Para o outro pokemon fugir:
    def fugir_de(self, outro_pokemon):
        # Aumenta por quantas vezes tentou fugir:
        self.__tentou_fugir += 1
        # Cálculo de tentativa de fuga:
        a = self.__velocidade
        b = outro_pokemon.velocidade
        c = self.__tentou_fugir
        f = ((a * 128 / b) + 30 * c) % 256

        if random.randrange(0, 255) < f:
            # Conseguiu fugir:
            self.__fugiu = True
            return True
        else:
            # Não conseguiu:
            return False

    # Permite que o pokémom recupere a vida:
    def cura(self, quantidade):
        self.__vida += quantidade

    # Getters:
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

    # Retorna a cópia dos dados do pokemon:
    def copy(self):
        # Ou seja, essa função retorna uma cópia desse pokémon:
        return Pokemon(self.__nome, self.__vida_maxima, self.__ataque, self.__defesa,
                       self.__velocidade, self.__especial_ataque, self.__especial_defesa, self.__nivel,
                       self.__chance_genero, self.__tipos, self.__conjunto_movimentos, self.itens.copy(),
                       self.__imagem_id, self.__is_easter_egg)

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        # Se vida for menor que 0, ela retornará 0,
        # caso contrário vida é igual a vida.
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

    # Setters:
    # Adiciona os efeitos:
    def add_effect(self, effect):

        place = True
        # Verifica se o efeito que está querendo adicionar não existe na lista de efeitos:
        for i in range(len(self.__pokemon_effects)):
            if effect["id"] == self.__pokemon_effects[i]["id"]:
                # Achamos o efeito que queremos adicionar na lista, então não vamos adicionar:
                place = False
                # E não precisamos continuar procurando por efeitos iguais, então:
                break

        # Se place == True, então não existe, assim podemos adicionar, mas se for place == False,
        # então existe, assim não precisamos adicionar efeito duplicado:
        if place:
            # Se o efeito não dura para "sempre":
            if not effect["stops"] is None:
                # Sortear por quantas rodadas durará o mesmo:
                effect["stops"] = random.choice(effect["stops"])
            # Adicionar o efeito para a lista de efeitos
            self.__pokemon_effects.append(effect)
        # Retorna se adicionou o efeito
        return place

    @sumindo.setter
    def sumindo(self, sumindo):
        # Define se está sumindo:
        self.__sumindo = sumindo
        # Reseta se está invisível:
        self.__sumido = sumindo

    @sumido.setter
    def sumido(self, valor):
        self.__sumido = valor

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @vida.setter
    def vida(self, vida):
        vida_a_colocar = int(vida)
        # A vida não pode ser negativa ou maior que a vida máxima:
        if vida_a_colocar < 0:
            vida_a_colocar = 0
        elif vida_a_colocar > self.__vida_maxima:
            vida_a_colocar = self.__vida_maxima

        self.__vida = vida_a_colocar

    @vida_maxima.setter
    def vida_maxima(self, valor):
        valor_anterior = self.__vida_maxima
        valor = int(valor)
        self.__vida_maxima = valor
        # Verifica se a vida é a maior que a vida máxima:
        # if self.__vida > self.__vida_maxima:
        #    # Se sim, a vida recebe o valor da vida máxima:
        #    self.__vida = self.__vida_maxima

        # Reduz a vida uniformemente e a animação também:
        # Evitar divisão por zero:
        if valor_anterior == 0:
            valor_anterior = 1
        self.__vida = int(self.__vida * valor / valor_anterior)
        self.__vida_anim = self.__vida

    @ataque.setter
    def ataque(self, ataque):
        if not self.__protegido:
            self.__ataque = ataque

    @defesa.setter
    def defesa(self, defesa):
        if not self.__protegido:
            self.__defesa = defesa

    @velocidade.setter
    def velocidade(self, velocidade):
        if not self.__protegido:
            self.__velocidade = velocidade

    @especial_ataque.setter
    def especial_ataque(self, especial):
        if not self.__protegido:
            self.__especial_ataque = especial

    @especial_defesa.setter
    def especial_defesa(self, especial):
        if not self.__protegido:
            self.__especial_defesa = especial

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @imagem_costas.setter
    def imagem_costas(self, imagem_costa):
        self.__imagem_costas = imagem_costa

    @imagem_frente.setter
    def imagem_frente(self, imagem_frente):
        self.__imagem_frente = imagem_frente

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel
