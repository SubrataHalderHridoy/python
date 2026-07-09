# class Student:
#     subject = "python"  #|
#     college = "ABC"     #| parameter
#     year = "4th year"   #|

# stu1=Student()
# stu2=Student()
# print(stu1.subject, stu1.college, stu1.year)
# print(stu2.subject, stu2.college, stu2.year)




#__init__ method
# class Student:
#     def __init__(self):
#         print("constuructor was called...")

# stu1=Student()
# stu2=Student()
# stu3=Student()
# stu4=Student()


# class Student:
#     def __init__(self, name, cgpa):
#         self.name=name 
#         self.cgpa=cgpa

# stu1=Student("Rahul", 9.0)
# stu2=Student("Hridoy", 8.9)
# stu3=Student("Shanta", 9.4)
# stu4=Student("Oishi", 8.5)
# print(stu1.name, stu1.cgpa)
# print(stu2.name, stu2.cgpa)
# print(stu3.name, stu3.cgpa)
# print(stu4.name, stu4.cgpa)




# called instance method----------------------
# class Student:                               #|
#     def __init__(self, name, cgpa):          #|
#         self.name=name  #                    #|
#         self.cgpa=cgpa  # instance attribute #|
#                                              #|
#     def get_cgpa(self): #stu1, stu2   <-------
#         return self.cgpa    

# stu1=Student("Rahul", 9.0)
# stu2=Student("Hridoy", 8.9)
# stu3=Student("Shanta", 9.4)

# print(stu1.get_cgpa())
# print(stu2.get_cgpa())
# print(stu3.get_cgpa())
# print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")




#Constructor ----> default & parameterized constructor
# class Student:
#     def __init__(self):   #default constructor
#             print("object is default constructor")
    
#     def __init__(self, name, cgpa):  #parameterized constructor
#          self.name=name
#          self.cgpa=cgpa




#Attribute ---->class & instance

# class Student:
#     college_name="apna college" #class

#     def __init__(self,name,cgpa):  
#         # instance
#         self.name=name
#         self.cgpa=cgpa

# stu1=Student("Rahul", 9.2)
# print(stu1.name)
# print(stu1.cgpa)
# print(Student.college_name)       





class Laptop:
    storage_type="ssd"

    def __init__(self, RAM, storage):
        self.RAM=RAM
        self.storage=storage
    
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):  #unique instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")    
    

    @staticmethod
    def calc_discount(price, discount):
        final_price=price-(discount*price/100)
        print(f"discount price = {final_price}")


l1=Laptop("64gb", "512")
# l2=Laptop("32gb", "256gb")
# l1.get_info()
# l1.get_storage_type()

l1.calc_discount(40_000, 10)



























