# Atua em tudo que envolve tempo no jogo:
class Tempo:
    def __init__(self, milisegundos=0):
        # Milisegundos:
        self.__milisegundos = milisegundos
        # Etapas de cada turno (usado na função process_turns em main.py):
        self.__etapa_turno = 0
        # Tem por quanto tempo o pokémon está visível ou invisível:
        self.__sumido_tempo = 0
        # Conta o tempo que está na tela de fim de jogo:
        self.__fim_de_jogo_tempo = 0
        # Conta o tempo entre cada caractere na animação do texto que mostra o que está
        # acontecendo:
        self.__mensagem_tempo = 0

    # Getters:
    @property
    def mensagem_tempo(self):
        return self.__mensagem_tempo

    @property
    def fim_de_jogo_tempo(self):
        return self.__fim_de_jogo_tempo

    @property
    def milisegundos(self):
        return self.__milisegundos

    @property
    def etapa_turno(self):
        return self.__etapa_turno

    @property
    def sumido_tempo(self):
        return self.__sumido_tempo

    # Setters:
    @fim_de_jogo_tempo.setter
    def fim_de_jogo_tempo(self, valor):
        self.__fim_de_jogo_tempo = valor

    @sumido_tempo.setter
    def sumido_tempo(self, sumido_tempo):
        self.__sumido_tempo = sumido_tempo

    @milisegundos.setter
    def milisegundos(self, milisegundos):
        self.__milisegundos = milisegundos

    @mensagem_tempo.setter
    def mensagem_tempo(self, valor):
        self.__mensagem_tempo = valor

    # Acrescenta mais uma etapa no turno:
    def etapa_turno_incrementa(self):
        self.__etapa_turno += 1

    # Reseta o turno:
    def etapa_turno_reseta(self):
        self.__etapa_turno = 0

    # Soma milisegundos com o valor (delta):
    def adicionar(self, valor):
        self.__milisegundos += valor

    # Reseta os milisegundos para 0:
    def resetar(self, delta):
        self.__milisegundos = - delta
