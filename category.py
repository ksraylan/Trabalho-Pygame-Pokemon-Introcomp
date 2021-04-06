# Temos nesta classe 
class Category:
    def __dictionary(self, a_list):
        return {"id": a_list[0], "name": a_list[1]}
    @property
    def normal_move(self):
        return self.__dictionary([0,"Normal move"])
    @property
    def state_move(self):
        return self.__dictionary([1, "State move"])
    @property
    def item_move(self):
        return self.__dictionary([2, "Item move"]) 