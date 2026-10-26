# Inheritance (kalıtım): Miras alma 

# Person => name, lastname , age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastname = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')



class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('student created')
    
    # override
    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch


    def who_am_i(self):
        print(f'I am a {self.branch} teacher')











p1 = Person('Talha','Kalfa')
s1 = Student('Çağan', 'Kalfa', 1453)
t1 = Teacher('Nurettin','kalfa','Math')

t1.who_am_i()

print(p1.firstName + ' ' + p1.lastname)
print(s1.firstName + ' ' + s1.lastname + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
