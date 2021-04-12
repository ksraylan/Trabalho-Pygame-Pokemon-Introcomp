# Define as posições:
class Pos:
    def __init__(self, width, height, i_limit=-1):
        # Largura, altura e limite:
        self.__width = width
        self.__height = height
        # Limite da seta:
        self.i_limit = i_limit
        # Posição x e y que a seta começa:
        self.__x = 0
        self.__y = 0
        self.__i = 0
        # Calcula qual item está selecionado:
        self.i_calc()
        # Deslocamento da "página":
        self.__offset = 0

    # Getter e setter:
    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    # Atualização dos valores de x e y: 
    def i_calc(self):
        current_x = 0
        current_y = 0
        i = 0
        # O que isso faz é calcular em que parte da "grade" o item está:
        while current_x != self.__x or current_y != self.__y:
            i += 1
            current_x += 1
            if current_x >= self.__width:
                current_x = 0
                current_y += 1
            if i > 1000:  # Caso entre em loop infinito:
                break

        if i > self.__i_limit:  # Se passou do limite:
            # Volta para dentro do limite:
            i = self.__i_limit
        # Por úlimo, define o item selecionado:
        self.__i = i

    # Getter e setter:
    @property
    def i_limit(self):
        return self.__i_limit

    @i_limit.setter
    def i_limit(self, value):
        # Confere se o valor não é menor que 0
        # se não for limite de i é igual ao valor:
        if not value < 0:
            self.__i_limit = value
        else:
            # Calcula o limite de i:
            self.__i_limit = self.width * self.height - 1

    # Getters e setters:    
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def i(self):
        return self.__i

    @width.setter
    def width(self, width):
        self.__width = width
        # Limite de i é igual a altura * largura.
        self.i_limit = self.__width * self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        # Limite de i é igual a altura * largura.
        self.i_limit = self.__width * self.__height

    @x.setter
    def x(self, x):
        # O x recebe ele mesmo só que corrigido:
        self.__x = self.fix_x(x)
        # Calcula qual item está selecionado:
        self.i_calc()

    def fix_x(self, x):  # Corrige o x se ele passar do limite em que a seta pode se locomover:
        if x < 0:
            x = self.__width - 1
        if x >= self.__width:
            x = 0
        return x

    def fix_y(self, y):  # Corrige o y que nem o x:
        if y < 0:
            y = self.__height - 1
        elif y >= self.__height:
            y = 0
        return y

    @y.setter
    def y(self, y):
        # O y recebe ele mesmo só que corrigido:
        self.__y = self.fix_y(y)
        # Calcula qual item está selecionado:
        self.i_calc()

    @i.setter
    def i(self, i):
        # Define a posição do item:
        self.__i = i
        self.__y = (i // self.width)
        self.__x = i - (i * self.width)
