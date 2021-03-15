class Mensagem:
    def __init__(self, texto=""):
        self.__texto = texto
    
    @property
    def texto(self):
        return self.__texto
    
    @texto.setter
    def texto(self, valor):
        self.__texto = valor