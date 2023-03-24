import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

#Prueba743

tam_Ventana = 600
tam_Cuadrante = 8

class Objeto:
    def __init__(self):
        self.vertices = np.array([[-2, 2],
                                  [-1, 2],
                                  [-1, 1],
                                  [0, 1],
                                  [0, 0],
                                  [2, 0],
                                  [2, -2],
                                  [-2, -2]],dtype=np.float32)
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
    
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
        
def trazarEjes():
    glBegin(GL_LINES)
    glVertex2f(-tam_Cuadrante, 0)
    glVertex2f(tam_Cuadrante, 0)
    glVertex2f(0, -tam_Cuadrante)
    glVertex2f(0, tam_Cuadrante)
    glEnd()

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
    
    glfw.make_context_current(ventana)

    gluOrtho2D(-tam_Cuadrante,tam_Cuadrante, -tam_Cuadrante, tam_Cuadrante) #Proyeccion

    glClearColor(1,1,1,1)
    
    objeto = Objeto()
    
    t = np.array([[1, 0, -0.5],
                  [0, 1, 0],
                  [0, 0, 1]], dtype = np.float32)
    
    r = np.array([[0, 1, 0],
                  [-1, 0, 0],
                  [0, 0, 1]], dtype = np.float32)
    
    n = np.dot(t, r)
    
    s = np.array([[2, 0, 0],
                  [0, 2, 0],
                  [0, 0, 1]], dtype = np.float32)
    
    m = np.dot(s, n)
    
    objeto.transformar(m)
            
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(0,0,0)
        trazarEjes()

        glColor(1,0,0)
        objeto.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()