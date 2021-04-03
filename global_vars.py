
class Funcao:
    def mostrar_texto_ataque_normal(self, retornado, mensagem):
        dano = retornado[0]
        foi_critico = retornado[1]
        errou = True if dano == 0 else False
        if errou:
            mensagem.texto = "Errou o alvo"
        else:
            if foi_critico:
                mensagem.texto = "Foi muito efetivo! Perdeu {} HP".format(dano)
            else:
                mensagem.texto = "Fez perder {} HP".format(dano)
    def mostrar_mensagem_errou(self, mensagem):
        if not mensagem.texto == "Errou o alvo":
            mensagem.texto = "Errou"
funcao = Funcao()