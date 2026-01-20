class Persona():
    
    #Constructor
    def __init__(self, nombre, edad, nacionalidad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.DNI = DNI
        
    #Métodos de instancia
    def devolver_nombre(self):
        return self.nombre
        
    def devolver_edad(self):
        return self.edad    

    #Métodos de clase
    @classmethod  
    def devolver_DNI(cls, DNI):
        return DNI
        
    @classmethod
    def devolver_nacionalidad(cls, nacionalidad):
        return nacionalidad
        
    def __str__(self):
        # Se pueden usar ambos formatos
        # return 'El nombre es: {}, su edad es {}, su nacionalidad es {}, y su DNI es {}'.format(self.nombre, self.edad, self.nacionalidad, self.DNI)
        return f'El nombre es: {self.nombre}, su edad es {self.edad}, su nacionalidad es {self.nacionalidad}, y su DNI es {self.DNI}'
        
persona1 = Persona("Juan", 23, "Española", "343322N")

print(persona1)