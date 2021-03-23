def compare_effects(effect1, effect2):
        return True if effect1[0] == effect2[0] else False

class Effect:

    

    @property
    def leech_seed(self):
        # id, offset, stops ,priority (True = before turns, False = atfer all turns)
        return [0, -1, None, True]