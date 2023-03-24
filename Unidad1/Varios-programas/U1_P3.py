#Funciona cuando |dy| >= |dx|
def fx(x, xi, yi, xf, yf):
    return yi + (x-xi)*(yf-yi)/(xf-xi)

#Funciona cuando |dx| >= |dy|
def fy(y, yi, xi, yf, xf):
    return xi + (y-yi)*(xf-xi)/(yf-yi)

def main():
    xi, yi = 0,0
    xf, yf = -3,10

    dy = yf - yi
    dx = xf - xi

    print("dy = ", dy)
    print("dx = ", dx)

    if (abs(dx) <= abs(dy)):

        y = yi
        while(y<=yf):
            print(y, round(fy(y, xi, yi, xf, yf)))
            y += 1
    else:

        print("dy = ", dy)
        print("dx = ", dx)

        x = xi
        while(x<=xf):
            print(x, round(fx(x, xi, yi, xf, yf)))
            x += 1

if __name__ == "__main__":
    main()