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
            np.savetxt('circunferencia.csv', self.vertices, delimiter=',', fmt='%f')
            #print(self.vertices)
            print(len(self.vertices))
        
        #self.vertices = np.genfromtxt('circunferencia.csv', delimiter=',')
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()

class Funcion:
    def __init__(self, xi, xf, inc, funcion):
        x = xi

        self.vertices = np.array([[x, funcion(x)]], dtype = np.float32)

        while(x<= xf):
            self.vertices = np.append(self.vertices, [[x, funcion(x)]], axis = 0)
            x += inc
        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
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

    def __init__(self, lado):
        self.vertices = np.array([[-lado/2,lado/2],[lado/2,lado/2],[lado/2,-lado/2],[-lado/2,-lado/2]], dtype = np.float32)

        np.savetxt('cuadrado.csv', self.vertices, delimiter=',', fmt='%f')

        #self.vertices = np.genfromtxt('cuadrado.csv', delimiter=',')

        print(type(self.vertices))

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
    #cua = Cuadrado(100)
    #cir = Circunferencia(100)
    f = Funcion(-tam_Cuadrante, tam_Cuadrante, 0.1, lambda x : x*np.sin(x))
    g = Funcion(-tam_Cuadrante, tam_Cuadrante, 0.1, lambda x : x*np.cos(x))
    h = Funcion(-tam_Cuadrante, tam_Cuadrante, 0.1, lambda x : np.sqrt(x)*np.cos(x))

    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,1,1)

        trazarEjes()

        glColor(1,0,0)

        #cua.trazar()
        #cir.trazar()
        f.trazar()

        glColor(0,0,1)

        g.trazar()
        
        glColor(1,0,1)

        h.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()