import glfw
from OpenGL.GL import *

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
            glVertex2f(round(x)/250, round(y)/250)
            x += incx
            y += incy
            i += 1
        glEnd()

def framebuffer_size_callback(window, width, height):
    print(width,height)
    glViewport(0,0, width, height)


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
    
    glfw.make_context_current(ventana)

    #RGB
    glClearColor(0,0,0,0)

    x, y = 100,100

    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,0,0)
        
        glBegin(GL_POINTS)

        #Primero creamos el objeto
        r1 = Recta(-200,0,200,100)
        r2 = Recta(-200,0,200,-100)
        r3 = Recta(200,-100,200,100)

        for i in range(-250,250):
            glVertex2f(i/250,0)
            glVertex2f(0,i/250)
            i += 1

        glEnd()

        glColor(1,1,1)
        #Y despues de crear el objeto podemos mandar a llamar la clase
        r1.trazar()
        r2.trazar()
        r3.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()

#Usar el algoritmo de la circunferencia para que sea automatico