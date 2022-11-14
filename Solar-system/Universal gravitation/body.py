import numpy as np
class Body:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 120 / AU  # 1AU = 100 pixels
    TIMESTEP = 360*24
    def __init__(self, mass, size, r, v, object_name, colour=None, sun=False):
        self.__mass = mass
        self.__size = size
        self.__r = r
        self.__v = v
        self.__a = np.array([0, 0], dtype=float)
        self.colour = colour
        self.sun = sun
        self.object_name = object_name

    def draw(self, canvas, root):
        canvas.delete(self.object_name)
        canvas.create_oval(self.pos[0]*self.SCALE + 700-(self.size/2),self.pos[1]*self.SCALE + 350 -(self.size/2),self.pos[0]*self.SCALE + 700+(self.size/2),self.pos[1]*self.SCALE + 350+(self.size/2), outline = self.colour, fill = self.colour, tags=self.object_name)
        root.update()
	
    
    def attraction(self, other):
        distance_vec = other.pos - self.pos
        distance = np.linalg.norm(distance_vec)

        force = self.G * self.mass * other.mass / distance**2
        theta = np.arctan2(distance_vec[1], distance_vec[0])
        force_x = np.cos(theta) * force
        force_y = np.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.vel += [total_fx / self.mass * self.TIMESTEP, total_fy / self.mass * self.TIMESTEP]

        self.pos += self.vel*self.TIMESTEP

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