# Greatest 3 number

a= 14
b=45
c=34

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    

print(greatest(a,b,c))    