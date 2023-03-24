xi,yi = 1,1
xf,yf = 10,9

dx = xf - xi
dy = yf - yi

xk,yk = xi,yi

if dx >= dy:
    while xk <= xf:
       print(xk,",",yk)
       DPk = 2*xk*dy + 2*dy - 2*yk*dx + 2*yi*dx - 2*xi*dy - dx
       if DPk >= 0:
           yk += 1
       xk += 1
else:
    while yk <= yf:
        print(xk,",",yk)
        DPk = 2*yk*dx + 2*dx - 2*xk*dy + 2*xi*dy - 2*yi*dx - dy
        if DPk >= 0:
            xk += 1
        yk += 1