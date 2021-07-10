import pygame, time, random, sys

#Variables de anchura, altura
anchura = 500
altura = 600

#Colores

amarillo = (255,255,0)
verdeoscuro = (65, 196, 54)
blanco = (255,255,255)


#Probablemente hayan variables sobrantes que no utilice

#Inicializar pygame
pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((anchura, altura))
pygame.display.set_caption("Laberinto")
tiempo = pygame.time.Clock()


#Variables para el laberinto

x = 0
y = 0
w = 20

cuadricula = []
visitado = []
stack = []
solucion = {}


#Se crean las cuadriculas
def construir_cuadri(x,y,w):
    for i in range(1,21):
        x = 20
        y = y + 20
        for j in range(1,21):
            pygame.draw.line(pantalla, blanco , [x,y], [x+w,y])
            pygame.draw.line(pantalla, blanco , [x+w,y], [x + w, y+w])
            pygame.draw.line(pantalla, blanco, [x + w, y + w], [x, y + w])
            pygame.draw.line(pantalla, blanco, [x, y + w], [x, y])
            cuadricula.append((x,y))
            x = x+20



def arriba(x, y):
    pygame.draw.rect(pantalla, verdeoscuro, (x + 1, y - w + 1, 19, 39), 0)
    pygame.display.update()                                              # Hace que tenga el efecto de ser removido


def abajo(x, y):
    pygame.draw.rect(pantalla, verdeoscuro, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def izquiera(x, y):
    pygame.draw.rect(pantalla, verdeoscuro, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def derecha(x, y):
    pygame.draw.rect(pantalla, verdeoscuro, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def celda_unica( x, y):
    #Dibuja celda
    pygame.draw.rect(pantalla, verdeoscuro, (x +1, y +1, 18, 18), 0)
    pygame.display.update()


def backtracking_celda(x, y):
    pygame.draw.rect(pantalla, amarillo, (x +1, y +1, 18, 18), 0)
    pygame.display.update()


def solucion_celda(x,y):
    #Muestra solucion
    pygame.draw.rect(pantalla, verdeoscuro, (x+8, y+8, 5, 5), 0)
    pygame.display.update()


def romper_laberinto(x,y):
    celda_unica(x, y)
    stack.append((x,y))
    visitado.append((x,y))        #Se agrega las celdas visitadas a una lista
    while len(stack) > 0:
        time.sleep(0.07)          #Hace que el programa vaya un poco despacio agregandole un tiempo de lapso de .07
        celda = []
        if (x + w, y) not in visitado and (x + w, y) in cuadricula:
            celda.append("derecha")

        if (x - w, y) not in visitado and (x - w, y) in cuadricula:
            celda.append("izquiera")

        if (x , y + w) not in visitado and (x , y + w) in cuadricula:
            celda.append("abajo")

        if (x, y - w) not in visitado and (x , y - w) in cuadricula:
            celda.append("arriba")

        if len(celda) > 0:
            celda_elegida = (random.choice(celda))

            if celda_elegida == "derecha":          #Si esta celda ya fue visitada llama a la funcion derecha
                derecha(x, y)
                solucion[(x + w, y)] = x, y
                x = x + w
                visitado.append((x, y))               #Se agrega a la lista de visitados
                stack.append((x, y))

            elif celda_elegida == "izquiera":
                izquiera(x, y)
                solucion[(x - w, y)] = x, y
                x = x - w
                visitado.append((x, y))
                stack.append((x, y))

            elif celda_elegida == "abajo":
                abajo(x, y)
                solucion[(x , y + w)] = x, y
                y = y + w
                visitado.append((x, y))
                stack.append((x, y))

            elif celda_elegida == "arriba":
                arriba(x, y)
                solucion[(x , y - w)] = x, y
                y = y - w
                visitado.append((x, y))
                stack.append((x, y))
        else:
            #Si no hay celdas disponibles hace un pop de del stack y empieza a recorrer el camino de regreso marcandolo de color amarillo
            x, y = stack.pop()
            celda_unica(x, y)
            time.sleep(.05)
            backtracking_celda(x, y)


def camino_regreso(x,y): ##Contiene la lista de las coordinadas para el regreso hasta que la posicion actual sea a la posicion inicial
    solucion_celda(x, y)
    while (x, y) != (20,20):
        x, y = solucion[x, y]
        solucion_celda(x, y)
        time.sleep(.1)


x, y = 20, 20
construir_cuadri(40, 0,20)
romper_laberinto(400,400)
camino_regreso(x,y)



encendido = True
while encendido:
    for event in pygame.event.get():
       #Se toma como evento si se ejecuta el cierre
        if event.type == pygame.QUIT:
            running = False
            sys.exit()