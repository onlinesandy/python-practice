class Parent():
    def __init__(self):
        print("Parent Class")
    def greeting(self):
        print("Hello g")

class child(Parent):
    def __init__(self):
        print("Child Class")
        super().__init__()
    
 
ch = child()
ch.greeting()

