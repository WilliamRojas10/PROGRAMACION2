"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiante: William Rojas

Práctico 2: Tipos abstractos de datos
"""
"""
1.a*  Implementar una clase llamada AlumnoMateria con las partes Constructor, operaciones y condiciones.
Constructor: nombre, nota, materia
Operaciones: imprimir datos y mostrar_estado() {libre, regular, promocional}
Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""

class AlumnoMateria:
    def __init__(self, nombre, materia, nota): # Agregar parámetros
        """funcion que inicializa una variable AlumnoMateria
        tener en cuenta las condiciones del TAD (texto e int)
        """
        assert type(nombre) == str, "Esto no es un string"
        assert type(materia) == str, "Esto no es un string"
        assert type(nota) == int, f"Esto no es un entero es {type(nota)}"
        assert nota >= 0 and nota <= 10, "nota no esta entre 0 y 10"
        
        self.nombre = nombre
        self.nota = nota
        self.materia = materia
    def __str__(self)->str:
        return f"{self.nombre}, {self.materia}, {self.nota}"
    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre"""
        nota = self.nota
        if nota<4:
            estado = "libre"
        elif nota >= 4 and nota < 7:
            estado = "regular"
        else:
            estado = "promocionado"
        return estado

# Test
alumno1 = AlumnoMateria ("Juan", "Matemáticas", 4)
assert alumno1.__str__() == "Juan, Matemáticas, 4"
assert alumno1.mostrar_estado() == "regular"

"""
1.b Implementar la clase registroAlumnoMateria() que guarde varias notas y diga si el alumno está regular, promocional o libre. Con las siguientes reglas.
    Constructor: (Nombre, Materia)
    Agregar nota: Agrega una nota al alumno en la materia (lista de notas)
    Promedio: Devuelve el promedio de notas que tiene el alumno
    Mostrar notas: imprime la lsita de notas
    Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""
class RegistroAlumnoMateria:
    notas = []
    def __init__(self, nombre, materia): # Agregar parámetros
        """funcion que inicializa una variable registroAlumnoMateria"""
        pass
    def __str__(self):
        pass
    def agregar_nota(self):
        pass
    def mostrar_notas(self):
        pass
    def calcular_promedio(self)->float:
        pass
    def mostrar_estado(sef)->str: 
        """calcula si esta regular, promocionado, o libre
        si saca menos de 4 de promedio , queda libre
        Promocion promedio de 7 y todas las notas 6 o mas.
        Sino Regular
        """
        pass
<<<<<<< HEAD

=======
"""
>>>>>>> bd8f96c (Practico 2 casi terminado)
a = RegistroAlumnoMateria ("Nombre", "Materia")
a.agregar_nota(4)
a.agregar_nota(10)
assert alumno1.mostrar_estado() == "promocionado"
assert alumno1.__str__() == "Juan, Matemáticas, promocionado"
<<<<<<< HEAD

#SOLUCION
=======
"""

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

"""SOLUCION"""
>>>>>>> bd8f96c (Practico 2 casi terminado)
class RegistroAlumnoMateria:
    def __init__ (self, nombre, materia): # Agregar parámetros
        """funcion que inicializa una variable registroAlumnoMateria"""
        self.nombre = nombre
        self.materia = materia
        self.notas = []
        self.promedio = self.calcular_promedio()
           
    def __str__(self):
        condicion = f"{self.nombre}, {self.materia}, {self.mostrar_estado()}"
        return condicion
    
    def agregar_nota(self, nota):
        if nota >= 0 and nota <= 10:
           self.notas.append(nota)
        
    def mostrar_notas(self):
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

alumno1 = RegistroAlumnoMateria ("Juan", "Matemáticas") #Inicializacion de objeto 
alumno1.agregar_nota(10)
#Test
assert alumno1.mostrar_estado() == "promocionado"
assert alumno1.__str__() == "Juan, Matemáticas, promocionado"

"""
2.a* A la clase punto vista en la materia agregarle el método Distancia al origen ()siendo el origen el punto (0,0). Crear un programa que use este método para imprimir en pantalla la distancia entre al origen de los puntos A, B y C.
"""
<<<<<<< HEAD
=======
"""
>>>>>>> bd8f96c (Practico 2 casi terminado)
A = Punto(2,3)
B = Punto(5,5)
C = Punto(1,5)

A.distancia(B)
<<<<<<< HEAD
assert A.distancia_origen() == 3.605551275463989
assert B.distancia_origen() == 7.0710678118654755
assert C.distancia_origen() == 5.0990195135927845
=======
assert A.distancia == 3.605551275463989
assert B.distancia == 7.0710678118654755
assert C.distancia == 5.0990195135927845
"""

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

    def distancia_origen(self,otro):
        return ((self.par[0]-otro.par[0])**2 + (self.par[1]-otro.par[1])**2) ** (1/2)
