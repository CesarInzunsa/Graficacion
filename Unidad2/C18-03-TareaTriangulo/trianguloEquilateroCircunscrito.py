#Librerias
import math
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

#Clase que permite dibujar en pantalla una linea recta
class Recta:
    #Constructor
    def __init__(self, xi, yi, xf, yf):
        self.xi = round(xi)
        self.yi = round(yi)
        self.xf = round(xf)
        self.yf = round(yf)

    def trazar(self):

        dx = self.xf - self.xi
        dy = self.yf - self.yi

        if abs(dx) >= abs(dy):
            pasos = abs(dx)
        else:
            pasos = abs(dy)

        incx = dx / pasos
        incy = dy / pasos

        x = self.xi
        y = self.yi

        glBegin(GL_POINTS)

        i = 0

        while i <= pasos:
            glVertex2i(round(x), round(y))
            x += incx
            y += incy
            i += 1

        glEnd()

#Clase que permite dibujar en pantalla una circunferencia
class Circunferencia:
    #Constructor
    def __init__(self, radio):
        self.radio = round(radio)

    def trazar(self):

        self.radio = round(self.radio)

        x = 0
        y = self.radio
        DPK = 3 - 2 * self.radio

        glBegin(GL_POINTS)

        while x <= y:
            glVertex2i(round(x), round(y))
            glVertex2i(round(y), round(x))
            glVertex2i(round(y), round(-x))
            glVertex2i(round(x), round(-y))
            glVertex2i(round(-x), round(-y))
            glVertex2i(round(-y), round(-x))
            glVertex2i(round(-y), round(x))
            glVertex2i(round(-x), round(y))
            
            if DPK >= 0:
                DPK += 4 * (x - y) + 10
                y -= 1
            else:
                DPK += 4 * x + 6    
            x += 1
        
        glEnd()

#Clase que permite dibujar en pantalla un triangulo equilatero
class TrianguloEquilatero:

    #Constructor
    def __init__(self,lado):
        self.lado = round(lado)
        
        self.radio = round(lado/math.sqrt(3)) #lado entre raiz de 3

        self.apotema = round(math.sqrt(3)/6*lado) #raiz de 3 entre 6 por el lado
        
        self.lado1 = Recta(0,self.radio,-lado/2,-self.apotema)
        self.lado2 = Recta(0,self.radio,lado/2,-self.apotema)
        self.lado3 = Recta(-lado/2,-self.apotema,lado/2,-self.apotema)

    def trazar(self):
        self.lado1.trazar()
        self.lado2.trazar()
        self.lado3.trazar()

#Clase que permite dibujar en pantalla un triangulo equilatero inscrito con solo el radio
class TrianguloEquilateroCircunscrito:

    #Constructor
    def __init__(self,radio):

        self.radio = round(radio)

        self.lado = round(2*1.7320508075688772*radio) #2 por raiz de 3 por el radio

        self.t = TrianguloEquilatero(self.lado)
        self.c = Circunferencia(radio)

    def trazar(self):
        self.t.trazar()
        self.c.trazar()

def framebuffer_size_callback(window, width, height):
    glViewport(0,0, width, height)

#Funcion principal
def main():
    
    if not glfw.init():
        return

    ventana = glfw.create_window(801, 801, "Triangulo Equilatero Circunscrito", None, None)
    
    if not ventana:
        glfw.terminate()
        return

    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
    
    glfw.make_context_current(ventana)

    gluOrtho2D(-400,400,-400,400)

    glClearColor(0,0,0,0)

    TEI = TrianguloEquilateroCircunscrito(120)

    while not glfw.window_should_close(ventana):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glColor(1,1,1)

        glBegin(GL_POINTS)

        for i in range(-400,400):
            glVertex2i(i,0)
            glVertex2i(0,i)
            i += 1

        glEnd()

        glColor(1,1,1)

        TEI.trazar()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()