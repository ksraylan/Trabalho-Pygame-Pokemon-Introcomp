class Condicao:
    def __init__(self, atual = 0):
        self.__atual = 0
    
    # faz aqui
    @property
    def atual(self):
        return self.__atual

    @atual.setter
    def atual(self,atual):
        self.__atual = atual
    
    @property
    def batalhando(self):
        return 0
    @property
    def vitoria(self):
        return 1
    @property
    def derrota(self):
        return 2