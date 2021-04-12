class EasterEgg:
    def __init__(self):
        # Código para ativar o EasterEgg:
        self.codigo = "introcomp"
        # Últimos caracteres que o usuário digitou no teclado:
        self.__ultimos = ["", "", "", "", "", "", "", "", ""]
    
    def processa_caractere(self, caractere):
        # Tira o último caractere:
        self.__ultimos.pop(0)
        # Adiciona o novo:
        self.__ultimos.append(caractere)
        return self.__verificar_se_foi_ativado()

    def __verificar_se_foi_ativado(self):
        # Converte a lista de caracteres em string:
        em_texto = ""
        # Percorre cada caractere:
        for c in self.__ultimos:
            em_texto += c
        # Verifica se é igual ao código:
        if em_texto == self.codigo:
            return True
        else:
            return False
