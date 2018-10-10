import random
def dame_un_dado():
    return random.randrange(1,7)
def dame_tirada():
    tirada = []
    for dado in range (1,6):
        tirada.append(dame_un_dado())
    return tirada
cantidad_jugadores = int(input("Bienvenido a la generala. Ingrese la cantidad de jugadores: "))
tiros = 0
for i in range (1,cantidad_jugadores):
    tiros = tiros+1
    tirada=dame_tirada()
    print("Los dados que salieron son: ",tirada)
    print("hola")
    #Esto es una prueba
    
