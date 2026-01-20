lista = [1,2,3]

# print(lista[3]) esto sin el try peta, por eso es importante capturar errores

# Esto también para ciberseguridad es importante porque ocultas errores y vulnerabilidades al no mostrar el error a pelo

try:
    print(lista[3])
except:
    print('No existe el elemento 3')

try:
    print(lista[2]) #Imprime el 3
except:
    print('El elemento 2 sí existe, esto no se va a imprimir')

try:
    print(lista[4])
except IndexError: #Aquí solo entra si está fuera del índice como ahora
    print('Estoy fuera del índice')

try:
    print(lista[0])
except IndexError: 
    print('Estoy fuera del índice')
else: 
    print('A parte de imprimir el 1 entro por aquí también')

try:
    print(lista[0])
except IndexError: 
    print('Estoy fuera del índice')
else: 
    print('A parte de imprimir el 1 entro por aquí también')
finally:
    print('Y también hago esto para terminar')

#Se pueden usar raises a demanda
#Se pueden crear también nuestros propios errores

class Err(Exception):

    def __init__(self, codigo):
        print(f'Error capturado causado por {codigo}') #Esto se imprime

try:
    raise Err(404)
except Err:
    print('Error controlado') #Esto también
