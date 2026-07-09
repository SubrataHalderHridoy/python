a=10
b=5
print(type(a/5))


a=5+10.0
print(type(a))

# type casting
a=int(5+10.0) #explicit type casting
a1=5+10.0   #implicit type casting
print(a, type(a))
print(a1, type(a1))

b=float(7)  #explicit type casting
b1=7        #implicit type casting  
print(b, type(b))
print(b1, type(b1))

c=str(10)  #explicit type casting
c1="10"    #implicit type casting
print(c, type(c))
print(c1, type(c1))


d=bool(1)  #explicit type casting
print(d, type(d))

d=bool(0)  #explicit type casting
print(d, type(d))