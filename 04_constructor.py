class Employee():
    language="Python"
    salary=1200000

    def __init__(self , name , salary , language):  # dunder method ,, autometically call
        self.name=name
        self.language=language
        self.salary=salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is{self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(): # object aer dorker naii
        print("Good morning")    


hridoy=Employee("Hridoy", "python", 150000000)
print(hridoy.name, hridoy.language, hridoy.salary)