import math

r = 10

def f(x):
    return round (math.sqrt(r**2 - x**2))

def main():
    x = 0
    pix = 0

    while x <= r/math.sqrt(2):
        y = f(x)

        print(x,y)
        print(-x,y)
        print(x,-y)
        print(-x,-y)
        print(y,x)
        print(-y,x)
        print(y,-x)
        print(-y,-x)

        x += 1

        pix += 8

    print("Numero total de pixeles necesarios para dibujar la circunferencia: ",pix)


if __name__=="__main__":
    main()