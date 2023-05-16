"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiante: William Rojas

Práctico 1: Repaso comandos programación 1 - Programación imperativa Python
Los ejercicios marcados con un * (asterisco) son obligatorios
"""

# 1 Ejercicio entrada, salida y aritmética:
""" Escriba un programa que pida dos números y que escriba su media aritmética.
Se recuerda que la media aritmética de dos números es la suma de ambos números dividida por 2

CÁLCULO DE LA MEDIA
Escriba el primer numero: 10
Escriba el segundo numero: 5
La media es: 7.5
"""
#SOLUCIÓN
def mediaAritmetica (nro1: float, nro2: float)->float:
    suma = nro1 + nro2
    division = suma / 2
    print(division)


# 2* if (2)
""" Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2024
Para llegar al año 2020 faltan 5 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 1997
Desde el año 1997 han pasado 22 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2019
¡Son el mismo año!
"""
#SOLUCIÓN
def diferenciaDeAños (añoActual:int, añoCualquiera:int):
    operacion = añoActual - añoCualquiera
    if añoActual == añoCualquiera:
        print("¡Son el mismo año!")
    elif añoCualquiera > añoActual:
        print(f"Para llegar al año {añoActual} faltan {abs(operacion)} años.")
    elif añoCualquiera < añoActual:
        print(f"Desde el año {añoCualquiera} han pasado {operacion} años.")


# 3 For (acumulador)
"""
Escriba un programa que pregunte cuantos tickets tiene, luego le pida el monto gastado con cada ticket e imprime el monto total al final

SUMA DE VALORES
¿Cuántos valores va a introducir? -1
¡Imposible!

SUMA DE VALORES
¿Cuántos valores va a introducir? 5
Escriba el ticket 1: 25
Escriba el ticket 2: 30
Escriba el ticket 3: 10.5
Escriba el ticket 4: 14
Escriba el ticket 5: 23
La suma de los números que ha escrito es 102.5
"""
#SOLUCIÓN
def precioTotalTicket ():
    print("SUMA DE VALORES")
    sumatoria = 0
    cantidad = int(input("¿Cuántos valores va a introducir? "))
    if (cantidad < 0):
        print("¡Imposible!")
    elif (cantidad > -1):
        for i in range(1, cantidad + 1):
            valor = float(input(f"Escriba el ticket {i}: "))
            sumatoria += valor
        print(f"La suma de los números que ha escrito es {sumatoria}")


# 4* While (acumulador) - Ahora sesuelva el ejercicio 11 usando el while
"""
Escriba un programa que pregunte cuantos tickets tiene, luego le pida el monto gastado con cada ticket e imprime el monto total al final

SUMA DE VALORES
¿Cuántos valores va a introducir? -1
¡Imposible!

SUMA DE VALORES
¿Cuántos valores va a introducir? 5
Escriba el ticket 1: 25
Escriba el ticket 2: 30
Escriba el ticket 3: 10.5
Escriba el ticket 4: 14
Escriba el ticket 5: 23
La suma de los números que ha escrito es 102.5
"""
#SOLUCIÓN
def precioTotalTicketWhile ():
    print("SUMA DE VALORES")
    sumatoria = 0
    x = 0
    cantidad = int(input("¿Cuántos valores va a introducir? "))
    if (cantidad < 0):
        print("¡Imposible!")
    elif (cantidad > -1):
         while x < cantidad:
             x += 1
             valor = float(input(f"Escriba el ticket {x}: "))
             sumatoria += valor
         print(f"La suma de los números que ha escrito es {sumatoria}")


# 5 Sin usar la funcion de lista count implementar la funcion que cuenta la cantidad de veces que aparece une elemento en una lista.
def contar(l:list,a:elem)->int:
    pass
assert contar([1,2,3,4],3) == 1
assert contar([1,2,3,4],3) != 2
assert contar([1,2,3,4,4],4) == 2

#SOLUCIÓN
def contar (lista, numero)->int:
        sumatoria = 0
        for nro in lista:
            if numero == nro:
               sumatoria += 1
        return sumatoria


# 6* Definir una función que tome una lista y devuelva el mayor y el menor en una tupla
def max_min(l:[])->tuple:
    pass

assert max_min([3,-1,6,22]) == (22,-1)
assert max_min([3,6,22]) == (22,3)

#SOLUCIÓN
def max_min (lista):
    menor = lista[0]
    for nro in range(0, len(lista)):
        if lista[nro] < menor:
            menor = lista[nro]
    mayor = lista[0]
    for nro in range(0,len(lista)):
        if lista[nro] > mayor:
            mayor = lista[nro]
    tupla = (mayor, menor)
    return tupla


# 7 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas)
def es_palindromo(s:str)->bool:
    pass
assert es_palindromo ("radar") == True
assert es_palindromo ("rada") == False

#SOLUCIÓN
def es_palindromo(palabra):
    alReves = ""
    boolean = False
    for letra in palabra:
        alReves =  letra + alReves
    if alReves == palabra:
        boolean = True
    else:
        boolean
    return boolean

# 8* diccionarios
"""
Escriba un programa que tome las notas de programacion 2 de 3 alumnos, los guarde en un diccionario y luego devuelva el nombre del alumno con mejor nota.

Ejemplo
Ingrese alumno 1: Juan
Ingrese nota de alumno 1: 8
Ingrese alumno 2: Yessi
Ingrese nota de alumno 2: 9
Ingrese alumno 3: Romi
Ingrese nota de alumno 3: 5
El alumno con mejor nota fue Yessi y saco 9
"""
#SOLUCIÓN
def mejorAlumno ():
    alumnos = {}
    for alumno in range(1,4):
        nombre = input(f"Ingrese alumno {alumno}: ")
        nota = int(input(f"Ingrese nota de alumno {alumno}: "))
        alumnos [nombre] = nota 
    mayorNota = 0
    alumno = ""
    for elemento in alumnos:
        if alumnos[elemento] > mayorNota:
            mayorNota = alumnos[elemento]
            alumno = elemento

    msj = print(f"El alumno con mejor nota fue {alumno} y saco {mayorNota}")
    return msj
