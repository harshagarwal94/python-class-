#1 
class person: 
    def __init__(self,fname, lname): 
        self.fname=fname 
        self.lname=lname 
p1=person("Harsh","Agarwal") 
print(p1.fname,p1.lname) 

 

 

 

#2 
class Dog: 
    kind="cannie" 
    def __init__(self,name): 
        self.name = name 
d=Dog("fibo") 
e=Dog("Buddy") 
print(d.kind) 
print(e.kind) 
print(d.name) 
print(e.name) 






#3  ----14-9-2020
class rectangle: 
 
    def __init__(self,lenght,bredth): 
        self.l=lenght 
        self.b=bredth 
    def area(self): 
        area_rec=self.l*self.b 
        print(area_rec) 
class square(rectangle): 
    pass 
v=square(20,30) 
x=rectangle(20,30) 
x.area() 
v.area() 
 
 
 
 
 #4--------18-9-2020
 class xyz: 
    def You(self): 
        pass 
class abc(xyz): 
    def You(self): 
        print("This is Ghost") 
class uvw(xyz): 
    def You(self): 
        print("You are just a crazy guy") 
r=abc() 
r.You() 
w=uvw() 
w.You() 
 
