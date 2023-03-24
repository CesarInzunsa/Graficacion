def main():
    radio = 9

    x = 0
    y = radio
    DPK = 3-2*radio

    while x <= y:
        print(x,y)
        print(y,x)
        print(y,-x)
        print(x,-y)
        print(-x,-y)
        print(-y,-x)
        print(-y,x)
        print(-x,y)
        
        if DPK >= 0:
            DPK += 4*(x-y) + 10
            y -= 1
        else:
            DPK += 4*x + 6    
        x += 1

            
if __name__ == "__main__":
    main()