import math

r = 10

def f(x):
    return round (math.sqrt(r**2 - x**2))

def main():
    x = 0

    while x <= r/math.sqrt(2):
        print(x, f(x))
        x += 1

if __name__=="__main__":
    main()