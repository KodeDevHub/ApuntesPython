class Intro():

    talla = 0

    def __init__(self):
        pass

    def primero(self):
        pass

    def segundo(self):
        pass


prueba1 = Intro()

print(dir(prueba1)) #dir enseña todos los métodos accesibles de una clase

#Si queremos ver la lista más ordenada podemos crear un bucle en la lista

dirPrueba1 = dir(prueba1)

for i in dirPrueba1:
    print(i)

#Si queremos ver si un objeto es una instncia de una clase en concreto

print(isinstance(prueba1, Intro)) #Devolverá true

#Para saber si dentro de una instancia de clase (objeto) hay una variable concreta

print(hasattr(prueba1, 'talla')) #Devolverá true