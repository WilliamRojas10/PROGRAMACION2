<<<<<<< HEAD
#1 b 
class RegistroAlumnoMateria:
    def __init__ (self, nombre, materia): # Agregar parámetros
        """funcion que inicializa una variable registroAlumnoMateria"""
        self.nombre = nombre
        self.materia = materia
        self.notas = []
        self.promedio = self.calcular_promedio()
           
    def __str__(self)-> str:
        condicion = f"{self.nombre}, {self.materia}, {self.mostrar_estado()}"
        return condicion
    
    def agregar_nota(self, nota)-> None:
        if nota >= 0 and nota <= 10:
           self.notas.append(nota)
        
    def mostrar_notas(self)-> str:
        infoNotas = f"Notas: {self.notas}"
        return infoNotas 
    
    def calcular_promedio(self)->float:
        sumador = 0
        contador = 0
        promedio= 0
        for nota in self.notas:
            sumador += nota 
            contador += 1
        if sumador >= 0 and contador > 0:
            promedio = sumador / contador
        return promedio
    
    def mostrar_estado(self)->str: 
        self.promedio = self.calcular_promedio() #Le asignamos el nuevo valor del metodo 
        estado = ""
        if self.promedio >= 7 and self.promedio <= 10:
            estado = "promocionado"
        if self.promedio >= 4 and self.promedio < 7:
            estado = "regular"
        if self.promedio < 4:
            estado = "libre"
        return estado

        """calcula si esta regular, promocionado, o libre
        si saca menos de 4 de promedio , queda libre
        Promocion promedio de 7 y todas las notas 6 o mas.
        Sino Regular
        """
#Test
alumno1 = RegistroAlumnoMateria ("Juan", "Matemáticas") #Inicializacion de objeto 
alumno1.agregar_nota(10)
assert alumno1.mostrar_estado() == "promocionado"
assert alumno1.__str__() == "Juan, Matemáticas, promocionado"




#2
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
        pass

    def es_origen(self)->bool:
        """Me dice si el punto corresponde al origen del plano (0,0)"""
        return self.x == 0 and self.y ==0
            
    def mover(self,dx:int,dy:int)->None: 
        """Mueve el punto dx lugares en x y dy lugares en y"""
        # (1,2) moverlo 2 a la dercha (dx = 2) y uno arriba (dy = 1) -> (1+2,2+1)
        # (1,2) moverlo 2 a la izquierda (dx = -2) y uno abajo (dy = -1) -> (1-2,2-1)
        

    def distancia(self,otro)->float:
        # calcula la distancia entre 2 puntos
        # pitagoras -> a**2 + b**2 = h**2
        pass
    def __str__(self):
        """Devolver un string con la representación del punto."""
        return f"({self.x},{self.y})"

punto_1 = Punto()
print (punto_1)
print (punto_1.es_origen()) # True
punto_2 = Punto(2,-8)
print (punto_2)


print (punto_2.es_origen()) # False

a = Punto (-3,2) # mover(2,3) -> (-1 , 5)





#3
class Circulo:
    def __init__( self, puntoA:float = 0, puntoB:float = 0 ): # toma un radio , centro
        self.a = puntoA
        self.b = puntoB
        self.radio = abs(self.a - self.b)
        self.PI = 3.1415

    def diametro ( self )-> float:
        diametro = self.radio * 2
        return diametro
    def perimetro_circulo ( self )-> float:
        perimetro =  self.diametro() * self.PI
        return perimetro
    def area_circulo ( self )-> float:
        area = self.radio ** 2 * self.PI
        return area
    
    def __eq__(self,otro):#?
        pass
    def mover(self):#?
        pass

#Test
c = Circulo(5,20)
assert c.diametro() == 30
assert c.area_circulo() == 706.8375000000001
assert c.perimetro_circulo() == 94.245
#print(c.radio)





#4
class Fraccion:
    def __init__(self,arriba:int,abajo:int)->object:
        """inicializa una variable del tipo fraccion"""
        self.num = arriba # Numerador
        self.den = abajo # Denominador
        self.resultado = self.num / self.den

    def __str__(self)->str:
        info = f"{(str(self.num))} / {str(self.den)} = {str(self.resultado)}"
        return info
        """Convertir el objeto en cadena para poder imprimirlo"""
        
        pass
    def __add__(self, num2, den2): #Agregue un parametro de la funcion orogonal porque una fraccion  toma 2 numeros
        """Sumar dos fracciones y retornar resultado, pueden tener distinto denominador"""
        fila1 = self.num + num2
        fila2 = self.den + den2
        resultado = fila1 / fila2
        return resultado

    def __eq__(self, otraFrac):
        """compara dos fracciones y dice si son equivalentes"""
        pass

