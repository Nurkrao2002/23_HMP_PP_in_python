'''
instance method: It will act on instance variables
accessor methods: They read the instance variables. They do not modify.
They are used with the help of getter() method. --> get method
mutator methods: They not only read but can also modify the instance variables.
 They can be used with the help of setter() method. --> set method
 '''
class Admission:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
a=Admission()
a.setname('Python')
print("My Name is",a.getname()) 