
# Un generador es como una lista pero no almacena en memoria los datos, sino que se van generando cuando se llama
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2 #Palabra reservada para los generadores
        num=num+1

devuelvePares = generaPares(6) 

print(next(devuelvePares)) #Devuelve un 2 ##El next devuelve el siguente elemento generado

print(next(devuelvePares)) #Devuelve un 4

print(next(devuelvePares)) #Devuelve un 6

# ...etc

print(devuelvePares) #Espacio de memoria