import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

class Circunferencia:

    #Constructor
    def __init__(self, r):
        self.radio = round(r)

    def circunferenciaBresenham(self):

        self.radio = round(self.radio)

        x = 0
        y = self.radio
        DPK = 3-2*self.radio

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
                DPK += 4*(x-y) + 10
                y -= 1
            else:
                DPK += 4*x + 6    
            x += 1
        
        glEnd()

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


class Cuadrado():
    def __init__(self, lado):
        lado = round(lado)
        self.r1 = Recta(-lado/2, lado/2, lado/2, lado/2) #arriba
        self.r2 = Recta(-lado/2, -lado/2, lado/2, -lado/2) #abajo
        self.r3 = Recta(-lado/2, -lado/2, -lado/2, lado/2) #izquierda
        self.r4 = Recta(lado/2, -lado/2, lado/2, lado/2)  #derecha

    def trazar(self):
        self.r1.trazar()
        self.r2.trazar()
        self.r3.trazar()
        self.r4.trazar()

        #para el cuadrado inscrito se recibe como parametro el radio
        #con el radio se obtiene los lados del cuadrado con la hipotenusa

        #cuadro inscrito
        #triangulo inscrito

class CuadradoInscrito():
    #Constructor
    def __init__(self, radio):
        lado = 1.41421356237*radio
        self.circulo = Circunferencia(radio)
        self.cuadrad = Cuadrado(lado)

    def trazar(self):
        self.circulo.circunferenciaBresenham()
        self.cuadrad.trazar()
        

def framebuffer_size_callback(window, width, height):
    print(width,height)
    glViewport(0,0, width, height)

def cursor_pos_callback(window, width, height):
    print(width-250, 250-height)

def main():

    #Si no se pudo iniciar el glfw, termina el programa
    if not glfw.init():
        return

    #Crear una ventana
    ventana = glfw.create_window(500, 500, "Prueba GLFW", None, None)
    
    #Si no se puede crear la ventana, termina el programa
    if not ventana:
        glfw.terminate()
        return

    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
    
    glfw.set_cursor_pos_callback(ventana, cursor_pos_callback)
    
    glfw.make_context_current(ventana)

    gluOrtho2D(-250,250, -250, 250) #Proyeccion

    glClearColor(0,0,0,0)

    c1 = CuadradoInscrito(200)

    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,0,0)
        
        glBegin(GL_POINTS)

        #Primero creamos el objeto
        

        for i in range(-250,250):
            glVertex2i(i,0)
            glVertex2i(0,i)
            i += 1

        glEnd()

        glColor(1,1,1)
        #Y despues de crear el objeto podemos mandar a llamar la clase

        #c1.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()