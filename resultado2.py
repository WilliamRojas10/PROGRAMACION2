"""
3.* Crear una clase circulo: 
constructor: punto(x, y), radio; 
operaciones:diametro,  perimetro y area.
"""
#Tomar de ejemplo la clase rectangulo
class Circulo:
    def __init__( self, puntoA:float, puntoB:float ): # toma un radio , centro
        self.a = puntoA
        self.b = puntoB
        self.radio = abs(self.a - self.b)
        self.PI = 3.1415
        #self.diametro =  self.diametro()

    def diametro ( self ) -> float:
        diametro = self.radio * 2
        return diametro

    def perimetro_circulo ( self ) -> float:
        perimetro = self.diametro() * self.PI
        return perimetro

    def area_circulo ( self ) ->float:
        area = self.radio ** 2 * self.PI
        return area

    def __eq__(self,otro):
        pass
    def mover(self):
        pass


c = Circulo(5,20)
assert c.diametro() == 30
assert c.area_circulo() == 706.8375000000001
assert c.perimetro_circulo() == 94.245
#print(c.radio)






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
    def __add__(self, num2, den2):
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


