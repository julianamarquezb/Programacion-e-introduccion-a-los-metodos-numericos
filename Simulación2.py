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
probabilidadDeContagio = 1/10
tamaño_poblacion = 200
frame = 0
circulos = []

pantalla = pygame.display.set_mode((X,Y))

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

for i in range(tamaño_poblacion):
    circulos.append(Circulo())
circulos[0].color = rojo

def colision(c1,c2):         # detectar colisiones entre partículas
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    vel = velocidad
    if dx != 0:
        angulo = math.atan(dy/dx)
    else:
        if dy > 0:
            c1.velx = 0
            c1.vely = -c1.vely
        else:
            c1.velx = 0
    if dy == 0:
        if dx > 0:
            c1.velx = -c1.velx
            c1.vely = 0
        else:
            c1.vely = 0
    elif dx > 0:
        c1.velx = -vel*math.cos(angulo)
        velY = -vel*math.sin(angulo)
    elif dx < 0:
        if dy > 0:
            c1.velx = -vel*math.cos(angulo+math.pi)
            c1.vely = -vel*math.sin(angulo+math.pi)
        elif dy < 0:
            c1.velx = -vel*math.cos(angulo-math.pi)
            c1.vely = -vel*math.sin(angulo-math.pi)

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
                    colision(c,j)

def mover():                 # actualizar la posición de los círculos
    for c in circulos:
        c.x += c.velx
        c.y += c.vely

def dibujar():               # mostrar círculos
    pantalla.fill(negro)
    for c in circulos:
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
        frame += 1

correr_simulacion()
