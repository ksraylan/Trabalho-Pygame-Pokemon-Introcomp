# Mostra o que acontece durante os ataques da batalha:
class Funcao:
    # Mostra o que ocorre caso ataque acertou o alvo:
    def mostrar_texto_ataque_normal(self, retornado, mensagem):
        dano = retornado[0]
        foi_critico = retornado[1]
        errou = True if dano == 0 else False
        # Mensagem caso o pokemon tenha errado:
        if errou:
            mensagem.texto = "Errou o alvo"
        # Mensagem caso o pokemon tenha acertado:
        else:
            if foi_critico:
                mensagem.texto = "Foi muito efetivo! Perdeu {} HP".format(dano)
            else:
                mensagem.texto = "Fez perder {} HP".format(dano)
    # Mostra o que ocorre caso erre o ataque:
    def mostrar_mensagem_errou(self, mensagem):
        if not mensagem.texto == "Errou o alvo":
            mensagem.texto = "Errou"
funcao = Funcao()