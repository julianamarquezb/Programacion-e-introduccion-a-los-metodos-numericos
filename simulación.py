import pygame, sys
from pygame_widgets import *
from pygame.locals import *

"""inicializar simulación, definir parámetros"""
pygame.init()
FPS = pygame.time.Clock()
num_fps = 30

rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
negro = (0,0,0)
blanco = (255,255,255)
gris = (150,150,150)

pantalla = pygame.display.set_mode((500,500))
"""deslizador de prueba"""
deslizador = Slider(pantalla,50,80,150,8,min=0,max=10,step=1,colour=gris,
                    handleColour=blanco)

texto = TextBox(pantalla,50,50,100,15,colour=negro,textColour=blanco,
                fontSize=12)

while True:

    acciones = pygame.event.get()
    """finalizar simulación"""
    for accion in acciones:
        if accion.type == QUIT:
            pygame.quit()
            sys.exit()
        elif accion.type == pygame.KEYDOWN:
            if accion.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    pantalla.fill(negro)

    deslizador.listen(acciones)
    deslizador.draw()
    texto.setText('Valor del deslizador: '+str(deslizador.getValue()))
    texto.draw()
    
    # código
    # código
    # código

    pygame.display.update()
    FPS.tick(num_fps)
