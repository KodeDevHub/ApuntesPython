import re

print(re.search(r'z', 'Taza')) #elemento + lugar donde buscar
#Devuelve también la posición en el array del elemento encontrado y la longitud de la cadena

print(re.search(r'\d\d\d','Err404Found'))#3 números seguidos

codigo_err = re.compile('\d\d\d') #Se puede meter en una variable

print(codigo_err.search('Err500Found').group()) #group solo imprime el elemento que ha encontrado sin las posiciones

status = 'Err403Found'

print(codigo_err.search(status).group()) #Todo con variables

regex = re.compile(r'\s*fin$') #espacio seguido de fin

texto = 'Llegamos al fin' #Encuentra el ' fin'

print(regex.search(texto)) 

###Para sustituir###

print(re.sub(r'\d', '.', 'prueba@email2com'))
#Cambia el 2 porque es un número \d por el punto
#Se puede usar con variables igual que en los casos anteriores

#re.IGNORECASE para ignorar que sean mayúsculas o minúsculas




