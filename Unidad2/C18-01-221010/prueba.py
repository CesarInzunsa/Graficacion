import glfw
from OpenGL.GL import *

#El metodo se llama DDA | el metodo del profe
#Algoritmo DDA
#Este algoritmo lo vamos a reutilizar cuando usemos el OpenGL
#No lo borres Cesar del futuro
def dda(xi, yi, xf, yf):

    dx,dy = xf-xi, yf-yi

    if abs(dx) >= abs(dy):
        pasos = abs(dx)
    else:
        pasos = abs(dy)

    incx = dx / pasos
    incy = dy / pasos

    x, y = xi, yi

    glBegin(GL_POINTS)

    i = 0

    while i <= pasos:
        glVertex2f(round(x)/250, round(y)/250)
        x += incx
        y += incy
        i += 1
    glEnd()

def framebuffer_size_callback(window, width, height):
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
        x = -250
        while(x<=250):
            glVertex2f(x/250,0)  #Restringido el uso de la f, hasta nuevo aviso.
            x += 1

        y = -250
        while(y<=250):
            glVertex2f(0,y/250)  #Restringido el uso de la f, hasta nuevo aviso.
            y += 1

        glEnd()

        glColor(1,1,1)
        dda(-100,-100,100,100)


        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()

#Usar el algoritmo de la circunferencia para que sea automatico