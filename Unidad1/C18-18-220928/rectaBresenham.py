xF = [0, 3, 10, 10, 10, 10, 10, 3, 0, -3, -10, -10, -10, -10, -10, -3]
yF = [10, 10, 10, 3, 0, -3, -10, -10, -10, -10, -10, -3, 0, 3, 10, 10]

def main():
    def vuelta(c):
        #Caso 3,13,5,11
        #Caso 1,7,9,15
        #Caso 0,4,8,12
        #Caso 2,6,10,14
        xi, yi = 0, 0
        x, y = xi, yi
        print("Caso ",c)

        xf, yf = xF[c],yF[c]
        dx, dy = xf-xi, yf-yi
        signo_dx = dx>0
        signo_dy = dy>0
        diferencia = 0
        if (abs(dx)==abs(dy)):
            while((x>=xf,x<=xf)[signo_dx]):
                print(x,y)
                x+= (-1,1)[signo_dx]
                y+= (-1,1)[signo_dy]
        elif (abs(dx)>abs(dy)):
            while ((x>=xf,x<=xf)[signo_dx]):
                print(x,y)
                diferencia = (2*((abs(dy)*(x+1-xi)+dx*(yi-abs(y))))-dx)*(-1,1)[signo_dx]
                y = (y,y+(-1,1)[signo_dy])[diferencia>=0]
                x+=(-1,1)[signo_dx]
        else:
            while ((y>=yf,y<=yf)[signo_dy]):
                print(x,y)
                diferencia = (2*((abs(dx)*(y+1-yi)+dy*(xi-abs(x))))-dy)*(-1,1)[signo_dy]
                x = (x,x+(-1,1)[signo_dx])[diferencia>=0]
                y+=(-1,1)[signo_dy]

    for i in range(0,16):
        vuelta(i)
if __name__ == "__main__":
    main()