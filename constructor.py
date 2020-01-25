class employee():
    """
        Here is Class Documentation
        """
        
    def __init__(self,name,age):
        """
        Here is constroctor Documentation
        """
        self.name = name
        self.age = age

emp1 = employee("s",32)

print(emp1.__dict__)
print(emp1.__doc__)
print(emp1.__init__.__doc__)
