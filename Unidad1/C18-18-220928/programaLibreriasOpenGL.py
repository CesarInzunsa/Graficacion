import glfw
from OpenGL.GL import *

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
    
    glfw.make_context_current(ventana)

    #RGB
    glClearColor(0,0,0,0)

    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,0,0)
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2i(0,0)
        glVertex2i(1,1)
        glVertex2i(0,1)
        glVertex2i(-1,0)
        glVertex2f(0.5,0.5)  #Restringido el uso de la f, hasta nuevo aviso.
        glEnd()


        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()