q = Fraccion(2,4)
p = Fraccion(1,2)

#assert q == p
print(p)
print(q.__str__())





#5
class Cafetera:
        def __init__ (self, capacidadMaxima = 1000, cantidadActual = 0):
          assert type(capacidadMaxima) == int, f"Esto no es un entero es {type(capacidadMaxima)}"
          assert type(cantidadActual) == int, f"Esto no es un entero es {type(cantidadActual)}"
          assert capacidadMaxima >= 0 and cantidadActual >= 0, "Las cantidades tienen que ser superior o igual a 0"
          self.capacidadMaxima = capacidadMaxima #El usuario define su valor por medio del parametro del construtor
          self.cantidadActual = self.capacidadMaxima #A CantidadActual se le asigna el valor de capacidadMaxima
          self.cantidadActual = cantidadActual #El usuario define su valor
          if self.cantidadActual > capacidadMaxima: #CantidadActual NO puede ser mayor a capacidadMaxima
              self.cantidadActual = 1000

        def __str__(self) -> str:
            return f"Capacidad Maxima {self.capacidadMaxima} y Cantidad actual {self.cantidadActual}"
    
        def llenarCafetera(self)-> None:
            self.cantidadActual = self.capacidadMaxima
            
        def servirTaza(self, cantidadTaza)-> None:
            if self.cantidadActual >= cantidadTaza:
                self.cantidadActual = self.cantidadActual - cantidadTaza
            elif self.cantidadActual < cantidadTaza:
                 self.cantidadActual = 0
            
        def vaciarCafetera (self)-> None:
            self.cantidadActual = 0

        def agregarCafe(self, cantidadCafe)-> None:
            assert cantidadCafe > -1, f"Cantidad de cafe tiene que ser mayor o igual a 0"
            if cantidadCafe <= self.capacidadMaxima and cantidadCafe > -1:
               self.cantidadActual += cantidadCafe
            elif cantidadCafe > self.capacidadMaxima:
                 self.cantidadActual = self.capacidadMaxima
            
termo = Cafetera(1000, 900)
termo.servirTaza(40)
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 860"
termo.vaciarCafetera()
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 0"
termo.agregarCafe(50)
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 50"
termo.llenarCafetera()
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 1000"




         
          

=======
#1 b
class RegistroAlumnoMateria:
    def __init__ (self, nombre, materia): # Agregar parámetros
        """funcion que inicializa una variable registroAlumnoMateria"""
        self.nombre = nombre
        self.materia = materia
        self.notas = []
        self.promedio = self.calcular_promedio()
           
    def __str__(self)-> str:
        condicion = f"{self.nombre}, {self.materia}, {self.mostrar_estado()}"
        return condicion
    
    def agregar_nota(self, nota)-> None:
        if nota >= 0 and nota <= 10:
           self.notas.append(nota)
        
    def mostrar_notas(self)-> str:
        infoNotas = f"Notas: {self.notas}"
        return infoNotas 
    
    def calcular_promedio(self)->float:
        sumador = 0
        contador = 0
        promedio= 0
        for nota in self.notas:
            sumador += nota 
            contador += 1
        if sumador >= 0 and contador > 0:
            promedio = sumador / contador
        return promedio
    
    def mostrar_estado(self)->str: 
        self.promedio = self.calcular_promedio() #Le asignamos el nuevo valor del metodo 
        estado = ""
        if self.promedio >= 7 and self.promedio <= 10:
            estado = "promocionado"
        if self.promedio >= 4 and self.promedio < 7:
            estado = "regular"
        if self.promedio < 4:
            estado = "libre"
        return estado

        """calcula si esta regular, promocionado, o libre
        si saca menos de 4 de promedio , queda libre
        Promocion promedio de 7 y todas las notas 6 o mas.
        Sino Regular
        """
#Test
alumno1 = RegistroAlumnoMateria ("Juan", "Matemáticas") #Inicializacion de objeto 
alumno1.agregar_nota(10)
assert alumno1.mostrar_estado() == "promocionado"
assert alumno1.__str__() == "Juan, Matemáticas, promocionado"




#2 a
"""
class punto:
    def __init__(self,ejeX, ejey):
        self.x = ejeX
        self.y = ejey
    def origen(self)->float:
        return self.x == 0 and self.y == 0
    
    def distancia(self,otro)->float:
        # calcula la distancia entre 2 puntos
        # pitagoras -> a**2 + b**2 = h**2
        return ((self.x-otro.x)**2 + (self.y-otro.y)**2) ** (1/2)
"""
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

#2 b
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



