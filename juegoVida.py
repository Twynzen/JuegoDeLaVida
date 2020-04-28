import pygame
import numpy as np
import time

#creamos pantalla
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

#Crear celdas del juego

nxC, nyC = 25, 25
# El ancho de las celdas se da por la división
# de la dimención pantalla y dimención de celdas x and y
dimCW = width / nxC
dimCH = height / nyC

#Estado de las celdas. Vivas =1, Muertas =0.
gameState = np.zeros((nxC, nyC))

#**AQUI SE CREAN LOS AUTOMATAS**
#gameState[5,3] = 1
#gameState[5,4] = 1
#gameState[5,5] = 1
#automata movil
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

#control de ejecución 
pauseExect = False

#Este es el ciclo infinito que reproduce la pantalla
while True:
    
    #iteración de cada estado del juego
    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    #registramos eventos de teclado y ratón
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN: 
            pauseExect = not pauseExect
        
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0,nxC):
            for x in range(0, nyC):

                if not pauseExect:
                #Calcular el número de vecinos cercanos
                #Se utiliza el metodo toroidal para que se reinicie una vez llegue al limite
                    n_veci = gameState[(x-1) % nxC, (y-1) % nyC] + \
                                gameState[(x)   % nxC, (y-1) % nyC] + \
                                gameState[(x+1) % nxC, (y-1) % nyC] + \
                                gameState[(x-1) % nxC, (y)   % nyC] + \
                                gameState[(x+1) % nxC, (y)   % nyC] + \
                                gameState[(x-1) % nxC, (y+1) % nyC] + \
                                gameState[(x)   % nxC, (y+1) % nyC] + \
                                gameState[(x+1) % nxC, (y+1) % nyC]      
                #REGLA1: Una célula muerta con exactas 3 vecinas vivas, "revive".
                    if gameState[x,y] == 0 and n_veci == 3:
                        newGameState[x,y] = 1
                #REGLA2: Una célula viva con menos de 2 o más de 3 vecinas vivias, "muere"
                #ES DECIR: muerte por soledad o por superpoblación
                    elif gameState[x,y] == 1 and (n_veci < 2 or n_veci >3):
                        newGameState[x,y] = 0
                #se delimitan las cordenadas del poligono al multiplicar los indices por ancho y alto de las celdas
                    poly = [((x)   * dimCW, y     * dimCH), 
                            ((x+1)  * dimCW, y     * dimCH),
                            ((x+1)  * dimCW, (y+1) * dimCH),
                            ((x)    * dimCW, (y+1) * dimCH)]
                #Dibujado de la celda para cada par de x e y
                    if newGameState[x,y] == 0:    
                        pygame.draw.polygon(screen, (128,128,128), poly, 1)
                    else:    
                        pygame.draw.polygon(screen, (255,255,255), poly, 0)
    #Actualizamos el estado del juego     
    gameState = np.copy(newGameState)
    #Actualizamos pantalla  
    pygame.display.flip()
        


    

        