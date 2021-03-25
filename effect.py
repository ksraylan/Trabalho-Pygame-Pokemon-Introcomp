def compare_effects(effect1, effect2, priority):
        return True if effect1["id"] == effect2["id"] and effect1["priority"] == priority else False

class Effect:
    @property
    def leech_seed(self):
        # id, offset, stops ,priority (True = before turns, False = atfer all turns)
        #return [0, -1, None, True]
        # usar dicionários é melhor:
        return {"id": 0,
                "offset": -1,
                "stops": None,
                "priority": True}