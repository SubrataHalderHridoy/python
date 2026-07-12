## Celsisus to Fahrenheit

# c/5=(f-32)/9

# def f_to_c(f):
#     return 5*(f-32)/9
# f=int(input(f"Enter temperature in F: "))
# print(f"{f_to_c(f)}  °C")



def f_to_c(f):
    return 5*(f-32)/9
f=int(input(f"Enter temperature in F: "))
c=f_to_c(f)
print(f"{round(c, 2)}°C") # decimal 2 number
