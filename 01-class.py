class Employee:
    name="hridoy"
    language="py" #This is a class attribute
    salary=120000000

hridoy=Employee()  # object intialition
hridoy.name="hridoy halder"   # This is a object attribute
print(hridoy.name, hridoy.language)

rohan=Employee()
print(rohan.salary, rohan.language)