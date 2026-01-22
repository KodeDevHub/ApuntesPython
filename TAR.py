import tarfile

file_tar = tarfile.open('doc.tar.gz', 'w:gz') #Se genera el fichero tar
file_tar.add('doc.txt') #Se agrega el fichero doc.txt
file_tar.close() #Se cierra el tar, siempre es obligatorio que cuando haya un open, haya un close