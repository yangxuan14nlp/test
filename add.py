def add(x, y):
    return x+y

if __name__ == "__main__":
    while(1):
        x,y = eval(input('pls input x, y : '))
        print('x+y = ', add(x,y))