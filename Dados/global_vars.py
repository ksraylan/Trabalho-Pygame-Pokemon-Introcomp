# Biblioteca de números aleatórios e outros:
import random


# Mostra o que acontece durante os ataques da batalha:
class Funcao:
    # Mostra o que ocorre caso ataque acertou o alvo:
    @staticmethod
    def mostrar_texto_ataque_normal(retornado, mensagem):
        # Mostra o que retornará:
        dano = retornado[0]
        foi_critico = retornado[1]
        print("dano:",dano)
        errou = True if dano == 0 else False  # Errou caso deu nenhum dano ("0")
        # Mensagem caso o pokemon tenha errado:
        if errou:
            mensagem.texto = "Errou o alvo"
        # Mensagem caso o pokemon tenha acertado:
        else:
            # Caso o ataque tenha sido crítico:
            if foi_critico:
                mensagem.texto = "Foi muito efetivo! Perdeu {} HP".format(dano)
            # Caso o ataque tenha sido normal:
            else:
                mensagem.texto = "Fez perder {} HP".format(dano)
        # Retorna quanto de dano deu:
        return dano

    # Mostra o que ocorre caso errou o ataque:
    @staticmethod
    def mostrar_mensagem_errou(mensagem):
        if not mensagem.texto == "Errou o alvo":
            mensagem.texto = "Errou"

    # Retorna se vai ser shiny:
    @staticmethod
    def shiny_aleatorio():
        return True if random.randrange(0, 16) == 0 else False  # 1/16 de probabilidade = 6.25%  


# Cria o objeto:
funcao = Funcao()
