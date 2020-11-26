#1
def product(a, b):
    p = a * b
    print(p)
def product(a, b, c):
     p = a * b*c
     print(p)
product(4,5, 5)
        #product(4,5)#error




#2
class Person:
 def Hello(self, name=None):
   if name is not None:
       print('Hello ' + name)
   else:
       print('Hello ')
obj = Person()
obj.Hello()
obj.Hello('Priyanka')



#3
class Compute:
   def area(self, x = None, y = None):
      if x != None and y != None:
         return x * y
      elif x != None:
         return x * x
      else:
         return 0

obj = Compute()
print("Area Value:", obj.area())
print("Area Value:", obj.area(4))
print("Area Value:", obj.area(3, 5))



#4
class Tomato():
    def type(self):
        print("Vegetable")

    def color(self):
        print("Red")


class Apple():
    def type(self):
        print("Fruit")

    def color(self):
        print("Red")


def func(obj):
    obj.type()
    obj.color()


obj_tomato = Tomato()
obj_apple = Apple()
func(obj_tomato)
func(obj_apple)




#4
class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot")


class parrot(Bird):
    def flight(self):
        print("Parrots can fly")


class penguin(Bird):
    def flight(self):
        print("Penguins do not fly")


obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()

obj_bird.intro()
obj_bird.flight()

obj_parr.intro()
obj_parr.flight()

obj_peng.intro()
obj_peng.flight()





#5
from abc import ABC, abstractmethod
class Polygon(ABC):
    def noofsides(self): # abstract method
       pass
class Triangle(Polygon):
    def noofsides(self): # overriding abstract method
       print("I have 3 sides")
class Pentagon(Polygon):
    def noofsides(self): # overriding abstract method
       print("I have 5 sides")
class Hexagon(Polygon):
    def noofsides(self): # overriding abstract method
       print("I have 6 sides")
class Quadrilateral(Polygon):
    def noofsides(self): # overriding abstract method
       print("I have 4 sides")
R = Triangle()
R.noofsides()
K = Quadrilateral()
K.noofsides()
R = Pentagon()
R.noofsides()
K = Hexagon()
K.noofsides()





#6

from abc import ABC, abstractmethod


class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")

    # Driver code


R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()





#7
class Order:
  def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer
  def __len__(self):
       return len(self.cart)
order = Order(['banana', 'apple', 'mango'], 'Real Python')
len(order)
print(len(order))





#8
class Order:
    def __init__(self, cart, customer):
       self.cart = list(cart)
       self.customer = customer
    def __iadd__(self, other):
        self.cart.append(other)
        return 'Hey, I am string!'

order = Order(['banana','apple'],'Real Python')

order +='mango'
print(order)





#9
class Mock:
     def __init__(self, num):
        self.num = num
     def __add__(self, other):
         return Mock(self.num + other)

mock = Mock(5)
mock = mock + 6
print(mock.num)






#10
class Order:
  def __init__(self, cart, customer):
    self.cart = list(cart)
    self.customer = customer
  def __iadd__(self, other):
    self.cart.append(other)
    return self #using self

order = Order(['banana','apple'],'Real Python')

order +='mango'
print(order.cart)






#11
class Person:
  def __init__(self, fname, lname):
   self.firstname = fname
   self.lastname = lname

  def printname(self):
   print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike","Olsen")

x.printname()





#12
class Person:
   def __init__(self, fname, lname):
     self.firstname = fname
     self.lastname = lname
   def printname(self):
     print(self.firstname, self.lastname)
class Student1(Person):
    def __init__(self, fname, lname):
      super().__init__(fname, lname)
      print(self.firstname, self.lastname)
class Student2(Student1):
     def __init__(self, fname, lname):
      super().__init__(fname, lname)
x = Student1("Vivek","Singh")
y = Student2("Priyanka","Singh")






