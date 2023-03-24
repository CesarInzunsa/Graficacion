#El metodo se llama DDA | el metodo del profe
#Algoritmo DDA
#Este algoritmo lo vamos a reutilizar cuando usemos el OpenGL
#No lo borres del futuro
def main():
    xi, yi = 0,0
    xf, yf = -10,10

    dx,dy = xf-xi, yf-yi

    if dx>=abs(dy):
        pasos = abs(dx)
    else:
        pasos = abs(dy)

    incx = dx / pasos
    incy = dy / pasos

    x, y = xi, yi
    i = 0
    while i <=pasos:
        print(round(x), round(y))
        x += incx
        y += incy
        i += 1

if __name__=="__main__":
    main()