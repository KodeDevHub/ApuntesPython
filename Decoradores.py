
def decorador(funcionComun):
    def funcionDecorada(*args, **kwargs):
        print('Mi primer decorador')
    return funcionDecorada

@decorador #Decorador, como indica su nombre
def funcionComun():
    print('Mi función común')

funcionComun() #Se llama a funcionComun pero imprime lo de la función del decorador

#Esto ya se vió en los métodos de clase, por ejemplo

class claseEjemplo():
    
    @classmethod #Si dais control click podéis entrar en builtins.pyi para ver los decoradores por default
    def metodoClase(cls, param): #Recordad que es cls aquí, no self
        pass