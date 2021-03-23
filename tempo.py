class Tempo:
    def __init__(self, milisegundos = 0):
        self.__milisegundos = milisegundos
        self.__etapa_turno = 0
        self.__sumido_tempo = 0
        self.__fim_de_jogo_tempo = 0
        self.__mensagem_tempo = 0

    @property
    def mensagem_tempo(self):
        return self.__mensagem_tempo

    @mensagem_tempo.setter
    def mensagem_tempo(self, valor):
        self.__mensagem_tempo = valor

    @property
    def fim_de_jogo_tempo(self):
        return self.__fim_de_jogo_tempo

    @property
    def milisegundos(self):
        return self.__milisegundos

    @property
    def etapa_turno(self):
        return self.__etapa_turno
    
    def etapa_turno_incrementa(self):
        self.__etapa_turno += 1
    
    def etapa_turno_reseta(self):
        self.__etapa_turno = 0

    @property
    def sumido_tempo(self):
        return self.__sumido_tempo

    @fim_de_jogo_tempo.setter
    def fim_de_jogo_tempo(self, valor):
        self.__fim_de_jogo_tempo = valor

    @sumido_tempo.setter
    def sumido_tempo(self, sumido_tempo):
        self.__sumido_tempo = sumido_tempo

    @milisegundos.setter
    def milisegundos(self, milisegundos):
        self.__milisegundos = milisegundos

    # soma milisegundos com valor:
    def adicionar(self, valor):
        self.__milisegundos += valor
    
    # reseta milisegundos para 0:
    def resetar(self):
        self.__milisegundos = 0