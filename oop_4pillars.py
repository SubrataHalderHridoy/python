### ENCAPSULATION ###
#public
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name= name 
#         self.balance= balance

# acc1= BankAccount("Rahul kumar", 100_000)
# print(acc1.name, acc1.balance)



#protected
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name= name 
#         self._balance= balance  # protected

# acc1= BankAccount("Rahul kumar", 100_000)
# print(acc1.name, acc1._balance)





# private
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name= name 
#         self.__balance= balance # private - data mangling

#     def get_balance(self):
#         return self.__balance    
#     def set_balance(self, newBalance):
#         self.__balance = newBalance

# acc1= BankAccount("Rahul kumar", 100_000)
# #print(acc1.name, acc1.get_balance())

# acc1.set_balance(200_00000)
# print(acc1.name, acc1._BankAccount__balance)






### INHERITANCE ###

# class Employee:
#     start_time="10am"
#     end_time="6pm"
    
#     def change_time(self,new_end_time):
#         self.end_time=new_end_time
# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role=role


# t1=Teacher("Math")
# t1.change_time("5pm")
# print(t1.subject, t1.start_time, t1.end_time)


# staff1=AdminStaff("manager")
# print(staff1.role, staff1.start_time, staff1.end_time)




# multilevel inheritance

# class Employee:
#     start_time="10am"
#     end_time="6pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role=role

# class Account(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role) # parent class aer constructor kaa call
#         self.salary=salary

# acc1=Account(34_0000, "CA")
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)



#multiple inheritance
# class Teacher:
#     def __init__(self, salary):
#         self.salary=salary

# class Student:
#     def __init__(self, gpa):
#         self.gpa=gpa

# class TA(Teacher , Student):
#     def __init__(self, salary, gpa, name):
#         super().__init__(salary)
#         Student.__init__(self,gpa)
#         self.name=name

# ta1=TA(15_000, 9.3, "hridoy")
# print(ta1.name, ta1.gpa, ta1.salary)
            




### ABSTRACT CLASS ###
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass 

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")

# lion = Lion()
# lion.make_sound()

# cow=Cow()
# cow.make_sound()






### POLYMORPHISM ###

# class Employee:
#     def get_designation(self):
#         print("designed = Employee")

# class Teacher(Employee):
#     def get_designation(self): # function overriding
#         print("designation = Teacher")

# t1=Teacher()
# t1.get_designation()


class Teacher():
    def get_designation(self):
        print("designation = Teacher")

t1=Teacher()
t1.get_designation()

