# Determina os itens que são usados pelo pokémon:
class Itens:

    # Itens que se usam na batalha:
    @property
    def dire_hit(self):
        # Aumenta a proporção de acertos críticos de Pokémon em batalha. Esmaece se o Pokémon for retirado.
        return [0, "Dire Hit"]

    @property
    def guard_spec(self):
        # O item que impede a redução de estatísticas entre os Pokémon do grupo por cinco turnos após o uso.
        return [1, "Guard Spec"]

    @property
    def x_accuracy(self):
        # Aumenta a estatística de precisão do Pokémon em batalha. Esmaece se o Pokémon for retirado.
        return [2, "X Accuracy"]

    @property
    def x_attack(self):
        # Aumenta a estatística "ATTACK" do Pokémon na batalha. Esmaece se o Pokémon for retirado.
        return [3, "X Attack"]

    @property
    def x_defense(self):
        # Aumenta a estatística "DEFENSE" do Pokémon em batalha. Esmaece se o Pokémon for retirado.
        return [4, "X Defense"]

    @property
    def x_special(self):
        # Eleva o SP. Estatística "ATK" de Pokémon em batalha. Esmaece se o Pokémon for retirado.
        return [5, "X Special"]

    @property
    def x_speed(self):
        # Aumenta a estatística do "SPEED" do Pokémon em batalha. Esmaece se o Pokémon for retirado.
        return [6, "X Speed"]

    @property
    def berry_juice(self):
        # Ele restaura o HP de um Pokémon em 20 pontos.
        return [-1, "Berry Juice"]

    @property
    def elixir(self):
        # Restaura o PP de todos os movimentos de um Pokémon em 10 pontos cada.
        return [-2, "Elixir"]

    @property
    def potion(self):
        # Ele restaura o HP de um Pokémon em 20 pontos.
        return [-3, "Potion"]
