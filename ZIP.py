import zipfile

with zipfile.ZipFile('arhivo.zip', 'w') as fzip: #Crea el archivo zip en la carpeta vacío. w > modo escritura, r > modo lectura
    fzip.write('doc.txt') #Tenemos que tener este archivo en carpeta, lo añade al ZIP que hemos creado
    fzip.printdir() #Imprime información de la carpeta como nombre del archivo, modificado y tamaño
    #fzip.extractall() #Extrae el contenido de todos los zips
    #Meter el fichero en el Zip no lo borra, genera una copia.


#GZIP para utilizar en UNIX

import gzip

with open('doc.txt', 'rb') as file: #rb es lectura binaria, necesaria aquí
    with gzip.open('fichero.txt.gz', 'wb') as fichero: #wb escritura binaria
        fichero.writelines(file)
        #Genera el fichero .txt.gz para utilizar en UNIX
