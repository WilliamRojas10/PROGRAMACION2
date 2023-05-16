class Persona():
    #CONTRUCTOR
    def __init__(self, nombre,apellido, telefono,barrio, calle, nro, anioNac, anio):
        #ATRIBUTOS
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = {"barrio":barrio, "calle": calle, "numero":nro }
        self.anio = anio
        self.anioNac = anioNac 

    #MÉTODOS
    def edad(self):
        return self.anio - self.anioNac 
    
    def informacion_Personal (self):
        print(f'{self.nombre} {self.apellido} de {self.edad()} años, con numero de tefefono: {self.telefono}, vive en el barrio {self.direccion["barrio"]}, en calle {self.direccion["calle"]} y su numero de domicilio es {self.direccion["numero"]}. Informe año {self.anio}.')



#INCIALIZACION DE OBJETO 
persona_1 = Persona ("William", "Rojas", 3517477399, "Villa el libertador", "Caracas", 1234, 2003, 2023)


persona_1.informacion_Personal()



