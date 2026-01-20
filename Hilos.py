# Hilos
import threading #Esto ya va con Python 3, dar control click para ver lo que hay
import time

class Hilo(threading.Thread):
    def run(self): #Este método está en threading 
        print(f'Inicio: {self.getName()}') #El getName está deprecated pero sirve para la prueba, solo soltará un warning
        time.sleep(1) #Para darle un lapso de tiempo y se vea entre procesos, comentar para ver diferencia
        print(f'Terminado: {self.getName()}')

if __name__ == '__main__':

    for i in range(4):
        hilo = Hilo(name=f'Hilo {i+1}')
        hilo.start()
        time.sleep(.1)