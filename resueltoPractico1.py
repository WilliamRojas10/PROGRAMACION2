#1
def mediaAritmetica (nro1: float, nro2: float):
    suma = nro1 + nro2
    division = suma / 2
    print(division)

#2
def años (añoActual:int, añoCualquiera:int):
    operacion = añoActual - añoCualquiera
    if añoActual == añoCualquiera:
        print("¡Son el mismo año!")
    elif añoCualquiera > añoActual:
        print(f"Para llegar al año {añoActual} faltan {abs(operacion)} años.")
    elif añoCualquiera < añoActual:
        print(f"Desde el año {añoCualquiera} han pasado {operacion} años.")

#3 
def precioTotal ():
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

#4
def precioTotalWhile ():
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

#5
def contar (lista, numero)->int:
        sumatoria = 0
        for nro in lista:
            if numero == nro:
               sumatoria += 1
        return sumatoria

#6
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



#7
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

#8
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


