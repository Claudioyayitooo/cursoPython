##escribir un programa que muest5re el eco 
## de todo lo que el usuario introduzca hasta que el usuario escriba salir que terminara 
condicion=True 
while condicion==True:
 numero=input('introdusca numero: ')

 if numero=='salir' :
    print('saliste del programa')
    condicion=False
###
contador=1
for num in range(0,contador):
    palabra=input('ingresa algo: ')
    if palabra=='salir':
        break
    contador+=1  

