#Primera implementacion
class Punto:
    """Un punto en el espacio bi dimensional:
    - coordenada x
    - coordenada y
    """
    
    def __init__(self, x = 0 , y = 0): # si no paso x e y se considera que el punto es (0,0) 
        "Crea el objeto punto"
        self.x = x
        self.y = y

    def __eq__(self, otro)->bool:
        """Devolver True si self es igual a otro."""
        return (self.x == otro.x) and (self.y == otro.y)

    def es_origen(self)->bool:
        """Me dice si el punto corresponde al origen del plano (0,0)"""
        return self.x == 0 and self.y ==0
            
    def mover(self, dx:int, dy:int)->None: 
        """Mueve el punto dx lugares en x y dy lugares en y"""
        self.x = self.x + dx 
        self.y = self.y + dy
    
    def actualizar_xy(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def distancia(self,otro)->float:
        # calcula la distancia entre 2 puntos
        # pitagoras -> a**2 + b**2 = h**2
        return ((self.x-otro.x)**2 + (self.y-otro.y)**2) ** (1/2)

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return f"({self.x},{self.y})"

a = Punto(1,2)
print(a)
a.mover(5,3)
print(a)
print(a.es_origen())
b = Punto()
print(b.es_origen())
c = Punto(6,5)
print(c)

print (b==c) # Falso
print (a==c) # True

origen = Punto()
b.distancia(c)




#Segunda implementación
class Punto:
    """Un punto en el espacio bi dimensional: implementacion con un par
    - coordenada x
    - coordenada y
    """
    par = [0,0] # lista
    def __init__(self, x=0, y=0): # si no paso x e y se considera que el punto es (0,0) 
        self.par = [x,y]

    def __eq__(self, otro):
        """Devolver True si self es igual a otro."""
        return self.par == otro.par

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return f"({self.par[0]},{self.par[1]})"

    def es_origen(self):
        """Me dice si el punto corresponde al origen del plano"""
        return self.par == [0,0]

    def mover(self,dx,dy):
        """Mueve el punto dx lugares en x y dy lugares en y"""
        self.par = [self.par[0]+dx, self.par[1]+dy] 

    def distancia(self,otro):
        return ((self.par[0]-otro.par[0])**2 + (self.par[1]-otro.par[1])**2) ** (1/2)

a = Punto(1,2)
print(a)
a.mover(5,3)
print(a)
print(a.es_origen())
b = Punto()
print(b.es_origen())
c = Punto(6,5)
print(c)

print (b==c) # Falso
print (a==c) # True

origen = Punto()
b.distancia(c)

class Rectangulo():
    """ Esta clase modela un rectángulo en el plano. """

    def __init__(self, base, altura, origen = Punto()):
        """ base (número) es la longitud de su base,
            altura (número) es la longitud de su base,
            origen (Punto) es el punto del plano de su esquina
            inferior izquierda. """
        self.base = base
        self.altura = altura
        self.origen = origen

    def area(self)-> int:
        """Calcula el area de un rectangulo base*altura"""
        return self.base * self.altura

    def perimetro(self)->int:
        " calcula el perimetro de un rectangulo base *2 + altura*2"
        return (self.base * 2) + (self.altura * 2)

    def mover(self, dx = 0, dy = 0):
        """mueve el origen del rectangulo """
        self.origen.mover(dx,dy)

    def __str__(self):
        """ muestra los datos del rectángulo """
        return "rectangulo"
        return f"Base: {self.base}, Altura: {self.arltura}, Origen: {self.origen}"

    def __eq__(self,otro):
        """dice si dos rectangulos son iguales"""
        return (self.base == otro.base) and (self.altura == otro.altura)

c = Rectangulo (4,4)
print("----------------o-----------")
print (c)
print("Area",c.area())
print("Perímetro",c.perimetro())
c.mover(1,2)
print (c)
p1 =  Punto(2,3)
r = Rectangulo (3,8, p1) 
print(r)
print("Area",r.area()) 
print("Perímetro",r.perimetro())
print(c.__eq__(r))