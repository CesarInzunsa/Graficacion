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
tam_Ventana = 600
tam_Cuadrante = 10

class Circunferencia:
    def __init__(self,r,n=20):
        self.vertices = np.array([[r*np.cos(t),r*np.sin(t),0] for t in np.linspace(0,2*np.pi,n)],dtype=np.float32)
    
    def transformar(self, M):
       i = 0
       while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                          [self.vertices[i][1]],
                          [self.vertices[i][2]],[1]], dtype=np.float32)

            Pp= np.dot(M,P)

            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            self.vertices[i][2] = Pp[2][0]
            i += 1

    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()

class Cubo:

    def __init__(self):
        self.vertices = np.array([[2,2,2],
                                  [2,-2,2],
                                  [2,2,-2],
                                  [2,-2,-2],
                                  [-2,2,-2],
                                  [-2,-2,-2],
                                  [-2,2,2],
                                  [-2,-2,2],
                                  [2,2,2],
                                  [2,-2,2]], dtype = np.float32)
        
    def trazar(self):
        glBegin(GL_QUAD_STRIP)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()
        
    def transformar(self, M):
       i = 0
       while i < len(self.vertices):
            P = np.array([[self.vertices[i][0]],
                          [self.vertices[i][1]],
                          [self.vertices[i][2]],
                          [1]], dtype=np.float32)

            Pp = np.dot(M,P)

            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            self.vertices[i][2] = Pp[2][0]
            i += 1
            
    def trasladar(self, tx,ty,tz):
    
       T = np.array([[1,0,0,tx],
                     [0,1,0,ty],
                     [0,0,1,tz],
                     [0,0,0,1]], dtype = np.float32)
       i = 0
       self.transformar(T)
            
    #Con respecto al 0,0       
    def escalar(self, sx,sy,sz):
    
       S = np.array([[sx,0,0,0],
                     [0,sy,0,0],
                     [0,0,sz,0],
                     [0,0,0,1]],dtype = np.float32)
       self.transformar(S) 
            
    def rotarZ(self, t):
        t = np.radians(t)
        Rz = np.array([[np.cos(t),-np.sin(t),0,0],
                       [np.sin(t), np.cos(t),0,0],
                       [0,0,1,0],
                       [0,0,0,1]], dtype=np.float32)
        self.transformar(Rz)

    def rotarX(self, t):
        t = np.radians(t)
        Rx = np.array([[1,0,0,0],
                       [0,np.cos(t),-np.sin(t),0],
                       [0,np.sin(t), np.cos(t),0],
                       [0,0,0,1]], dtype=np.float32)
        self.transformar(Rx)

    def rotarY(self, t):
        t = np.radians(t)
        Ry = np.array([[np.cos(t),0,np.sin(t),0],
                       [0,1,0,0],
                       [-np.sin(t),0,np.cos(t),0],
                       [0,0,0,1]], dtype=np.float32)
        self.transformar(Ry)

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

    glClearColor(1,1,1,0) #RGB

    glViewport(0,0,tam_Ventana,tam_Ventana)

    #Proyeccion 3D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-12,12,-12,12,1,25) #(left,right,buttom,top,near,far) Paralelo
    glFrustum(-3,3,-3,3,2,25) #perspectiva
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5,6,8,0,0,0,0,1,0) #(eyeX,eyeY,eyeZ,centerX,centerY,centerZ,upX,upY,upZ)
    
    #cir = Circunferencia(6,30)
    cubo = Cubo()
            
    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #ACTIVAR EL 3D
        glEnable(GL_DEPTH_TEST) #PARA DIBUJAR LO QUE ESTA OCULTO PARA LA VISTA
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE) #RELLENO DEL OBJETO CON  GL_FILL, GL_LINE
  
        trazarEjes() #Funcion para trazar los ejes

        glColor(0,0,0)
        cubo.trazar()
        time.sleep(0.1)
        
        cubo.trasladar(-2,-2,2)
        cubo.rotarX(5)
        cubo.trasladar(2,2,-2)

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()