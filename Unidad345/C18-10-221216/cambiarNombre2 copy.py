import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

#Prueba743

'''
    *** matriz del modelo: las transformaciones que le hacemos a la matriz (escalar, transladar, rotar)


    *** matriz de vista: La camara ayuda a pasar los parametros de que en cual lugar esta la camara
            coordenadas de la camara
            hacia donde ve la camara
            matriz para mover la camara

    *** matriz de proyeccion: una escala

    frustrum para perspctica gluperspective la ultima tiene ancho y alto
    ortogonal en paralelo

    gluLookAt para la camara los parametros posicionan la camara, los que tiene eye son la posicion de la camara, los segundos son a donde apunta, y lo☼ ultimos son para mover la camara sobre su eje.
'''

'''
    agarrar la pregunta 7, 8 y 9
    aro y piedra crear funciones y tambien en la del anillo
    y probarlo.
'''

#Variables globales
tam_Ventana = 600
tam_Cuadrante = 10

class Anillo:
    def __init__(self):
        self.aro = Aro()
        self.piedra = Piedra()
        
    def trazar(self):
        self.aro.trazar()
        self.piedra.trazar()

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

    #Matriz de Proyeccion 3D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12,12,-12,12,1,25) #(left,right,buttom,top,near,far) Paralelo
    #glFrustum(-3,3,-3,3,2,25)  #() Perspectiva

    xv,yv,zv = 5,5,8
    #xv,yv,zv = 5,0,0
    r = np.sqrt(xv**2+zv**2)
    t = np.arctan(zv/xv)
    
    tx = 0
    te = 0
    tzz = 0
    tk = 0

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
        glPushMatrix()
        '''
        glRotate(tzz,0,0,1)  #Paso 4
        glRotate(90,0,0,1)  #Paso 3
        glRotate(90,1,0,0)  #Paso 2
        glTranslate(0,-5,0) #Paso 1
        '''
        #m = np.array([1,0,0,0,0,1,0,0,0,0,1,0,0,-5,0,1], dtype = np.float32)
        #m = np.array([0,1,0,0,0,0,1,0,1,0,0,0,0,0,-5,1], dtype = np.float32)
        
        m2 = np.array([-np.sin(t), np.cos(t),0,0,0,0,1,0,np.cos(t),np.sin(t),0,0,0,0,-5,1])
        
        glMultMatrixf(m2) #Matriz compuesta
        anillo.trazar()
        glPopMatrix()
        

        time.sleep(0.05)
        #tx -= 0.05
        #te += 5
        #tzz += 5
        tk += np.radians(5)
        
        xv = r * np.sin(t)
        zv = r * np.cos(t)
        
        '''
        #Matriz de vista (la camara)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(xv,yv,zv,0,0,0,0,1,0) #(eyeX,eyeY,eyeZ,centerX,centerY,centerZ,upX,upY,upZ)

        t += np.radians(5)
        '''
        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()