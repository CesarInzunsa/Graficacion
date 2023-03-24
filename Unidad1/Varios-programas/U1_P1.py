def f(x, xi, yi, xf, yf):
    return yi + (x-xi)*(yf-yi)/(xf-xi)

#Cuerpo del programa
def main():
    xi, yi = 2,3
    xf, yf = 8,6

    x = xi
    while(x<=xf):
        print(x, round(f(x, xi, yi, xf, yf)))
        x += 1

if __name__ == "__main__":
    main()