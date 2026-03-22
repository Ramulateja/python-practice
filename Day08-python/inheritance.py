class parent:
    def speak(self):
        print("hello")
class child(parent):
    pass
d1=child()
d1.speak()



class hello:
    def __init__(self,name):
        self.name=name
p1=hello("tej")
print(p1.name)