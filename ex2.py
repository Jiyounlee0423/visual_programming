class Human():
    def __init__(self, n):
        self.name = n
    
    def print_name(self):
        print(self.name)
        return self.name

a = Human('jiyoun-Lee')
a.print_name()
new_name = Human.print_name(a)

class Student(Human):
    def __init__(self):
        super().__init__('not defined')

b = Student()
b.print_name()

class Teacher(Human):
    def __init__(self, n):
        super().__init__(n)
    
    def print_name(self):
        print('teacher:', self.name)

c = Teacher('jiyoun_Lee')
c.print_name()