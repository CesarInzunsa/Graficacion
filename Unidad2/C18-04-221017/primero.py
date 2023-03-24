import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

#Variables globales
tam_Ventana = 800
tam_Cuadrante = 250

'''
def trazarEjes(tam):
	glBegin(GL_LINES)
	glVertex2f(-tam, 0)
	glVertex2f(tam,0)
	glVertex2f(0, -tam)
	glVertex2f(0, tam)
	glEnd()
'''

class Cuadrado():

	def __init__(self, lado):
		self.v1 = [-lado/2, lado/2]
		self.v2 = [lado/2, lado/2]
		self.v3 = [lado/2, -lado/2]
		self.v4 = [-lado/2, -lado/2]

	def trazar(self):

		glBegin(GL_LINE_LOOP)
		glVertex2fv(self.v1)
		glVertex2fv(self.v2)
		glVertex2fv(self.v3)
		glVertex2fv(self.v4)
		glEnd()

def framebuffer_size_callback(window, width, height):
    print(width,height)
    glViewport(0,0, width, height)

def main():

    #Si no se pudo iniciar el glfw, termina el programa
    if not glfw.init():
        return

    #Crear una ventana
    ventana = glfw.create_window(tam_Ventana, tam_Ventana, "kmkkm", None, None)
    
    #Si no se puede crear la ventana, termina el programa
    if not ventana:
        glfw.terminate()
        return

    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
    
    glfw.make_context_current(ventana)

    gluOrtho2D(-tam_Cuadrante,tam_Cuadrante, -tam_Cuadrante, tam_Cuadrante) #Proyeccion

    glClearColor(0,0,0,0)

    c = Cuadrado(200)

    #Mientras no haya cerrado la ventana, la ventana seguira existiendo
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT)
        #Aqui !!

        glColor(1,0,0)
        
        glBegin(GL_POINTS)

        #trazarEjes(tam_Cuadrante)

        glEnd()

        glColor(1,1,1)
        #Y despues de crear el objeto podemos mandar a llamar la clase

        c.trazar()

        glfw.swap_buffers(ventana)

    #Termina el programa
    glfw.terminate()

if __name__ == "__main__":
    main()