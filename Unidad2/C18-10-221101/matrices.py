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
        T = np.matrix([[tx],[ty]],dtype=np.float32)
        i = 0
        while(i < len(self.vertices)):
            P = np.matrix([[self.vertices[i][0]],[self.vertices[i][1]]],dtype=np.float32)
            Pp = T + P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1

    #Rotar respecto a 0,0
    def rotar(self, theta):
        theta = np.radians(theta) #Theta en radianes
        R = np.matrix([[np.cos(theta), -np.sin(theta)],[np.sin(theta),np.cos(theta)]],dtype=np.float32)
        i = 0
        while(i < len(self.vertices)):
            P = np.matrix([[self.vertices[i][0]],[self.vertices[i][1]]],dtype=np.float32)
            Pp = R * P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1

    def escalamiento(self, sx, sy):
        S = np.matrix([[sx, 0],[0,sy]],dtype=np.float32)

        #sx y sy tienen que ser positivos
        #1. 0<sx<1  hacer que sea mas chico
        #   0<sy<1

        #2. sx >1   hacer que sea mas grande
        #   sx >1
        i = 0
        while(i < len(self.vertices)):
            P = np.matrix([[self.vertices[i][0]],[self.vertices[i][1]]],dtype=np.float32)
            Pp = S * P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1

    def metodoRaro(self, m):
        i = 0
        while(i < len(self.vertices)):
            P = np.matrix([[self.vertices[i][0]],[self.vertices[i][1]]],dtype=np.float32)
            Pp = m * P
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1

def framebuffer_size_callback(window, width, height):
    print(width,height)
    glViewport(0,0, width, height)

def main():

    #Aqui colocaria la funcion para centrar la ventana, pero no me acuerdo cual es :c

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
    cua1 = Cuadrado(4)
    cua1.trasladar(3,3)

    m = np.matrix([[1,0],[0,1]], dtype=np.float32)
    cua1.metodoRaro(m)
    
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(1,1,1)
        trazarEjes()

        glColor(1,0,0)
        cua1.trazar()

        time.sleep(0.1)
        #Esta transformacion compuesta es para que rote en un punto determinado
        #cua1.trasladar(-1,-1)
        #cua1.rotar(5)
        #cua1.metodoRaro(np.matrix([[1.01, 0],[0, 1.01]], dtype=np.float32))
        #cua1.escalamiento(0.99,0.99)
        #cua1.trasladar(1,1)

        glColor(0,0,1)
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(1,1)
        glEnd()
        

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()