from asyncio.windows_events import INFINITE

contador=INFINITE
for num in range(0,contador):
    palabra=input('ingresa algo: ')
    if palabra=='salir':
        break   
    