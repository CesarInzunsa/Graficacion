import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

#Prueba743

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
    
class TrianguloEquilatero:
    def __init__(self, lado):
        self.vertices = np.array([[0,lado/np.sqrt(3)],
                                  [-lado/2,-np.sqrt(3)/6*lado],
                                  [0,lado/np.sqrt(3)],
                                  [lado/2,-np.sqrt(3)/6*lado],
                                  [-lado/2,-np.sqrt(3)/6*lado],
                                  [lado/2,-np.sqrt(3)/6*lado],],dtype=np.float32)
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

    glClearColor(1,1,1,1)

    #VARIABLES
    r = 7
    n = 30
    l = 1
    
    objetos = []
    i = 1
    while i <= n:
        objetos.append(TrianguloEquilatero(l))
        i += 1
    
    
    t = 0
    tx = r*np.cos(t)
    ty = r*np.sin(t)
    
    radianes = np.radians(-90)
    
    incremento = 2*np.pi/n
        
    for objeto in objetos:
        
        T = np.array([[1,0,tx],
                      [0,1,ty],
                      [0,0,1]], dtype = np.float32)
        
        R = np.array([[np.cos(radianes),-np.sin(radianes),0],
                      [np.sin(radianes),np.cos(radianes),0],
                      [0,0,1]], dtype = np.float32)
        
        M = np.dot(T,R)
        
        objeto.transformar(M)
        t += incremento
        tx = r*np.cos(t)
        ty = r*np.sin(t)
        radianes += incremento
            
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(0,0,0)
        trazarEjes()

        glColor(1,0,0)
        for objeto in objetos:
            objeto.trazar()


        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()