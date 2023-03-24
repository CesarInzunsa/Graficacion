m=-0.98
b=1

def f(x):
    return m*x+b
if -1 <= m <= 1:
    x = 2
    while x<=12:
        print(x, round(f(x)))
        x+=1
else:
    print("No va a funcionar. m = ", m)


#Elegir el diferencial que cambia mas rapido como su variable de control