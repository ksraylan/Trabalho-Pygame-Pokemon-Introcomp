
class Funcao:
    def mostrar_texto_ataque_normal(self, dano, mensagem):
        errou = True if dano == 0 else False
        if errou:
            mensagem.texto = "Errou o alvo"
        else:
            mensagem.texto = "Fez perder {} HP".format(dano)
    def mostrar_mensagem_errou(self, mensagem):
        if not mensagem.texto == "Errou o alvo":
            mensagem.texto = "Errou"
funcao = Funcao()