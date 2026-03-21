class person1:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("hello"+self.name)
p1=person1("tej")
p1.greet()