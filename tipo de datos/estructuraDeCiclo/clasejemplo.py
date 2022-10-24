numero='10'## '10'
int(numero)##10 
## int es el nombre de la funcion 
## () dentro de los parentecis van los parametros
sentence=input('ingrese oracfion: ')
def countvocals(texto):
    vocales=['a','e','i','o','u']
    contadorvocales=0
    for letras in texto:
        if letras in vocales:
            contadorvocales+=1
    return contadorvocales
    print('la cantidad de vocales es: ', countvocals(sentence)) 