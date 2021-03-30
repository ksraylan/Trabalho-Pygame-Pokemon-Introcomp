class Mensagem:
    def __init__(self, texto=""):
        self.__texto = texto
        self.__texto_posicao = 0
    
    @property
    def texto_posicao(self):
        return self.__texto_posicao
    
    def texto_deslocar_uma_posicao(self):
        self.__texto_posicao += 1
    def texto_resetar_posicao(self):
        self.__texto_posicao = 0

    @property
    def texto(self):
        return self.__texto + "!"
    
    @texto.setter
    def texto(self, valor):
        self.__texto = valor
        self.texto_resetar_posicao()