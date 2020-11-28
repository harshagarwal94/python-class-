#Program to find electricity unit charge"""
print("plz enter the no of units")
x=int(input())
if(x<50):
    y=x*0.5
    z=0.2*x+y
    print("your total charge is",z)
elif (x<150 and x>50):
    y=x*0.75
    z=0.2*x+y
    print("your total charge is",z)
elif (x<250 and x>150):
    y=x*1.20
    z=0.2*x+y
    print("your total charge is",z)
elif (x>=250 ):
    y=x*1.50
    z=0.2*x+y
    print("your total charge is",z)
else:
    print("wrong choice")
