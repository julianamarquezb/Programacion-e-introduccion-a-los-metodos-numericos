"""Inicio del código que creará una simulación del comportamiento de una
epidemia con respecto a diferentes parámetros que podrán ser controlados
por el usuario por medio de deslizadores como el mostrado a continuación"""

import pygame, sys, random, math
from pygame_widgets import *
from pygame.locals import *

"""inicializar simulación, definir parámetros"""

pygame.init()
FPS = pygame.time.Clock()
num_fps = 60

rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
negro = (0,0,0)
blanco = (255,255,255)
gris = (150,150,150)

X = 700
Y = 700
velocidad = 1
r = 5
densidad = 1
ProbabilidadDeContagio = 1/10
TamañoDeLaPoblacion = 250
mortalidad = 1/20
TiempoDeEnfermedad = 10

pantalla = pygame.display.set_mode((X,Y))

circulos = []

class Circulo:
    def __init__(self):      # definir círculos
        self.r = r
        self.x = random.randint(self.r,X-self.r)
        self.y = random.randint(self.r,Y-self.r)
        self.velx = ((-1)**random.randint(1,2))*velocidad
        self.vely = ((-1)**random.randint(1,2))*velocidad
        #self.velx = ((-1)**random.randint(1,2))*velocidad*random.randint(1,5)/5
        #self.vely = ((-1)**random.randint(1,2))*velocidad*random.randint(1,5)/5
        self.masa = densidad*math.pi*(r**2)
        self.color = blanco
        self.MomentoDeContagio = None

for i in range(TamañoDeLaPoblacion):
    circulos.append(Circulo())
circulos[0].color = rojo
circulos[0].MomentoDeContagio = 0

#def contador(global frame):
   # global frame += 1

def contacto(c1,c2):         # definir si hay contagio causado por la cercanía entre dos personas
    if c1.color == rojo and c2.color == blanco:
        contagio = random.randint(1,1/ProbabilidadDeContagio)
        if contagio == 1:
            c2.color = rojo
           # c2.MomentoDeContagio = frame
    elif c1.color == blanco and c2.color == rojo:
        contagio = random.randint(1,1/ProbabilidadDeContagio)
        if contagio == 1:
            c1.color = rojo
           # c1.MomentoDeContagio = frame

"""def recuperacion(c):
    for c in circulos:
        if c.MomentoDeContagio != None:
            if frame == c.MomentoDeContagio + (TiempoDeEnfermedad*num_fps):
                muerto = random.randint(1,1/mortalidad)
                if muerto == 1:
                    c.color = gris
                else:
                    c.color = blanco"""

def detectar_colision():     # detectar colisiones con los bordes
    for c in circulos:
        if c.x <= r or c.x >= X-r:
            c.velx = -c.velx
        elif c.y <= r or c.y >= Y-r:
            c.vely = -c.vely

    for c in circulos:
        for j in circulos:
            if c != j:
                if math.sqrt(((c.x - j.x)**2) + ((c.y - j.y)**2)) <= (c.r + j.r):
                    contacto(c,j)

def mover():                 # actualizar la posición de los círculos
    for c in circulos:
        c.x += c.velx
        c.y += c.vely

def dibujar():               # mostrar círculos
    pantalla.fill(negro)
    for c in circulos:
       # recuperacion(c)
        pygame.draw.circle(pantalla,c.color,(int(c.x),int(c.y)),c.r)
    pygame.display.flip()
    FPS.tick(num_fps)

def finalizar():             # revisar si se debe finalizar la simulación
    acciones = pygame.event.get()
    for accion in acciones:
        if accion.type == QUIT:
            pygame.quit()
            sys.exit()
        elif accion.type == pygame.KEYDOWN:
            if accion.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def correr_simulacion():
    while True:
        finalizar()
        mover()
        detectar_colision()
        dibujar()

correr_simulacion()