>>>>>>> bd8f96c (Practico 2 casi terminado)

"""
2.b Utilizando el método de distancia al origen cree una función que tome una lista de puntos y devuelva el que se encuentra más alejado del origen.
def mas_lejos(lista:[Punto])->Punto
toma una lista de puntos y devuelve el mas alejado del origen
"""
<<<<<<< HEAD
assert mas_lejos([Punto(2,3) , Punto( 5,5 ), Punto(1,5)]) == Punto(5,5)
=======
#assert mas_lejos([Punto(2,3) , Punto( 5,5 ), Punto(1,5)]) == Punto(5,5)
>>>>>>> bd8f96c (Practico 2 casi terminado)

"""
3.* Crear una clase circulo: 
constructor: punto(x, y), radio; 
operaciones:diametro,  perimetro y area.
"""
#Tomar de ejemplo la clase rectangulo
class Circulo:
    def __init__( self ): # toma un radio , centro
        pass
    def diametro ( self ):
        pass
<<<<<<< HEAD
    def perimetro ( self ):
        pass 
    def area ( self ):
=======
    def perimetro_circulo ( self ):
        pass 
    def area_circulo ( self ):
>>>>>>> bd8f96c (Practico 2 casi terminado)
        pass
    def __eq__(self,otro):
        pass
    def mover(self):
        pass
<<<<<<< HEAD
=======
"""
>>>>>>> bd8f96c (Practico 2 casi terminado)
c = Circulo(0, 0, 4.5)
assert c.diametro() == 9.0
assert c.area_circulo() == 63.61725123519331
assert c.perimetro_circulo() == 28.274333882308138
<<<<<<< HEAD
=======
"""

"""Solucion"""
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
>>>>>>> bd8f96c (Practico 2 casi terminado)

"""
4. Definir el TAD Fracción junto con su implementación en Clases.
    En python tenemos el tipo de dato float, pero no fraccion (numeros racionales)
    Constructor: arriba, abajo
    Operaciones:
    mostrar: convertir el objeto en cadena para poder imprimirlo = ⅓.
    Sumar (o restar) fracciones: suma de dos fracciones (tener en cuenta el denominador común)
    Igualdad: ¿Cuando dos fracciones son equivalentes?

Escribir test para los métodos de la clase
"""
class Fraccion:
    def __init__(self,arriba,abajo):
        """inicializa una variable del tipo fraccion"""
        self.num = arriba # Numerador
        self.den = abajo # Denominador
    def __str__(self):
        """Convertir el objeto en cadena para poder imprimirlo"""
        
        pass
    def __add__(self, otraFrac):
        """Sumar dos fracciones y retornar resultado, pueden tener distinto denominador"""
        pass
    def __eq__(self, otraFrac):
        """compara dos fracciones y dice si son equivalentes"""
        pass
<<<<<<< HEAD

q = Fraccion(2,4)
p = Fraccion(1,2)

assert q == p
=======
"""
q = Fraccion(2,4)
p = Fraccion(1,2)
assert q == p
"""

"""Solucion"""
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
>>>>>>> bd8f96c (Practico 2 casi terminado)

"""
5.* Desarrolla una clase Cafetera con 
Atributos:
	+ _capacidadMaxima (la cantidad máxima de café que puede contener la cafetera) y 
	+ _cantidadActual (la cantidad actual de café que hay en la cafetera). 
Métodos:
	+ Constructor predeterminado: establece la capacidad máxima en 1000 (c.c.) y la actual en cero (cafetera vacía).
	+ Constructor con la capacidad máxima de la cafetera; inicializa la cantidad actual de café igual a la capacidad máxima.
	+ Constructor con la capacidad máxima y la cantidad actual. Si la cantidad actual es mayor que la capacidad máxima de la cafetera, la ajustará al máximo.
	+ llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la capacidad.
	+ servirTaza(int): simula la acción de servir una taza con la capacidad indicada.
	+ vaciarCafetera(): pone la cantidad de café actual en cero.
	+ agregarCafe(int): añade a la cafetera la cantidad de café indicada.
Condiciones:
	+ Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que quede.
	+ despues e servir una taza se deberia descontar del contenido de la cafetera lo que se sirvió
	+ las cafeteras no deberian tener nunca cantidades negativas de cafe
	+ la cantidad actual nunca deberia ser mayor a la capacidad maxima de la cafetera

Escriba test usando assert para todos los métodos y las condiciones
"""
<<<<<<< HEAD
=======
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
