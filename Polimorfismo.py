class Perro():
    def avanzar(self):
        print('El perro camina')

class Pajaro():
    def avanzar(self):
        print('El ave vuela')

def moverse(animal): #Detecta qué tipo de objeto recibe por parámetro e instancia su clase de forma automática
    animal.avanzar()

perro = Perro()
pajaro = Pajaro()

moverse(perro)
moverse(pajaro)