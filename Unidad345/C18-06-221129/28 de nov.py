import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

# variables globales
tam_ventana = 800
tam_cuadrante = 10

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
                                 [2,-2,2],],dtype = np.float32)
        
    def trazar(self):
        glBegin(GL_QUAD_STRIP)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()
        
    def transformar(self, M):
       i = 0
       while i < len(self.vertices):
            P = np.matrix([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [self.vertices[i][2]],[1]], dtype=np.float32)

            Pp= M*P

            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            self.vertices[i][2] = Pp[2][0]
            i += 1
            
    def trasladar(self, tx,ty,tz):
    
       T = np.array([[1,0,0,tx],
                     [0,1,0,ty],
                     [0,0,1,tz],
                     [0,0,0,1]],dtype = np.float32)
       i = 0
       while i < len(self.vertices):
            P = np.matrix([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [self.vertices[i][2]],[1]], dtype=np.float32)

            Pp= T*P

            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            self.vertices[i][2] = Pp[2][0]
            i += 1
            
    def escalar(self, sx,sy,sz):
    
       S = np.array([[sx,0,0,0],
                     [0,sy,0,0],
                     [0,0,sz,0],
                     [0,0,0,1]],dtype = np.float32)
       i = 0
       while i < len(self.vertices):
            P = np.matrix([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [self.vertices[i][2]],[1]], dtype=np.float32)

            Pp= S*P

            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            self.vertices[i][2] = Pp[2][0]
            i += 1    
            
    def rotarz(self,t):
        t=np.radians(t)
        Rz = np.array([[np.cos(t),-np.sin(t),0,0],
                      [np.sin(t),np.cos(t),0,0],
                      [0,0,1,0],
                      [0,0,0,1]], dtype=np.float32)

        i=0
        while i < len(self.vertices):
                P = np.array([[self.vertices[i][0]],
                            [self.vertices[i][1]],
                            [self.vertices[i][2]],[1]], dtype=np.float32)

                Pp= np.dot(Rz,P)

                self.vertices[i][0] = Pp[0][0]
                self.vertices[i][1] = Pp[1][0]
                self.vertices[i][2] = Pp[2][0]
                i += 1

    def rotarx(self,t):
        t=np.radians(t)
        Rz = np.array([[1,0,0,0],
                      [0,np.cos(t),-np.sin(t),0],
                      [0,np.sin(t),np.cos(t),0],
                      [0,0,0,1]], dtype=np.float32)

        i=0
        while i < len(self.vertices):
                P = np.array([[self.vertices[i][0]],
                            [self.vertices[i][1]],
                            [self.vertices[i][2]],[1]], dtype=np.float32)

                Pp= np.dot(Rz,P)

                self.vertices[i][0] = Pp[0][0]
                self.vertices[i][1] = Pp[1][0]
                self.vertices[i][2] = Pp[2][0]
                i += 1

    def rotary(self,t):
        t=np.radians(t)
        Ry = np.array([[np.cos(t),0,np.sin(t),0],
                      [0,1,0,0],
                      [-np.sin(t),0,np.cos(t),0],
                      [0,0,0,1]], dtype=np.float32)

        i=0
        while i < len(self.vertices):
                P = np.array([[self.vertices[i][0]],
                            [self.vertices[i][1]],
                            [self.vertices[i][2]],[1]], dtype=np.float32)

                Pp= np.dot(Ry,P)

                self.vertices[i][0] = Pp[0][0]
                self.vertices[i][1] = Pp[1][0]
                self.vertices[i][2] = Pp[2][0]
                i += 1
#-------------------------



class Circunferencia:
    def __init__(self,r,n=20):
        self.vertices = np.array([[r*np.cos(t),r*np.sin(t),0] for t in np.linspace(0,2*np.pi,n)],dtype=np.float32)
    
    def transformar(self, M):
       i = 0
       while i < len(self.vertices):
            P = np.matrix([[self.vertices[i][0]],
                           [self.vertices[i][1]],
                           [self.vertices[i][2]],[1]], dtype=np.float32)

            Pp= M*P

            self.vertices[i][0] = Pp[0][0]
            self.vertices[i][1] = Pp[1][0]
            self.vertices[i][2] = Pp[2][0]
            i += 1

    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()


def framebuffer_size_callback(windiw,width,heigh):
    glViewport(0,0,width,heigh)

def main():
    if not glfw.init():
        return
    
    ventana = glfw.create_window(tam_ventana,tam_ventana,"19400584",None,None)

    if not ventana:
        glfw.terminate()
        return
    glfw.set_framebuffer_size_callback(ventana,framebuffer_size_callback)

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0) #RGB

    glViewport(0,0,tam_ventana,tam_ventana)

    #Proyeccion 3D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12,12,-12,12,1,25) #(left,right,buttom,top,near,far) Paralelo
    #glFrustum(-3,3,-3,3,2,25)
    
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    gluLookAt(5,5,8,0,0,0,0,1,0) #(eyeX,eyeY,eyeZ,centerX,centerY,centerZ,upX,upY,upZ)
    
    cir = Circunferencia(6,30)
    M = np.array([[1,0,0,0],
                  [0,0.9961946980917455,-0.08715574274765817,0],
                  [0,0.08715574274765817,0.9961946980917455,0],
                  [0,0,0,1]],dtype=np.float32)



    cubito = Cubo()
    

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        '''
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST) #Para no dibujar lo "oculto" a vista
        '''

        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor(1,0,0)#x
        glBegin(GL_LINES) 
        glVertex3f(-10,0,0)
        glVertex3f(10,0,0)
        glEnd()
        glColor(0,1,0)#y
        glBegin(GL_LINES) 
        glVertex3f(0,-10,0)
        glVertex3f(0,10,0)
        glEnd()
        glColor(0,0,1)#z
        glBegin(GL_LINES) 
        glVertex3f(0,0,-10)
        glVertex3f(0,0,10)
        glEnd()

        glColor(1,0,1)#x
        #cir.trazar()
        cubito.trazar()
        time.sleep(.1)
        cubito.transformar(M)
        #cir.transformar(M)
        
        #cubito.trasladar(0.5,0.5,1)
        #cubito.escalar(2,1,1)
        cubito.rotarz(5)

        glfw.swap_buffers(ventana)
        
    glfw.terminate()
    

if __name__ == "__main__":
    main()

