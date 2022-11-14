class Body:
    def __init__(self, mass, size, r, v, a, object_name, colour=None, sun=False):
        self.__mass = mass
        self.__size = size
        self.__r = r
        self.__v = v
        self.__a = a
        self.colour = colour
        self.sun = sun
        self.object_name = object_name

    def draw(self, canvas, root):
        canvas.delete(self.object_name)
        canvas.create_oval(self.pos[0]-(self.size/2),self.pos[1]-(self.size/2),self.pos[0]+(self.size/2),self.pos[1]+(self.size/2), outline = self.colour, fill = self.colour, tags=self.object_name)
        root.update()
	
    
    def attraction(self, other):
        pass

    def update_position(self, planets):
        pass

    @property
    def mass(self):
        return self.__mass
    @mass.setter
    def mass(self, mass):
        self.__mass = mass

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size    
    
    @property
    def pos(self):
        return self.__r
    @pos.setter
    def pos(self, pos):
        self.__r = pos   

    @property
    def vel(self):
        return self.__v
    @vel.setter
    def vel(self, vel):
        self.__v = vel  

    @property
    def ace(self):
        return self.__a
    @ace.setter
    def ace(self, ace):
        self.__a = ace    