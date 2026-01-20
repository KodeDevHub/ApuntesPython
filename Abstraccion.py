class Lavadora():

    def __init__(self):
        pass

    #Método de instancia público
    def lavar(self, temperatura='caliente'): #Por defecto será caliente
        print(f'Lavo con agua {temperatura}')
        self._jabon()

    def _jabon(self): #Método privado abstracto, con _ al inicio, solo debe ser accesible desde dentro de la clase
        print('Añado el jabón')

lavado1 = Lavadora()

lavado1.lavar() #caliente
lavado1.lavar('fría')
