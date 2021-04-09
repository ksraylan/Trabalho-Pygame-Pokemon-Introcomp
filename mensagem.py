#Posições dos textos:
class Mensagem:
    def __init__(self, texto=""):
        # O que será escrito no texto:
        self.__texto = texto
        # A posição que o texto estará:
        self.__texto_posicao = 0

    #Getters e setters:
    @property
    def texto_posicao(self):
        return self.__texto_posicao
    
    # Deslocamento do texto:
    def texto_deslocar_uma_posicao(self):
        self.__texto_posicao += 1
    # Reseta o deslocamento do texto (animação de escrever na tela)
    def texto_resetar_posicao(self):
        self.__texto_posicao = 0

    @property
    def texto(self):
        # Adiciona "!" no final da frase se não tiver "?":
        return self.__texto if self.__texto[-1] == "?" else self.__texto + "!"
    
    @texto.setter
    def texto(self, valor):
        # Faz com que a posição do texto seja resetado:
        self.__texto = valor
        self.texto_resetar_posicao()