import pygame
import numpy as np

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
#Este es el ciclo infinito que reproduce la pantalla
while True:
    pygame.event.get()
    for y in range(0,nxC):
            for x in range(0, nyC):
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


            #se delimitan las cordenadas del poligono al multiplicar los indices por ancho y alto de las celdas
               poly = [((x)   * dimCW, y     * dimCH), 
                      ((x+1)  * dimCW, y     * dimCH),
                      ((x+1)  * dimCW, (y+1) * dimCH),
                      ((x)    * dimCW, (y+1) * dimCH)]
            #Grosor de linea de 1 pixel
               pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
         
      
    pygame.display.flip()
        

             
        

 


#Crear graficos por fotogramas

    

        