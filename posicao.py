# Define as posições:
class Pos:
    def __init__(self, width, height, i_limit = -1):
        self.__width = width
        self.__height = height
        self.i_limit = i_limit
        # posição x e y que a seta começa:
        self.__x = 0
        self.__y = 0
        self.i_calc(False)
        self.__offset = 0

    # Getter e setter:
    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    # Atualização dos valores de x e y: 
    def i_calc(self, recalcular_x_e_y):
        current_x = 0
        current_y = 0
        i = 0
        # loop infinito:
        while current_x != self.__x or current_y != self.__y:
            i += 1
            current_x += 1
            if current_x >= self.__width:
                current_x = 0
                current_y += 1
            if i > 1000:
                break
            

        if i > self.__i_limit:
            i = self.__i_limit
        #if recalcular_x_e_y:
        #    self.i = i
        #else:
        self.__i = i

    # Getter e setter:
    @property
    def i_limit(self):
        return self.__i_limit

    @i_limit.setter
    def i_limit(self, value):
        if not value < 0:
            self.__i_limit = value
        else:
            #calcular o limite de i:
            self.__i_limit = self.width * self.height - 1

    # getters e setters:    
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
        self.i_limit = self.__width * self.__height
        
    
    @height.setter
    def height(self, height):
        self.__height = height
        self.i_limit = self.__width * self.__height
    
    @x.setter
    def x(self, x):
        self.__x = self.fix_x(x)
        self.i_calc(True)

    def fix_x(self, x):
        if x < 0:
            x = self.__width - 1
        if x >= self.__width:
            x = 0
        return x
    
    def fix_y(self, y):
        if y < 0:
            y = self.__height - 1
        elif y >= self.__height:
            y = 0
        return y

    @y.setter
    def y(self, y):
        self.__y = self.fix_y(y)
        self.i_calc(True)
    
    @i.setter
    def i(self, i):
        self.__i = i
        self.__y = (i//self.width)
        self.__x = i - (i * self.width)


