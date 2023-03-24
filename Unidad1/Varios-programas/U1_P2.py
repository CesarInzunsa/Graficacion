def f(x, xi, yi, xf, yf):
    return yi + (x-xi)*(yf-yi)/(xf-xi)

#Cuerpo del programa
def main():
    xi, yi = 0,0
    xf, yf = 10,3

    dy = yf - yi
    dx = xf - xi

    if (dx >= dy):
        m = dy/dx

        print("dy = ", dy)
        print("dx = ", dx)
        print("m = ", m)

        x = xi
        while(x<=xf):
            print(x, round(f(x, xi, yi, xf, yf)))
            x += 1
    else:
        print("No funciona")

if __name__ == "__main__":
    main()

    #Funciona cuando dx >= dy


    #Prox clase, cuando el if dx < dy;
    #despejar al reves la ecuacion.
    #Recordar que hay diferenciales negativos y positivos.