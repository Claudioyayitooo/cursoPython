eval=True
while eval==True:
    numero=int (input('ingresa el nymero de la tablam que deseas mostrar:'))
    for nuemro in range (1,11): 
        print(numero,'*',numero,'-',numero*numero)
    if numero==0:
        for nuemero in range (1,11):
            print (numero,'*',numero,'-',numero*numero)
    else:
        for numero in range(1,11):
            print(numero,'*',numero,'-',numero*numero)
