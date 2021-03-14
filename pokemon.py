#características do pokémon:
class Pokemon:
    def __init__(self, nome, vida, força, imagem_costas, imagem_frente):
        self.__nome = nome
        self.__vida = vida
        self.__força = força
        self.__imagem_costas = imagem_costas
        self.__imagem_frente = imagem_frente
    
    
    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @property
    def força(self):
        return self.__força


    @property
    def imagem_costas(self):
        return self.__imagem_costas

    @property
    def imagem_frente(self):
        return self.__imagem_frente

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @vida.setter
    def vida(self,vida):
        self.__vida = vida
        
    @força.setter
    def força(self,força):
        self.__força = força

    @imagem_costas.setter
    def imagem_costas(self,imagem_costa):
        self.__imagem_costas = imagem_costa

    @imagem_frente.setter
    def imagem_frente(self,imagem_frente):
        self.__imagem_frente = imagem_frente

    def batalha(self,ataque,outro_pokemon):
        outro_pokemon.vida -= ataque
        pass
