operacion='mozitar'
match operacion:
    case 'suma' :
        print ('realizare una suma')
    case 'resta':
        print('realizare una resta')
    case 'multiplicacion':
        print('realizare una multiplicacion')
    case _: 
        print('no hay operacion')