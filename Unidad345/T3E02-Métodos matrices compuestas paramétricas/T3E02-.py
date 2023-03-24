import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

#Prueba743

#Variables globales
tam_Ventana = 600
tam_Cuadrante = 10
            
class Aro:
    def __init__(self):
        puntos = []
        t = 0
        inc = 2*np.pi/15
        while t < 2*np.pi:
            puntos.append([4*np.cos(t),4*np.sin(t),-1])
            puntos.append([4*np.cos(t+inc),4*np.sin(t+inc),-1])
            puntos.append([4*np.cos(t),4*np.sin(t),1])
            puntos.append([4*np.cos(t+inc),4*np.sin(t+inc),1])
            puntos.append([3.5*np.cos(t),3.5*np.sin(t),1])
            puntos.append([3.5*np.cos(t+inc),3.5*np.sin(t+inc),1])
            puntos.append([3.5*np.cos(t),3.5*np.sin(t),-1])
            puntos.append([3.5*np.cos(t+inc),3.5*np.sin(t+inc),-1])
            puntos.append([4*np.cos(t),4*np.sin(t),-1])
            puntos.append([4*np.cos(t+inc),4*np.sin(t+inc),-1])
            t += inc
        self.vertices = np.array(puntos,dtype=np.float32)

    def trazar(self):
        glBegin(GL_QUAD_STRIP)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()
    
    def transformar(self,M):#coord. homogeneas 4X4
        i = 0
        while i < len(self.vertices):
            P =  np.array([[self.vertices[i][0]], #x
                           [self.vertices[i][1]], #y
                           [self.vertices[i][2]], #z
                           [1]],dtype=np.float32)
            Pp = np.dot(M,P)
            self.vertices[i][0] = Pp[0][0]#x'
            self.vertices[i][1] = Pp[1][0]#y'
            self.vertices[i][2] = Pp[2][0]#z'
            i += 1
        
    def escalamiento6(self, sx, sy, sz, xf, yf, zf):
        S = np.array([[sx,0,0,xf*(1-sx)],
                     [0,sy,0,yf*(1-sy)],
                     [0,0,sz,zf*(1-sz)],
                     [0,0,0,1]],dtype = np.float32)
        self.transformar(S)
    
    def rotacionZ7(self, t, xr, yr, zr):
        Rz = np.array([[np.cos(t), -np.sin(t), 0, -xr*np.cos(t) + yr*np.sin(t) + xr],
                      [np.sin(t), np.cos(t), 0, -xr*np.sin(t) - yr*np.cos(t) + yr],
                      [0,0,1,0],
                      [0,0,0,1]], dtype = np.float32)
        self.transformar(Rz)
    
    def rotacionX8(self, t, xr, yr, zr):
        Rx = np.array([[1,0,0,0],
                      [0, np.cos(t), -np.sin(t),  -yr*np.cos(t) + zr*np.sin(t) + yr],
                      [0,np.sin(t), np.cos(t), -yr*np.sin(t) - zr*np.cos(t) + zr],
                      [0,0,0,1]], dtype = np.float32)
        self.transformar(Rx)
    
    def rotacionY9(self, t, xr, yr, zr):
        Ry = np.array([[np.cos(t), 0, np.sin(t), -xr*np.cos(t) - zr*np.sin(t) + xr],
                      [0,1,0,0],
                      [-np.sin(t), 0, np.cos(t), xr*np.sin(t) - zr*np.cos(t) + zr],
                      [0,0,0,1]], dtype = np.float32)
        self.transformar(Ry)

