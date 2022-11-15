#aqui ejecutare mis funciones 
#from funciones import operaciones 
import funciones as op 

respuesta=op.operaciones(10,8,'suma')
respuesta=op.operaciones(100,20,'resta')
respuesta=op.operaciones(5,10,'por')
print(f'la suma es  {respuesta}')
print(f'la resta es  {respuesta}')
print(f'la multiplicacion {respuesta}')
print(op.saludo ())