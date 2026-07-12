class Employee:
    company="ITC"
    name="default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language="python"
    def printLanguages(self):
        print(f"out all the languages here is your language: {self.language}")

class Programmer(Employee, Coder):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a= Employee()
b=Programmer()

b.show()
b.showLanguage()
b.showLanguage()