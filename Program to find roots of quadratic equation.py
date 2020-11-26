#Program to find roots of quadratic equation
a=int(input("Write Value of first cofficient" ))
b=int(input("Write Value of second cofficient" ))
c=int(input("Write Value of third cofficient" ))
d=(b*b)-(4*a*c)
if(d>0):
    r1=(-b+math.sqrt(d))/(2*a)
    r2 = (-b-math.sqrt(d)) / (2 * a)
    print("two Distinct Real Roots exists for this equation root1:", r1, "root2", r2)
elif (d==0):
    r1=r2=(-b)/(2*a)
    print(("Two Equal and Real Roots Exists",r1)
elif (d<0):
    r1==r2==(-b)/(2*a);
    img=math.sqrt(d)/(2*a);
    print("Two Distinct Complex Roots Exists: r1 = %f+%f and r2 = %f-%f" %(r1, img, r2, img))
else:
    print("wrong choice")