class Piedra:
    def __init__(self):
        self.vertices = np.array([[0,5,0],
                                  [-0.5,4,1],
                                  [0.5,4,1],
                                  [0.5,4,-1],
                                  [-0.5,4,-1],
                                  [-0.5,4,1]],dtype=np.float32)
            
    def trazar(self):
        glBegin(GL_TRIANGLE_FAN)
        for vertice in self.vertices:
            glVertex3fv(vertice)
        glEnd()
    
    def transformar(self,M):#coord. homogeneas 4X4
        i = 0
        while i < len(self.vertices):
            P =  np.array([[self.vertices[i][0]], #x
                           [self.vertices[i][1]], #y
                           [self.vertices[i][2]], #z
                           [1]],dtype=np.float32)
            Pp = np.dot(M,P)
            self.vertices[i][0] = Pp[0][0]#x'
            self.vertices[i][1] = Pp[1][0]#y'
            self.vertices[i][2] = Pp[2][0]#z'
            i += 1
    
    def escalamiento6(self, sx, sy, sz, xf, yf, zf):
        S = np.array([[sx,0,0,xf*(1-sx)],
                     [0,sy,0,yf*(1-sy)],
                     [0,0,sz,zf*(1-sz)],
                     [0,0,0,1]],dtype = np.float32)
        self.transformar(S)
        
    def rotacionZ7(self, t, xr, yr, zr):
        Rz = np.array([[np.cos(t), -np.sin(t), 0, -xr*np.cos(t) + yr*np.sin(t) + xr],
                      [np.sin(t), np.cos(t), 0, -xr*np.sin(t) - yr*np.cos(t) + yr],
                      [0,0,1,0],
                      [0,0,0,1]], dtype = np.float32)
        self.transformar(Rz)
    
    def rotacionX8(self, t, xr, yr, zr):
        Rx = np.array([[1,0,0,0],
                      [0, np.cos(t), -np.sin(t),  -yr*np.cos(t) + zr*np.sin(t) + yr],
                      [0,np.sin(t), np.cos(t), -yr*np.sin(t) - zr*np.cos(t) + zr],
                      [0,0,0,1]], dtype = np.float32)
        self.transformar(Rx)
    
    def rotacionY9(self, t, xr, yr, zr):
        Ry = np.array([[np.cos(t), 0, np.sin(t), -xr*np.cos(t) - zr*np.sin(t) + xr],
                      [0,1,0,0],
                      [-np.sin(t), 0, np.cos(t), xr*np.sin(t) - zr*np.cos(t) + zr],
                      [0,0,0,1]], dtype = np.float32)
        self.transformar(Ry)
        
            
class Anillo:
    def __init__(self):
        self.aro = Aro()
        self.piedra = Piedra()
        
    def trazar(self):
        self.aro.trazar()
        self.piedra.trazar()
    
    def escalamiento6(self, sx, sy, sz, xf, yf, zf):
        self.aro.escalamiento6(sx, sy, sz, xf, yf, zf)
        self.piedra.escalamiento6(sx, sy, sz, xf, yf, zf)
    
    def rotacionZ7(self, t, xr, yr, zr):
        self.aro.rotacionZ7(t, xr, yr, zr)
        self.piedra.rotacionZ7(t, xr, yr, zr)
        
    def rotacionX8(self, t, xr, yr, zr):
        self.aro.rotacionX8(t, xr, yr, zr)
        self.piedra.rotacionX8(t, xr, yr, zr)
    
    def rotacionY9(self, t, xr, yr, zr):
        self.aro.rotacionY9(t, xr, yr, zr)
        self.piedra.rotacionY9(t, xr, yr, zr)

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

    #Matriz de Proyeccion 3D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12,12,-12,12,1,25) #(left,right,buttom,top,near,far) Paralelo
    #glFrustum(-3,3,-3,3,2,25)  #() Perspectiva

    xv = 5
    yv = 5
    zv = 8
    r = np.sqrt(xv**2+zv**2)
    t = np.arctan(zv/xv)

    #Matriz de vista (la camara)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(xv,yv,zv,0,0,0,0,1,0) #(eyeX,eyeY,eyeZ,centerX,centerY,centerZ,upX,upY,upZ)

    anillo = Anillo()

    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #ACTIVAR EL 3D
        glEnable(GL_DEPTH_TEST) #PARA DIBUJAR LO QUE ESTA OCULTO PARA LA VISTA
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE) #RELLENO DEL OBJETO CON  GL_FILL, GL_LINE

        trazarEjes() #Funcion para trazar los ejes
        
        glColor(0,0,0)
        anillo.trazar()
        
        #Aqui estan los metodos con los parametros que indicaba en la tarea
        #No sabia como entregarlo así que los deje todos ejecutandose
        anillo.escalamiento6(0.99, 0.99, 0.99, 0, 5, 0)
        anillo.rotacionZ7(5,0,5,0)
        anillo.rotacionX8(5,0,5,0)
        anillo.rotacionY9(5,0,5,0)
        
        #Para la animación
        time.sleep(0.05)
        xv = r * np.sin(t)
        zv = r * np.cos(t)
        t += np.radians(5)
        
        #Matriz de vista (la camara)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(xv,yv,zv,0,0,0,0,1,0) #(eyeX,eyeY,eyeZ,centerX,centerY,centerZ,upX,upY,upZ)
        
        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()