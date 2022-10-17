


def simplecalc(x,y,z):
    if z==1:
        print(x+y)
    elif z==2:
        print(x-y)
    elif z==3:
        print(x*y)
    else:
        print(x/y)
print("Simple Calculator")
a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
print("Enter the function you want to perform")
c=int(input("1:add,2:subtract,3:multiply,4:divide"))
simplecalc(a,b,c)

    
