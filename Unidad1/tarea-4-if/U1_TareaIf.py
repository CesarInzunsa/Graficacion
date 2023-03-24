def f1(x, xi, yi, xf, yf):
    return yi + (x-xi)*(yf-yi)/(xf-xi)

def f2(y, xi, yi, xf, yf):
    return xi + (y-yi)*(xf-xi)/(yf-yi)

###############################################

def caso1(x, xi, yi, xf, yf):
    print("CASO UNO")
    while(x <= xf):
        print(x, round(f1(x, xi, yi, xf, yf)))
        x += 1
    
def caso2(x, xi, yi, xf, yf):
    print("CASO DOS")
    while(x >= xf):
        print(x, round(f1(x, xi, yi, xf, yf)))
        x -= 1

def caso3(y, xi, yi, xf, yf):
    print("CASO TRES")
    while(y <= yf):
        print(round(f2(y, xi, yi, xf, yf)), y)
        y += 1

def caso4(y, xi, yi, xf, yf):
    print("CASO CUATRO")
    while(y >= yf):
        print(round(f2(y, xi, yi, xf, yf)), y)
        y -= 1

def main():
    xi, yi = 0,0
    xf, yf = 3,10

    dy = yf - yi
    dx = xf - xi

    print("dy = ", dy)
    print("dx = ", dx)

    if (abs(dx) >= abs(dy)):
        #Usamos la formula y = f(x)
        x = xi
        if (dx >= 0):
            #Caso uno
            caso1(x, xi, yi, xf, yf)
        else:
            #Quiere decir que dx < 0
            #Caso dos
            caso2(x, xi, yi, xf, yf)
    #Entra cuando dx < dy
    else:
        y = yi
        #Usamos la formula x = f(y)
        if (dy >= 0):
            #Caso tres
            caso3(y, xi, yi, xf, yf)
        else:
            #Quiere decir que dy < 0
            #Caso cuatro
            caso4(y, xi, yi, xf, yf)
    

if __name__ == "__main__":
    main()