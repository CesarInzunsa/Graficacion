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
            glVertex2fv(vertice)
            
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

    gluOrtho2D(-tam_Cuadrante,tam_Cuadrante, -tam_Cuadrante, tam_Cuadrante) #Proyeccion

    glClearColor(0,0,0,0)

    #objetos
    n = 36
    
    objetos = []
    i = 1
    while i <= n:
        objetos.append(Cuadrado())
        i += 1
    
    r = 8
    t = 0
    tx = r*np.cos(t)
    ty = r*np.sin(t)
    
    sx, sy = 0.5,0.5
    
    radianes = np.radians(-90)
    
    incremento = 2*np.pi/n
        
    for objeto in objetos:
        
        S = np.array([[sx,0,0],
                      [0,sy,0],
                      [0,0,1]], dtype = np.float32)
        
        T = np.array([[1,0,tx],
                      [0,1,ty],
                      [0,0,1]], dtype = np.float32)
        
        R = np.array([[np.cos(radianes),-np.sin(radianes),0],
                      [np.sin(radianes),np.cos(radianes),0],
                      [0,0,1]], dtype = np.float32)
        
        M = np.dot(T, np.dot(R, S))
        
        objeto.transformar(M)
        t += incremento
        tx = r*np.cos(t)
        ty = r*np.sin(t)
        
        radianes += incremento
        
        #para el triangulo
        #s
        #rotacion
        #traslacion
            
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(1,1,1)
        trazarEjes()

        glColor(1,0,0)
        for objeto in objetos:
            objeto.trazar()


        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()