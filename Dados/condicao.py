# Classe onde administra funções que precisam uma condição para que algo aconteça:
class Condicao:
    def __init__(self, atual=0):
        self.__atual = atual

    # O que está acontecendo atualmente na batalha/movimento:
    @property
    def atual(self):
        return self.__atual

    @atual.setter
    def atual(self, atual):
        self.__atual = atual

    # Confere o que está acontecendo no momento:
    @property
    def batalhando(self):
        return 0

    @property
    def vitoria(self):
        return 1

    @property
    def derrota(self):
        return 2
