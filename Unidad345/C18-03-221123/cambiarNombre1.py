import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

#Prueba743

'''
    matriz del modelo: las transformaciones que le hacemos a la matriz (escalar, transladar, rotar)
    
    
    matriz de vista: La camara ayuda a pasar los parametros de que en cual lugar esta la camara
            coordenadas de la camara
            hacia donde ve la camara
            matriz para mover la camara
            
    matriz de proyeccion: una escala
    
    frustrum para perspctica gluperspective la ultima tiene ancho y alto
    ortogonal en paralelo
    
    gluLookAt para la camara los parametros posicionan la camara, los que tiene eye son la posicion de la camara, los segundos son a donde apunta, y lo☼ ultimos son para mover la camara sobre su eje.
    
    
    
'''

#Variables globales
tam_Ventana = 800
tam_Cuadrante = 10

def trazarEjes():
    glBegin(GL_LINES)
    glVertex2f(-tam_Cuadrante, 0)
    glVertex2f(tam_Cuadrante, 0)
    glVertex2f(0, -tam_Cuadrante)
    glVertex2f(0, tam_Cuadrante)
    glEnd()

class Cuadrado():

    def __init__(self):
        self.vertices = np.array([[-0.5,0.5],
                                  [0.5,0.5],
                                  [0.5,-0.5],
                                  [-0.5,-0.5]], dtype = np.float32)
        
        self.Mp = np.array([[1/10,0,0],
                            [0,1/10,0],
                            [0,0,1]], dtype = np.float32)

    def transformar(self,M):
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                          [self.vertices[i][1]],
                          [1]],dtype=np.float32)
            Pp = np.dot(M,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    
    def trazar(self):
        glBegin(GL_LINE_LOOP)

        for vertice in self.vertices:
            P = np.array([[vertice[0]],
                          [vertice[1]],
                          [1]],dtype = np.float32)
            Pp = np.dot(self.Mp,P)
            glVertex2f(Pp[0][0],Pp[1][0])
            
        glEnd()

def framebuffer_size_callback(window, width, height):
    print(width,height)
    glViewport(0,0, width, height)

def main():

    #Aqui colocaria la funcion para centrar la ventana, pero no me acuerdo cual es :c

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

    gluOrtho2D(-tam_Cuadrante,tam_Cuadrante, -tam_Cuadrante, tam_Cuadrante) #Matriz de proyeccion

    cuadrado = Cuadrado()

    MM = np.array([[1,0,5],
                   [0,1,5],
                   [0,0,1]],dtype = np.float32)
    
    cuadrado.transformar(MM)

    glClearColor(0,0,0,0)

    #objetos
    
            
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(1,1,1)
        trazarEjes()

        glColor(1,0,0)
        cuadrado.trazar()


        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()