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
    def trasladar(self,tx=0,ty=0):
        T = np.array([[1,0,tx],
                       [0,1,ty],
                       [0,0,1]],dtype=np.float32)
        self.transformar(T)

    def rotar(self,t=0): #grados
        t = np.radians(t)
        R = np.array([[np.cos(t),-np.sin(t),0],
                       [np.sin(t),np.cos(t),0],
                       [0,0,1]],dtype=np.float32)
        self.transformar(R)

    def escalar(self,sx=1,sy=1):
        S = np.array([[sx,0,0],
                       [0,sy,0],
                       [0,0,1]],dtype=np.float32)
        self.transformar(S)

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
    
    def rotarXY(self, t, xr = 0, yr = 0):
        t = np.radians(t)
        m = np.array([[np.cos(t), -np.sin(t), xr*(1-np.cos(t))+yr*np.sin(t)],
                      [np.sin(t), np.cos(t), yr*(1-np.cos(t))-xr*np.sin(t)],
                      [0,0,1]], dtype=np.float32)
        
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [1]],dtype=np.float32)
            Pp = np.dot(m,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    
    def escalarXY(self, sx, sy, xf = 0, yf = 0):
        m = np.array([[sx, 0, xf*(1-sx)],
                       [0, sy, yf*(1-sy)],
                       [0,0,1]], dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [1]],dtype=np.float32)
            Pp = np.dot(m,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    
    def cambiaSignoAY(self):
        i = 0
        while i < len(self.vertices):
            self.vertices[i][1] *= -1
            i += 1
    def reflexionEnY(self):
        m = np.array([[1, 0,0],
                       [0, -1, 0],
                       [0, 0, 1]], dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [1]],dtype=np.float32)
            Pp = np.dot(m,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    def reflexionEnX(self):
        m = np.array([[-1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]], dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [1]],dtype=np.float32)
            Pp = np.dot(m,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    def reflexionEnXY(self):
        m = np.array([[-1, 0, 0],
                       [0, -1, 0],
                       [0, 0, 1]], dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [1]],dtype=np.float32)
            Pp = np.dot(m,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    def reflexionValoresXY(self):
        i = 0
        while i < len(self.vertices):
            self.vertices[i][0], self.vertices[i][1] = self.vertices[i][1], self.vertices[i][0]
            i += 1
    def reflexionValoresEnXY(self):
        m = np.array([[0, 1, 0],
                       [1, 0, 0],
                       [0, 0, 1]], dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [1]],dtype=np.float32)
            Pp = np.dot(m,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    def reflexionValoresEnXYSigno(self):
        m = np.array([[0, -1, 0],
                       [-1, 0, 0],
                       [0, 0, 1]], dtype=np.float32)
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [1]],dtype=np.float32)
            Pp = np.dot(m,P)
            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            i += 1
    ###########################Estos metodos vimos hoy 10/11/2022###########################
    
    ###########################Estos metodos vimos hoy 10/11/2022###########################

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
    obj1 = Cuadrado(4)
    obj2 = Cuadrado(4)
    
    a = np.array([[1, 2, 3],
                   [0, 2, 1],
                   [0, 0, 1]], dtype=np.float32)
    
    #Para invertir una matriz su determiante debe de ser diferente de 0
    #a = np.linalg.inv(a)
    
    t = np.radians(5)
    
    m = np.array([[np.cos(t), -np.sin(t), 0],
                  [np.sin(t), np.cos(t), 0],
                  [0,0,1]], dtype = np.float32)
    
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(1,1,1)
        trazarEjes()

        glColor(1,0,0)
        obj1.trazar()
        
        glColor(0,0,1)
        obj2.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()