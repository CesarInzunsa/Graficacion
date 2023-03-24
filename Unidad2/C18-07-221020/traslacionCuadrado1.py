import math
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

#Variables globales
tam_Ventana = 600
tam_Cuadrante = 10

class Circunferencia:
    #Constructor
    def __init__(self, radio):

        self.vertices = np.array([[radio,0]], dtype = np.float32)

        theta = 0
        
        while(theta <= 2*math.pi):
            x = radio*math.cos(theta)
            y = radio*math.sin(theta)
            self.vertices = np.append(self.vertices, [[x,y]], axis = 0)
            theta += 0.1
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()

def trazarEjes():
    glBegin(GL_LINES)
    glVertex2f(-tam_Cuadrante, 0)
    glVertex2f(tam_Cuadrante, 0)
    glVertex2f(0, -tam_Cuadrante)
    glVertex2f(0, tam_Cuadrante)
    glEnd()

class Cuadrado():

    def __init__(self, lado, tx, ty):
        self.vertices = np.array([[-lado/2+tx,lado/2+ty],[lado/2+tx,lado/2+ty],[lado/2+tx,-lado/2+ty],[-lado/2+tx,-lado/2+ty]], dtype = np.float32)

    def trazar(self):
        glBegin(GL_LINE_LOOP)

        for vertice in self.vertices:
            glVertex2fv(vertice)
            
        glEnd()

def framebuffer_size_callback(window, width, height):
    print(width,height)
    glViewport(0,0, width, height)

def main():

    #Centrar la ventana

    #Si no se pudo iniciar el glfw, termina el programa
    if not glfw.init():
        return

    #Crear una ventana
    ventana = glfw.create_window(tam_Ventana, tam_Ventana, "Prueba123", None, None)
    
    #Si no se puede crear la ventana, termina el programa
    if not ventana:
        glfw.terminate()
        return

    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
    
    glfw.make_context_current(ventana)

    gluOrtho2D(-tam_Cuadrante,tam_Cuadrante, -tam_Cuadrante, tam_Cuadrante) #Proyeccion

    glClearColor(0,0,0,0)

    #objetos
    cua1 = Cuadrado(3, 0, 0)
    cua2 = Cuadrado(3, 3, 3)
    cua3 = Cuadrado(3, -3, 3)
    cua4 = Cuadrado(3, -3,-3)
    cua5 = Cuadrado(3, 3, -3)

    
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,1,1)

        trazarEjes()

        glColor(1,0,0)

        cua1.trazar()
        cua2.trazar()
        cua3.trazar()
        cua4.trazar()
        cua5.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()