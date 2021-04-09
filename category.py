
class Category:
    # Transforma a lista em um dicionario:
    def __dictionary(self, a_list):
        return {"id": a_list[0], "name": a_list[1]}
    # Movimento normal:
    @property
    def normal_move(self):
        return self.__dictionary([0,"Normal move"])
    # Movimento de estado:
    @property
    def state_move(self):
        return self.__dictionary([1, "State move"])
    # Movimento ao usar item:
    @property
    def item_move(self):
        return self.__dictionary([2, "Item move"]) 