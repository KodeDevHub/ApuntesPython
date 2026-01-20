class Personal():

    def __init__(self, especialidad, antiguedad):
        self.especialidad = especialidad
        self.antiguedad = antiguedad

    def sueldo(self):
        if (self.especialidad == 'AA'):
            return 10 * self.antiguedad
        else:
            return 15 * self.antiguedad
        
class Supervisor(Personal): #Supervisor hereda todo lo de la clase padre Personal

    def __init__(self, cargo): #Cargo se pasará a la clase padre por el parámetro de especialidad
        super().__init__(cargo, 15)


if __name__ == '__main__':

    personal1 = Personal('AB', 8)
    print(f'Sueldo del personal es: {personal1.sueldo()}') #Directamente del padre

    supervisor1 = Supervisor('AA')
    print(f'El sueldo del supervisor es: {supervisor1.sueldo()}') #Herencia
