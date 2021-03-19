class Tempo:
    def __init__(self, milisegundos):
        self.__milisegundos = milisegundos

    @property
    def milisegundos(self):
        return self.__milisegundos

    @milisegundos.setter
    def milisegundos(self, milisegundos):
        self.__milisegundos = milisegundos

    # soma milisegundos com valor:
    def adicionar(self, valor):
        self.__milisegundos += valor
    
    # reseta milisegundos para 0:
    def resetar(self):
        self.__milisegundos = 0