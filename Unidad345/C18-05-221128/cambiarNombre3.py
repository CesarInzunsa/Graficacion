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

class Circunferencia:
    def __init__(self, r, v):
        
        self.vertices = np.array([[r*np.cos(t), r*np.sin(t), 0] for t in np.linspace(0,2*np.pi, v)], dtype=np.float32)
        
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()
    
    def transformar(self,M): #4x4
        i = 0
        while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                          [self.vertices[i][1]],
                          [self.vertices[i][2]],
                          [1]],dtype=np.float32)
            Pp = np.dot(M,P)
            self.vertices[i][0] = Pp[0][0] #x
            self.vertices[i][1] = Pp[1][0] #y
            self.vertices[i][2] = Pp[2][0] #z
            i += 1
            
    def rotarX(self):
        m = np.array([[1,0,0,0],
                      [0,np.cos(5),0-np.sin(5),0],
                      [0,np.sin(5),np.cos(5),0],
                      [0,0,0,1]], dtype = np.float32)
    
        self.transformar(m)

def trazarEjes():
    glBegin(GL_LINES)
    
    glColor(1,0,0)
    glVertex3f(-tam_Cuadrante, 0,0)
    glVertex3f(tam_Cuadrante, 0,0)
    
    glColor(0,1,0)
    
    glVertex3f(0, -tam_Cuadrante,0)
    glVertex3f(0, tam_Cuadrante,0)
    
    glColor(0,0,1)
    
    glVertex3f(0,0, -tam_Cuadrante)
    glVertex3f(0,0, tam_Cuadrante)
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

    #gluOrtho2D(-tam_Cuadrante,tam_Cuadrante, -tam_Cuadrante, tam_Cuadrante) #Matriz de proyeccion 2D
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10,-10,10,1,30)#paralelo
    #glFrustum(-3,3,-3,3,1,10)#Perspectiva

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5,5,8,0,0,0,0,1,0)
    
    glClearColor(0,0,0,0)

    #objetos
    c = Circunferencia(6, 30)
    
    m = np.array([[1,0,0,0],
                      [0,np.cos(5),0-np.sin(5),0],
                      [0,np.sin(5),np.cos(5),0],
                      [0,0,0,1]], dtype = np.float32)
    
    
            
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
  
        trazarEjes()

        glColor(1,0,1)
        glVertex3f(2,4,5)
        c.trazar()
        time.sleep(100)
        c.transformar(m)


        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()