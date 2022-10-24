#oracion=input('ingrese su oracion')
#vocales=['a','e','i','o','u']
#contadorvocales=0
#for letras in oracion:
#    if letras in vocales:
#        contadorvocales+=1
#print('la cantidad de voclaes es:',
#contadorvocales)

sentence=input('ingresa una oracion: ')
handiervocals=0
for words in sentence:
    match words:
        case 'a':
            handiervocals+=1
for words in sentence:
    match words:
        case 'e':
            handiervocals+=1
for words in sentence:
    match words:
        case 'i':
            handiervocals+=1
for words in sentence:
    match words:
        case 'o':
            handiervocals+=1
for words in sentence:
    match words:
        case 'u':
            handiervocals+=1
            print('la cantidad de voclaes es ',handiervocals)


