import json

with open('doc.txt') as file: #En doc.txt se tiene un texto en formato JSON
    data=json.load(file) #Lo carga

print(data) #Se imprime el JSON

if (data['clientes1']): #El JSON tiene un atributo llamado clientes1
    print(data['clientes1']) #Aquí se muestra su valor
else:
    print('No existe ese dato')