#classes in python
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.age = age
    def greeting(self):
        print("Goodmorning " +self.fname +" "+self.lname)
    def getAge(self):
        return self.age
#inheitance
class student(Person):
    def __init__(self, fname, lname,regno):
        super().__init__(fname, lname)
        self.regNumber = regno
    def welcome(self):
        print("Welcome ",self.fname,self.lname,"student:",self.regNumber)
student1 = student("josh","kefa",998880).welcome()

print(student1)