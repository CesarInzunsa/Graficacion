import glfw
from OpenGL.GL import *

class Circunferencia:

    #Constructor
    def __init__(self, r):
        self.radio = r

    def circunferenciaBresenham(self):

        self.radio = round(self.radio)

        x = 0
        y = self.radio
        DPK = 3-2*self.radio

        glBegin(GL_POINTS)

        while x <= y:
            glVertex2f(round(x)/250, round(y)/250)
            glVertex2f(round(y)/250, round(x)/250)
            glVertex2f(round(y)/250, round(-x)/250)
            glVertex2f(round(x)/250, round(-y)/250)
            glVertex2f(round(-x)/250, round(-y)/250)
            glVertex2f(round(-y)/250, round(-x)/250)
            glVertex2f(round(-y)/250, round(x)/250)
            glVertex2f(round(-x)/250, round(y)/250)
            
            if DPK >= 0:
                DPK += 4*(x-y) + 10
                y -= 1
            else:
                DPK += 4*x + 6    
            x += 1
        
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
        r1 = Circunferencia(100)
        r2 = Circunferencia(150)
        r3 = Circunferencia(200)

        for i in range(-250,250):
            glVertex2f(i/250,0)
            glVertex2f(0,i/250)
            i += 1

        glEnd()

        glColor(1,1,1)
        #Y despues de crear el objeto podemos mandar a llamar la clase
        r1.circunferenciaBresenham()

        glColor(0,1,0)
        r2.circunferenciaBresenham()

        glColor(1,1,1)
        r3.circunferenciaBresenham()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()

#Usar el algoritmo de la circunferencia para que sea automatico