#13
class TeamMember(object): # Parent class 1
  def __init__(self, name, uid):
    self.name = name
    self.uid = uid
class Worker(object): # Parent class 2
    def __init__(self, pay, jobtitle):
     self.pay = pay
     self.jobtitle = jobtitle
class TeamLeader(TeamMember, Worker): # Deriving from the two parent classes
    def __init__(self, name, uid, pay, jobtitle, exp):
      self.exp = exp
      TeamMember.__init__(self, name, uid)
      Worker.__init__(self, pay, jobtitle)
      print("Name: {}, Pay: {}, Exp: {}".format(self.name, self.pay, self.exp))
TL = TeamLeader('Jake', 10001, 250000,'Scrum Master', 5)





#14
class Team:
    def show_Team(self):
       print("This is our Team:")
# Testing class inherited from Team
class Testing(Team):
    TestingName = ""
    def show_Testing(self):
       print(self.TestingName)
# Dev class inherited from Team
class Dev(Team):
     DevName = ""
     def show_Dev(self):
        print(self.DevName)
# Sprint class inherited from Testing and Dev classes
class Sprint(Testing, Dev):
   def show_parent(self):
      print("Testing :", self.TestingName)
      print("Dev :", self.DevName)

s1 = Sprint() # Object of Sprint class
s1.TestingName = "James"
s1.DevName = "Barter"
s1.show_Team()
s1.show_parent()





#15
class Company:
  def __init__(self, name, proj): # constructor
    self.name = name # name(name of company) is public
    self._proj = proj # proj(current project) is protected
  def show(self):
    print("The code of the company is = ",self.ccode)

class Emp(Company):# define child class Emp
    def __init__(self, eName, sal, cname, cproj):# constructor
# calling parent class constructor
     Company.__init__(self, cname, cproj)
     self.n = eName # public member variable
     self.__sal = sal # private member variable
    def show_sal(self):
       print("The project of ",self.name," is ",self._proj)

       print("The salary of ",self.n," is ",self.__sal,)

c = Company("Stark Industries","Mark 4")

e = Emp("Steve", 9999999, c.name, c._proj)

e.show_sal()





#16
class Complex:
   def __init__(self, realpart, imagpart):
     self.r = realpart
     self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i





#17
class Person:

   def __init__(self, name): # init method or constructor

      self.name = name

   def say_hi(self): # Sample Method
      print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()







#18
class Myclass:
   def __init__(self, realpart, imagpart):
     self.r = realpart
     self.i = imagpart
x = Myclass(1.0, -2.5) #x is the instance of MyClass
x.counter = 1
while x.counter < 10:
 x.counter = x.counter * 2
print(x.counter)





#19
class Person:
  def __init__(self, name, age):
   self.name = name
   self.age = age
  def myfunc(self):
   print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age=40
print(p1.age)






#20
class Dog:
  tricks = [] # mistaken use of a class variable
  def __init__(self, name):
   self.name = name
  def add_trick(self, trick):
   self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) # unexpectedly shared by all dogs
print(e.tricks) # unexpectedly shared by all dogs







#21
class Dog:
  def __init__(self, name):
   self.name = name
   self.tricks = [] # creates a new empty list for each dog
  def add_trick(self, trick):
   self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)






#22
    # Function defined outside the class
def f1(self, x, y):
 print(x,x+y)
 return min(x, x+y)





#23
class C:
 f = f1
 def g(self):
  return 'hello world'
 h = g
x1=C()
print(x1.f(10,20))
print(x1.g())




#24
class employee:
  def __init__(self, name, sal):
   self._name=name # protected attribute
   self._salary=sal # protected attribute
e1=employee("Swati", 10000)

print(e1._salary)





#25
class employee:
  def __init__(self, name, sal):
   self.__name=name # private attribute
   self.__salary=sal # private attribute
   self.sal=sal
e1=employee("Bill",10000)

print(e1.sal)





#26
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
  print(f)