#3
class Circulo:
    def __init__( self, puntoA:float = 0, puntoB:float = 0, origen = Punto()): # toma un radio , centro
        self.a = puntoA
        self.b = puntoB
        self.radio = abs(self.a - self.b)
        self.PI = 3.1415
        self.origen = origen

    def __str__(self)-> str:
        """ muestra los datos del ciculo """
        return f"Este circulo tine Radio:{self.radio}, Origen: {self.origen}"
    def diametro ( self )-> float:
        diametro = self.radio * 2
        return diametro
    def perimetro_circulo ( self )-> float:
        perimetro =  self.diametro() * self.PI
        return perimetro
    def area_circulo ( self )-> float:
        area = self.radio ** 2 * self.PI
        return area

    def __eq__(self,otroCir)-> bool:
        """dice si dos circulos son iguales"""
        return self.radio == otroCir.radio

    def mover(self, dx = 0, dy = 0)-> None:
        """mueve el origen del circulo """
        self.origen.mover(dx,dy)
#Test
c = Circulo(5,20)
d = Circulo(20,5)
assert c.__str__() == "Este circulo tine Radio:15, Origen: (0,0)"
assert c.diametro() == 30
assert c.area_circulo() == 706.8375000000001
assert c.perimetro_circulo() == 94.245
assert c.__eq__(d) == True
assert d.__str__() == "Este circulo tine Radio:15, Origen: (0,0)"




#4
class Fraccion:
    def __init__(self,arriba:int,abajo:int)->object:
        """inicializa una variable del tipo fraccion"""
        self.num = arriba # Numerador
        self.den = abajo # Denominador
        self.dividido = self.num / self.den #Resultado

    def __str__(self)->str:
        """Convertir el objeto en cadena para poder imprimirlo"""
        info = f"{(str(self.num))} / {str(self.den)} = {str(self.dividido)}"
        return info
        
    def __add__(self, otraFrac): 
        """Sumar dos fracciones y retornar resultado, pueden tener distinto denominador"""
        denominador = self.den * otraFrac.den
        ope1 = self.num * otraFrac.den
        ope2 = self.den * otraFrac.num
        resultado = f'{ope1 + ope2} / {denominador}'
        return resultado

    def __eq__(self, otraFrac):
        """compara dos fracciones y dice si son equivalentes"""
        equivalente = self.dividido == otraFrac.dividido
        return equivalente
    
#Test   
q = Fraccion(2,4)
p = Fraccion(1,2)
assert q.__str__() == "2 / 4 = 0.5"
assert q.__add__(p) == "8 / 8"
assert q.__eq__(p) == True
assert p.__str__() == "1 / 2 = 0.5"


#5
class Cafetera:
        def __init__ (self, capacidadMaxima = 1000, cantidadActual = 0):
          assert type(capacidadMaxima) == int, f"Esto no es un entero es {type(capacidadMaxima)}"
          assert type(cantidadActual) == int, f"Esto no es un entero es {type(cantidadActual)}"
          assert capacidadMaxima >= 0 and cantidadActual >= 0, "Las cantidades tienen que ser superior o igual a 0"
          self.capacidadMaxima = capacidadMaxima #El usuario define su valor por medio del parametro del construtor
          self.cantidadActual = self.capacidadMaxima #A CantidadActual se le asigna el valor de capacidadMaxima
          self.cantidadActual = cantidadActual #El usuario define su valor
          if self.cantidadActual > capacidadMaxima: #CantidadActual NO puede ser mayor a capacidadMaxima
              self.cantidadActual = 1000

        def __str__(self) -> str:
            return f"Capacidad Maxima {self.capacidadMaxima} y Cantidad actual {self.cantidadActual}"
    
        def llenarCafetera(self)-> None:
            self.cantidadActual = self.capacidadMaxima
            
        def servirTaza(self, cantidadTaza)-> None:
            if self.cantidadActual >= cantidadTaza:
                self.cantidadActual = self.cantidadActual - cantidadTaza
            elif self.cantidadActual < cantidadTaza:
                 self.cantidadActual = 0
            
        def vaciarCafetera (self)-> None:
            self.cantidadActual = 0

        def agregarCafe(self, cantidadCafe)-> None:
            assert cantidadCafe > -1, f"Cantidad de cafe tiene que ser mayor o igual a 0"
            if cantidadCafe <= self.capacidadMaxima and cantidadCafe > -1:
               self.cantidadActual += cantidadCafe
            elif cantidadCafe > self.capacidadMaxima:
                 self.cantidadActual = self.capacidadMaxima
            
termo = Cafetera(1000, 900)
termo.servirTaza(40)
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 860"
termo.vaciarCafetera()
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 0"
termo.agregarCafe(50)
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 50"
termo.llenarCafetera()
assert termo.__str__() == "Capacidad Maxima 1000 y Cantidad actual 1000"




         
          

>>>>>>> bd8f96c (Practico 2 casi terminado)
