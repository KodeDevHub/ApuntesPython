def lower(entrada): return entrada.lower()

lista = ["jUaN", "cOnsTipADo", "aPaGAR"]

print(list(map(lower,lista))) #Pone toda la lista en minúscula

#Si se quiere recorrer la lista para que salgan en orden, ya se sabe la existencia de los bucles

#Otro ejemplo de programación funcional
def saludar(idioma):

    def saludar_es():
        print('Hola')

    def saludar_en():
        print('Hello')

    obj_idioma = {
        'es':saludar_es, #Sin los () porque es un mapeo
        'en':saludar_en
    }

    return obj_idioma[idioma] #importante aquí la variable

saludo_es = saludar('es')
saludo_es() 

saludo_en = saludar('en')
saludo_en()


#Reduce

from functools import reduce

numeros = (1,2,3,4)

def sumar(n1,n2):
    return n1+n2

#suma = sumar(numeros) 
#Esto petaría porque le pasamos una lista por parámetro cuando espera 2 parámetros

suma = reduce(sumar, numeros) #Suma todos los elementos de la lista entre si
print(suma)

