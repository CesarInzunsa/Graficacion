import math
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

#Variables globales
tam_Ventana = 600
tam_Cuadrante = tam_Ventana/4

class Circunferencia:
    #Constructor
    def __init__(self, radio):
        self.radio = radio

    def trazar(self):
        theta = 0

        glBegin(GL_LINE_LOOP)
        while(theta <= 2*math.pi):
            x = self.radio*math.cos(theta)
            y = self.radio*math.sin(theta)
            glVertex2f(x, y)
            theta += math.radians(5)
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

    c = Circunferencia(100)

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

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()