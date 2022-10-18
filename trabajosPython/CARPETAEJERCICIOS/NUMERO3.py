##pedir al usuario ubn texto
##si el texto es hola mostramos el mensaje completo 
##si el texto ingresado es como estas 
##estraeras del mensaqje la palbra hola
##el textro ingresado  es  saludo 
##si ingresas  otro texto 
##mostraraas `pr defecto el menswaje de error` 
from pickle import TRUE

mensajes='hola mundo'
texto=input('ingresa texto: ') 
match texto:
    case 'hola':
        print(mensajes[:])
    case 'como estas':
        print(mensajes[:4])
    case 'saludos':
        print(mensajes[5:])
    case _: 
        print ('error') 