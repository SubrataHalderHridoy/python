class Employee():
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.iname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.iname=value.split(" ")[1]


e= Employee()
e.a=45

e.name="Hridoy Halder"
print(e.name)

e.show()