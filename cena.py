# Cenas principais:
class Menu:
    def __init__(self):
        self.__atual = 0
        # Pokemon que esta sendo escolhido:
        self.__escolhendo_pokemon = 0
        # Pokemon que está batalhando:
        self.__batalhando = 1

    #Getters e setters:
    @property
    def escolhendo_pokemon(self):
        return self.__escolhendo_pokemon
    @property
    def batalhando(self):
        return self.__batalhando
    # Define o menu atual:
    @property
    def atual(self):
        return self.__atual
    
    @atual.setter
    def atual(self, valor):
        self.__atual = valor

    # Retorna True se está no menu passado pelo usuário, caso contrário False:
    def no_menu(self, outro_menu):
        return True if self.__atual == outro_menu else False

# Cenas secundárias:
class Submenu:
    def __init__(self):
        self.__atual = 0
        self.__principal = 0
        # O ataque que será escolhido:
        self.__escolhendo_ataque = 1
    
    # Getters e setters:
    @property
    def principal(self):
        return 0
    @property
    def escolhendo_ataque(self):
        return 1
    @property
    def fazendo_acoes(self):
        return 2
    @property
    def vitoria(self):
        return 3
    @property
    def derrota(self):
        return 4

    @property
    def atual(self):
        return self.__atual

    @property
    def texto(self):
        return 5
    @property
    def itens(self):
        return 6
    
    # Define o sub menu atual:
    @atual.setter
    def atual(self, valor):
        self.__atual = valor

    # Retorna True se está no sub menu passado pelo usuário, caso contrário False:
    def no_submenu(self, outro_menu):
        return True if self.__atual == outro_menu else False