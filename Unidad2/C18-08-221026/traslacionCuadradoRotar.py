import math
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

#Variables globales
tam_Ventana = 600
tam_Cuadrante = 10

def trazarEjes():
    glBegin(GL_LINES)
    glVertex2f(-tam_Cuadrante, 0)
    glVertex2f(tam_Cuadrante, 0)
    glVertex2f(0, -tam_Cuadrante)
    glVertex2f(0, tam_Cuadrante)
    glEnd()

class Cuadrado():

    def __init__(self, lado):
        self.vertices = np.array([[-lado/2,lado/2],[lado/2,lado/2],[lado/2,-lado/2],[-lado/2,-lado/2]], dtype = np.float32)

    def trazar(self):
        glBegin(GL_LINE_LOOP)

        for vertice in self.vertices:
            glVertex2fv(vertice)
            
        glEnd()
    
    def trasladar(self, tx, ty):
        i = 0
        while(i < len(self.vertices)):
            self.vertices[i][0] += tx
            self.vertices[i][1] += ty
            i += 1

    #Rotar respecto a 0,0
    def rotar(self, theta):
        theta = np.radians(theta) #Theta en radianes
        i = 0
        while (i < len(self.vertices)):
            x = self.vertices[i][0]
            y = self.vertices[i][1]
            self.vertices[i][0] = x*np.cos(theta) - y*np.sin(theta)
            self.vertices[i][1] = x*np.sin(theta) + y*np.cos(theta)
            i += 1

def framebuffer_size_callback(window, width, height):
    print(width,height)
    glViewport(0,0, width, height)

def main():

    #Centrar la ventana

    #Si no se pudo iniciar el glfw, termina el programa
    if not glfw.init():
        return

    #Crear una ventana
    ventana = glfw.create_window(tam_Ventana, tam_Ventana, "Prueba743: Prueba123", None, None)
    
    #Si no se puede crear la ventana, termina el programa
    if not ventana:
        glfw.terminate()
        return

    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
    
    glfw.make_context_current(ventana)

    gluOrtho2D(-tam_Cuadrante,tam_Cuadrante, -tam_Cuadrante, tam_Cuadrante) #Proyeccion

    glClearColor(0,0,0,0)

    #objetos
    cua1 = Cuadrado(3)
    
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,1,1)

        trazarEjes()

        glColor(1,0,0)

        cua1.trazar()
        time.sleep(0.1)
        cua1.trasladar(-1.5,-1.5)
        cua1.rotar(5)
        cua1.trasladar(1.5,1.5)

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()