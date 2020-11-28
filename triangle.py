print("plz enter the 1 side of the triangle")
x=int(input())
print("plz enter the 2 side of the triangle")
y=int(input())
print("plz enter the 3 side of the triangle")
z=int(input())
if x==y==z :
    print("it is an equilateral triangle")
elif(x==y or y==z or z==x):
    print("It is an isosceles triangle")
elif(x!=y and y!=z and z!=x):
    print("It is an scalene triangle")
else:
    print("wrong choice")
