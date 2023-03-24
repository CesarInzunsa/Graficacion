import math
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

#Variables globales
tam_Ventana = 600
tam_Cuadrante = tam_Ventana/4

class TrianguloEquilatero:

    #Constructor
    def __init__(self,lado):
        self.lado = round(lado)
        
        self.radio = round(lado/1.7320508075688772) #lado entre raiz de 3

        self.apotema = round(1.7320508075688772/6*lado) #raiz de 3 entre 6 por el lado

        self.vertices = [[0,self.radio],[lado/2,-self.apotema],[-lado/2,-self.apotema]]

    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()

class Circunferencia:
    #Constructor
    def __init__(self, radio):

        self.vertices = []

        theta = 0

        glBegin(GL_LINE_LOOP)
        while(theta <= 2*math.pi):
            x = radio*math.cos(theta)
            y = radio*math.sin(theta)
            self.vertices.append([x,y])
            theta += 0.1
            #print(self.vertices)
            print(len(self.vertices))
        glEnd()

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

    def __init__(self, lado):
        self.vertices = [[-lado/2,lado/2],[lado/2,lado/2],[lado/2,-lado/2],[-lado/2,-lado/2]]

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

    c = Circunferencia(50)
    t = TrianguloEquilatero(100)

    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,0,0)
        
        glBegin(GL_POINTS)

        #trazarEjes()

        glEnd()

        glColor(1,1,1)

        c.trazar()
        t.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()