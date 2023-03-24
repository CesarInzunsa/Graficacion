#Funciona cuando |dx| >= |dy| cuando dx negativo
def f(y, yi, xi, yf, xf):
    return xi + (y-yi)*(xf-xi)/(yf-yi)

def main():
    xi, yi = 0,0
    xf, yf = -3,10

    dy = yf - yi
    dx = xf - xi

    print("dy = ", dy)
    print("dx = ", dx)

    if (abs(dx) >= abs(dy)):

        x = xi
        while(x>=xf):
            print(x,round(f(x, xi, yi, xf, yf)))
            x -= 1
    else:
        print("No funciona")

if __name__ == "__main__":
    main()

#solo este y el dos estan bien

'''
cuando dx >= dy y positivo usamos y = f(x)
si dx es positivo usamos x++
sino x--



la tarea es unir los cuatro trabajos
'''