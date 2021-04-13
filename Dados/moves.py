# Importação:
from Dados.poke_types import Types

# Objeto que contém os tipos dos movimentos:
tipos = Types()


# Classe que descreve os movimentos que o pokémon realiza e suas características:
class Moves:
    def __init__(self):
        pass

    # Getters que é retornado o id, nome, pp atual, pp maximo, prioridade, força,
    # chance_de_acertar e tipo (nessa ordem):
    @property
    def fugir(self):
        return 0, "Fugir", 0, 0, 3, 0, 0, tipos.normal

    # Padrão quando aba o pp de todos os movimentos:
    @property
    def struggle(self):
        return 1, "Struggle", 1, None, 100, 50, 0, tipos.normal

    @property
    def tackle(self):
        return -1, "Tackle", 35, 35, 0, 35, 100, tipos.normal

    @property
    def growl(self):
        return -2, "Growl", 40, 40, 0, -6, 100, tipos.normal

    @property
    def leech_seed(self):
        return -3, "Leech Seed", 10, 10, 0, 0, 90, tipos.grass

    @property
    def vine_whip(self):
        return -4, "Vine Whip", 25, 25, 0, 45, 100, tipos.grass

    @property
    def poison_powder(self):
        return -5, "Poison Powder", 35, 35, 0, 0, 75, tipos.poison

    @property
    def sleep_powder(self):
        return -6, "Sleep Powder", 15, 15, 0, 0, 75, tipos.grass

    @property
    def thunder_shock(self):
        return -12, "Thunder Shock", 30, 30, 0, 40, 100, tipos.electric

    @property
    def tail_whip(self):
        return -13, "Tail Whip", 30, 30, 0, -6, 100, tipos.normal

    @property
    def thunder_wave(self):
        return -21, "Thunder Wave", 20, 20, 0, 0, 100, tipos.electric

    @property
    def scratch(self):
        return -22, "Scratch", 35, 35, 0, 40, 100, tipos.normal

    @property
    def ember(self):
        return -23, "Ember", 25, 25, 0, 40, 100, tipos.fire

    @property
    def withdraw(self):
        return -31, "Withdraw", 40, 40, 0, 6, 100, tipos.water

    @property
    def bubble(self):
        return -38, "Bubble", 30, 30, 0, 20, 100, tipos.water

    @property
    def fury_attack(self):
        return -40, "Fury Attack", 20, 20, 0, 15, 85, tipos.normal

    @property
    def horn_attack(self):
        return -41, "Horn Attack", 25, 25, 0, 65, 100, tipos.normal

    @property
    def stomp(self):
        return -42, "Stomp", 20, 20, 0, 65, 100, tipos.normal

    @property
    def horn_drill(self):
        return -43, "Horn Drill", 5, 5, 0, 0, 30, tipos.normal

    @property
    def curse(self):
        return -47, "Curse", 10, 10, 0, 0, 100, tipos.ghost

    @property
    def hypnosis(self):
        return -52, "Hypnosis", 20, 20, 0, 0, 60, tipos.psychic

    @property
    def lick(self):
        return -53, "Lick", 30, 30, 0, 30, 100, tipos.ghost

    @property
    def spite(self):
        return -54, "Spite", 10, 10, 0, 0, 100, tipos.ghost

    @property
    def leer(self):
        return -58, "Leer", 30, 30, 0, 0, 100, tipos.normal

    @property
    def twister(self):
        return -59, "Twister", 20, 20, 0, 40, 100, tipos.dragon

    @property
    def wrap(self):
        return -60, "Wrap", 20, 20, 0, 15, 90, tipos.normal

    @property
    def confusion(self):
        return -66, "Confusion", 25, 25, 0, 50, 100, tipos.psychic

    @property
    def disable(self):
        return -67, "Disable", 20, 20, 0, 0, 100, tipos.normal

    @property
    def barrier(self):
        return -68, "Barrier", 20, 20, 0, 0, 100, tipos.psychic

    @property
    def mist(self):
        return -69, "Mist", 30, 30, 0, 0, 100, tipos.ice

    @property
    def psychic(self):
        return -72, "Psychic", 10, 10, 0, 90, 100, tipos.psychic

    @property
    def metal_claw(self):
        return -76, "Metal Claw", 35, 35, 0, 50, 95, tipos.steel
