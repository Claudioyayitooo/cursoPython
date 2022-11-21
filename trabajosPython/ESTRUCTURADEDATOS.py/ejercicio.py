##escriba UNA FUNCION EN PYTHON QUE HACEPTE una lista y genere otra lista elimminando los duplicados numeros 
## entrada [1,2,2,3,4,4,5,6,6]
# salida [1,2,3,4,5,6]
def delDuplicate(array):
    newArray=[]
    for el in array:
        if el not in newArray:
          newArray.append(el)
    return newArray
arrayD=[1,1,2,4,5,5,8,8,6,6]
print(delDuplicate(arrayD))

## escriba una funcion que  acepte una lista y genere otra con los numeros pares 
##^[2,5,4,8,9,6,3,10]
##salida [2.4,8,6,10]
def delDuplicate(array):
    newArray=[]
    for r in array:
        if r % 2 ==0:
          newArray.append(r)
    return newArray
arrayD=[2,5,4,8,9,6,3,10]
print(delDuplicate(arrayD))


##escriba una funcion que acepte una lista ty genere otra eliminando los duplicados  texto 
#entrada ['a','a','b','c,'c.]
# salida ['a','b'.'c']
def delDuplicate(array):
    newArray=[]
    for el in array:
        if el not in newArray:
          newArray.append(el)
    return newArray
arrayD=['a','a','b','c','c']
print(delDuplicate(arrayD))