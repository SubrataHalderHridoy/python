class Employee():
    language="Python"
    salary=1200000

    def getInfo(self):
        print(f"The language is{self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")    


hridoy=Employee()
hridoy.getInfo()
hridoy.greet()