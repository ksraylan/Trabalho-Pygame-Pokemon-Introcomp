# Os efeitos serão comparados:
def compare_effects(effect1, effect2, priority):
        return True if effect1["id"] == effect2["id"] and effect1["priority"] == priority else False

class Effect:
    @property
    def leech_seed(self):
        # {id, quantos turnos precisa passar antes do efeito começar a funcionar,
        # para_depois de quantos turnos, prioridade (True = antes do seu movimento, False = depois do seu movimento)}
        # sem dicionarios seria: return [0, -1, None, True]
        # usar dicionários é melhor:
        return {"id": 0,
                "offset": 0, # logo quando pegar o efeito começará a funcionar
                "stops": None, # None: dura para "sempre"
                "priority": True}
    @property
    def wrap(self):
        return {"id": 1,
                "offset": -1, # quantos turnos precisa passar antes de começar (NOTA: precisa ser negativo)
                "stops": [2, 3, 4, 5], # de 2 a 5 turnos (todas as possibilidades)
                "priority": False} # depois do movimento dele
